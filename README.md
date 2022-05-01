# How to run the code.
list steps in building, running and playing 

### 1. Database

For the purposes of this demo, a SQLite db file has already been created with sample data in `mastermind.db`  
Created tables via sql in  `mastermind_tables.sql`

### 2. Environment Variables 

The `.env` file stores the secret key and database url to protect the database and any other important information.  

Place environment variables inside a file named `.env`

```
MASTERMIND_SECRET_KEY=mastermind
MASTERMIND_DATABASE_URL=sqlite:///mastermind.db
```

### 3. Build the frontend

First, change directory to `frontend` folder. In order to execute all the files written in vue.js `npm install` installs the dependencies. 
Run the 'build' files in the front end. Change directory back to the route of the project. 



```sh 
cd frontend
npm install
npm run build
cd ..
```

#### 4. Install all necessary requirements. 

I used the flask framework to develop the web applications along with flask_sqlalchemy 
and sqlachemy to communicate to the database. 

```sh
pip3 intall -r requirements.txt
```

#### 5. Start the server

```sh
python3 main.py 
```

#### 6. Play the game

Open [http://127.0.0.1:5037](http://127.0.0.1:5037) in your browser


# Thought Process 
Brainstorm information that needs to be stored in database. This holds valuable data and acts as the brain for the entire application which will lead the direction for the rest of the code. 

I know that I want different players stored in the database so that they can register and login. Therefore, I need a `Players` table. 

I want to be able to store the secret code of the specific game. I need to be able to remember all the players' guesses so a `Guesses` table is a must. The player will be playing against the computer that will provide hints to the player which will be stored in this table as well. 

These tables are reliant of each other: player's guesses and hints are tied to the specific game_id of the game from `Games` table. Then `Games` table relies on the `Players` table because the specific game is owned to the player's information. I want to be able to display 
all the games of each players to show completed games or in-progress games so that players have option to review it or come back at another time. 

INSERT tables database drawing here....


# Code Structure 
Created a `Computer Class` responsible for 
* creating the secret code via random.org api 
* comparing the player's guess to the secret code and returns the "hint". 

HINT 

hint = " "
1) Each character of the guess will be compared to the character of the secret code. If it is a match, both character will be replaced with None value and add "Y" (YES - right position and right character) to the hint string.
2) Will then loop through each guess character that are not None and see character is inside the secret code list. If character exist in secret code it will be replaced with None and add "M" (character exist but wrong position) to the hint. 

Created RESTFUL API routes in the server 
* `POST` /games  --> creates a brand new game 
* `GET` /games --> shows list of games for player 
* `GET` /games/<int:game_id/guesses --> get specific game_id
* `POST` /games/<int:game_id/guesses --> creates new guess 
* `POST` /players --> register player 
* `GET` /login --> login player 
* `DELETE` /logout --> logout player

Most if not all https request from the frontend, the database gets updated and stores the new data in its respective tables. 
The server then returns a response of all data needed to display in the frontend. 


# Creative Extension Implemented 
* I used the randomized numbers from random.org API as a key to the dictionary of emojis. I chose the theme wedding as an homage to a very recent special day for me. 
* Players are able to view scores: games won and games lost 
* Add easy, medium, difficult level by: changing the number of max number of choices to 4, 5, 6. 



# Creative Extensions Attempted 
* I would love to for users to be able to choose different themes that will display different emojis for the foodie, animal lover, flags for travelers, etc. 
* Add difficulty level by: decreasing the number of max_attempts_allowed to 9 or lower. 


