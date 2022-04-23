from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
import os
from sqlalchemy_serializer import SerializerMixin
import psycopg2

# library that takes key values in .env and places them in the "environment/computer" (where app is running)
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
# generates the CSRF token similar to the Flask app secret key
app.config["SECRET_KEY"] = os.environ["MASTERMIND_SECRET_KEY"]
app.config["DEBUG"] = True


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
    data = obj.__dict__
    keys_to_remove = ['_sa_instance_state', '__len__']
    for k in keys_to_remove:
        data.pop(k, None)
    return data


# db.session.add(p)
# db.session.commit()


# @app.route('/')
# def home():
#     return render_template('index.html')

# /recipe?game_id=1&guesses=xxxx
# This route retrieves information about a specific game (game_id, player_one_id, player_two_id (default: computer),
# result, secret_code, num_attempts, max_attempts, played on_
@app.route('/games/<int:game_id>', methods=['GET'])
def get_game_id(game_id):
    game = Games.query.get(game_id)
    if request.headers.get('Accept') == "application/json":
        return serialize(game)
    else:
        return render_template('game.html', game=game)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5038)