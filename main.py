from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
import os
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

# db.session.add(p)
# db.session.commit()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5038)