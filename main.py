from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, and_, desc
from sqlalchemy.ext.automap import automap_base
import os
# enable Cross-Origin Resource Sharing (CORS) in Flask, since our front-and back-end will be served on separate ports
from flask_cors import CORS
from computer import Computer
from datetime import datetime
from flask_login import UserMixin, LoginManager, login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

# library that takes key values in .env and places them in the "environment/computer" (where app is running)
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
# generates the CSRF token similar to the Flask app secret key
app.config["SECRET_KEY"] = os.environ["MASTERMIND_SECRET_KEY"]
app.config["DEBUG"] = True

CORS(app, resources={r'/*': {'origins': ['http://localhost:3000', 'http://localhost:5037']}}, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'

# Connect to database
# creates a new database
# this needs to connect to the Heroku database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("MASTERMIND_DATABASE_URL")
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

# mastermind database, has three tables "players", "guesses" and "games" set up
Base = automap_base(db.Model)

login_manager = LoginManager()
login_manager.init_app(app)


class Games(Base, db.Model):
    # extracts information from database row (sqlalchemy orm)
    def serialize(self):
        secret_code = self.secret_code
        secret_code_length = len(self.secret_code)

        # hide secret_code if game is not done
        if self.result == None:
            secret_code = None

        return {
            'id': self.id,
            'player_one_id': self.player_one_id,
            'player_two_id': self.player_two_id,
            'result': self.result,
            'secret_code': secret_code,
            'number_of_attempts': self.number_of_attempts,
            'max_attempts_allowed': self.max_attempts_allowed,
            'played_on': self.played_on,
            'secret_code_length': secret_code_length
        }


class Guesses(Base, db.Model):
    # extracts information from database row (sqlalchemy orm)
    def serialize(self):
        return {
            'id': self.id,
            'game_id': self.game_id,
            'player_id': self.player_id,
            'player_guess': self.player_guess,
            'hint': self.hint,
        }


class Players(Base, UserMixin, db.Model):
    # extracts information from database row(sqlachemy orm)
    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email_address': self.email_address,
        }


# reflect the tables
Base.prepare(db.engine, reflect=True)

# Check to see if "computer@reach.com" exist in database, otherwise make it.
# Robot / "computer" will always be player_two (playing against the "computer")
robot = Players.query.filter_by(email_address="computer@reach.com").first()
if robot == None:
    robot = Players(first_name="Computer", last_name="Computer", email_address="computer@reach.com",
                    password="password")
    db.session.add(robot)
    db.session.commit()

# Create Computer class
# Player will play against computer (User VS "Computer")
computer = Computer(robot.id)


# Render the main template
@app.route('/')
def home():
    return render_template('index.html')


# Return list of games for player_id and total num of games won and games lost
@app.route('/games', methods=['GET'])
@login_required
def show_games():
    # return current player's list of games
    games = Games.query.filter(
        or_(Games.player_one_id == current_user.id, Games.player_two_id == current_user.id)
    ).order_by(desc(Games.id)).all()
    list_of_games = list(map(lambda game: game.serialize(), games))

    # Calculate games_won / games_lost
    games_won = Games.query.filter(and_(Games.player_one_id == current_user.id, Games.result == True)).count()
    games_lost = Games.query.filter(and_(Games.player_one_id == current_user.id, Games.result == False)).count()
    data = {"games_won": games_won, "games_lost": games_lost, "games": list_of_games}
    return jsonify(data)


# Creates a new game for player_id with a chosen difficulty level playing against "computer"
@app.route('/games', methods=['POST'])
@login_required
def create_new_game():
    # retrieve the difficulty mode level: length of secret_code (4, 5, 6)
    mode = request.json

    # Special Step: Computer class will fetch secret code
    length_of_secret_code = mode
    secret_code_list = computer.get_secret_code(length_of_secret_code)

    # Special Step: Update the Games table
    # turns the list into str for easy storage into database
    secret_code = "".join(secret_code_list)
    new_game = Games(player_one_id=current_user.id, player_two_id=computer.id, secret_code=secret_code,
                     played_on=datetime.now())
    db.session.add(new_game)
    db.session.commit()
    new_game_id = new_game.id
    return get_game_id(new_game_id)


# This route retrieves information about a specific game (game_id, player_one_id, player_two_id (default: computer),
# result, secret_code, num_attempts, max_attempts, played_on date) from the Games table and
# list_of_guesses for a specific game_id from Guesses table
@app.route('/games/<int:game_id>', methods=['GET'])
@login_required
def get_game_id(game_id):
    game = Games.query.get(game_id)
    guesses = Guesses.query.filter_by(game_id=game_id).all()
    game_json = game.serialize()

    # Loops through each guess, and extracts data from guess SQLAlchemy object (by calling guess.serialize() on each)
    list_of_guesses_json = list(map(lambda guess: guess.serialize(), guesses))
    data = {"game": game_json, "guesses": list_of_guesses_json}
    # returns data in json format
    return jsonify(data)


# Creates player's guess on Guess table. Compares the player's guess to the secret code. Computer will provide hints.
# The game is over if game result is either True or False.
@app.route('/games/<int:game_id>/guesses', methods=['POST'])
@login_required
def create_new_guess(game_id):
    current_player_id = current_user.id
    # Retrieve the game_id data to retrieve the secret_code
    game = Games.query.filter_by(id=game_id).first()

    # makes sure that this game belongs to player_one_id so that no one else can make guesses
    if game.player_one_id != current_user.id:
        return f"You are not allowed to make guesses.", 400
    # retrieve player's guess
    new_guess = request.json
    string_new_guess = "".join(request.json)

    if len(new_guess) != len(game.secret_code):
        return f"Guess number needs to be {len(game.secret_code)} emojis", 400

    # convert secret code string from Game table into list/array
    secret_code = list(game.secret_code)

    # compare current_guess to secret code and return hint
    hint = computer.compare_current_guess(secret_code, new_guess)

    # add a new entry to the guess table
    guess = Guesses(player_id=current_player_id, game_id=game_id, player_guess=string_new_guess, hint=hint)
    db.session.add(guess)

    game.player_one_id = current_player_id
    game.number_of_attempts += 1

    # update "result" column in games table
    # Game Logic: The game ends if game.result is true or false. Game continues if game.result = None
    # Perfect hint == All "Y"s
    perfect_hint = "Y" * len(game.secret_code)
    if hint == perfect_hint:
        game.result = True
    elif game.number_of_attempts == game.max_attempts_allowed:
        game.result = False
    else:
        game.result = None

    game.played_on = datetime.now()
    db.session.commit()

    # Return updated game
    return get_game_id(game_id)


# Register new player and save data in Players table
@app.route('/players', methods=['POST'])
def register_player():
    # retrieves data from user_input
    new_player = request.json
    # Generate a hash of the password
    password = generate_password_hash(password=new_player['password'], method='pbkdf2:sha256', salt_length=8)
    player = Players(first_name=new_player['first_name'], last_name=new_player['last_name'],
                     email_address=new_player['email_address'],
                     password=password)
    db.session.add(player)
    db.session.commit()
    login_user(player)
    # return player's data except the player's password back to the frontend
    return player.serialize()


# Player will login successfully if check_password_hash = true
@app.route('/login', methods=['POST'])
def login():
    # retrieves data from user input
    player = request.json
    email_address = player["email_address"]
    password = player["password"]
    user = Players.query.filter(Players.email_address == email_address).first()
    if user == None:
        error = "That email does not exist. Please try again"
        return error
    elif check_password_hash(user.password, password):
        login_user(user)
        return user.serialize()
    else:
        error = "Incorrect password. Please try again."
        return error


# Called when the game loads. Login the user automatically
@app.route('/auto_login', methods=['POST'])
@login_required
def auto_login():
    return current_user.serialize()


# Player wants to log out of the game
@app.route('/logout', methods=['DELETE'])
@login_required
def logout():
    logout_user()
    return '', 204


@login_manager.user_loader
def load_user(user_id):
    return Players.query.get(user_id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5037)
