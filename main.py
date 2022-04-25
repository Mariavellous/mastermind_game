from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import insert
from sqlalchemy.ext.automap import automap_base
import os
# enable Cross-Origin Resource Sharing (CORS) in Flask, since our front-and back-end will be served on separate ports
from flask_cors import CORS
import psycopg2
from computer import Computer
from datetime import datetime




# library that takes key values in .env and places them in the "environment/computer" (where app is running)
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
# generates the CSRF token similar to the Flask app secret key
app.config["SECRET_KEY"] = os.environ["MASTERMIND_SECRET_KEY"]
app.config["DEBUG"] = True
CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}}, CORS_SUPPORTS_CREDENTIALS=True)
app.config['CORS_HEADERS'] = 'Content-Type'

# Connect to database
# creates a new database
# this connects to the Heroku database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("MASTERMIND_DATABASE_URL")
app.config["SQLACHEMY_TRACK_MODIFICARIONS"] = True
app.config["SQLACHEMY_ECHO"] = True
db = SQLAlchemy(app)

# mastermind database, has three tables "players", "guesses" and "games" set up
Base = automap_base(db.Model)

# reflect the tables
Base.prepare(db.engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name
Players = Base.classes.players
Guesses = Base.classes.guesses
Games = Base.classes.games


# turns the sqlalchemy orm object into json format
def serialize(obj):
    if type(obj) is list:
        return serialize_list(obj)
    data = obj.__dict__
    keys_to_remove = ['_sa_instance_state', '__len__']
    for k in keys_to_remove:
        data.pop(k, None)
    return data


# turn the list of sqlalchemy.orm objects into json format
def serialize_list(obj):
    data = []
    for item in obj:
        new_item = serialize(item)
        data.append(new_item)
    return data


# db.session.add(p)
# db.session.commit()


THEME_MAP = {
    "0": "🤵", "1": "👰️", "2": "💒", "3": "🔔",
    "4": "💐", "5": "❤️", "6": "🫶", "7": "🎊"
    }

computer = Computer()


# Retrieves randomize integers using random.org API and converts it into emojis.
# Current Theme: Wedding Emojis
# def get_secret_code():
#     RANDOM_INTEGER_URL_API = "https://www.random.org/integers/"
#     params = {
#         "num": 4,
#         "min": 0,
#         "max": 7,
#         "col": 1,
#         "base": 10,
#         "format": "plain",
#         "rnd": "new",
#     }
#     response = requests.get(f"{RANDOM_INTEGER_URL_API}",
#                             params=params)
#     response.raise_for_status()
#     random_integers = response.text.replace("\n", "")
#
#     # Convert random_integers to emoji
#     random_emojis = []
#     for item in random_integers:
#         random_emojis.append(THEME_MAP[item])
#
#     return random_emojis


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/games', methods=['POST'])
def create_new_game():
    # Special Step: fetch secret code
    # secret_code = get_secret_code()
    secret_code_list = computer.get_secret_code()
    # Special Step: Update Guess table
    current_player_id = 1
    # turns the list into str for easy storage into database
    secret_code = "".join(secret_code_list)
    new_game = Games(player_one_id=current_player_id, secret_code=secret_code, played_on=datetime.now())
    db.session.add(new_game)
    db.session.commit()

    player_one_guess = '2345'
    # game = Games.query.filter_by(player_one_id=current_player_id).first()
    return render_template('index.html')


# This route retrieves information about a specific game (game_id, player_one_id, player_two_id (default: computer),
# result, secret_code, num_attempts, max_attempts, played on_
# and list_of_guesses for a specific game_id from guesses table
@app.route('/games/<int:game_id>', methods=['GET'])
def get_game_id(game_id):
    game = Games.query.get(game_id)
    guesses = Guesses.query.filter_by(game_id=game_id).all()
    game_json = serialize(game)
    list_of_guesses_json = serialize(guesses)
    data = {"game": game_json, "guesses": list_of_guesses_json}
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5037)