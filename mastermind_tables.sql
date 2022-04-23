
-- DROP TABLE IF EXISTS mastermind;
DROP TABLE IF EXISTS players, games, guesses, computer;
-- CREATE DATABASE mastermind;
-- CREATE SCHEMA public;

CREATE TABLE players(
id SERIAL PRIMARY KEY,
first_name VARCHAR(30) NOT NULL,
last_name VARCHAR(30) NOT NULL,
email_address VARCHAR(50) UNIQUE NOT NULL,
password VARCHAR NOT NULL
);


CREATE TABLE games(
    id SERIAL CONSTRAINT game_id PRIMARY KEY,
    player_one_id INTEGER NOT NULL,
    CONSTRAINT player_one_id_fk FOREIGN KEY (player_one_id) REFERENCES players (id),
    player_two_id INTEGER,
    CONSTRAINT player_two_id_fk FOREIGN KEY (player_two_id) REFERENCES players (id),
    result BOOLEAN DEFAULT FALSE,
    secret_code VARCHAR(6) NOT NULL,
    number_of_attempts INTEGER DEFAULT 0,
    max_attempts_allowed INTEGER NOT NULL,
    played_on timestamp
);

CREATE TABLE guesses(
    id SERIAL CONSTRAINT table_id PRIMARY KEY,
    player_id INTEGER NOT NULL,
    CONSTRAINT player_id_fk FOREIGN KEY (player_id) REFERENCES players (id),
    game_id INTEGER NOT NULL,
    CONSTRAINT game_id_fk FOREIGN KEY (game_id) REFERENCES games (id),
    player_guess VARCHAR(20) NOT NULL,
    hint VARCHAR(6) NOT NULL
);

INSERT INTO players(first_name, last_name, email_address, password)
VALUES ('Computer', 'Computer', 'computer@example.com', 'password');

INSERT INTO players(first_name, last_name, email_address, password)
VALUES('Melanie', 'Alcaide', 'melanie@gmail.com', 'melanie');

INSERT INTO games(player_one_id, player_two_id, secret_code, max_attempts_allowed, played_on)
VALUES (1, 2, '1234', 8, CURRENT_TIMESTAMP);

-- Try to guess the secret code
INSERT INTO guesses(player_id, game_id, player_guess, hint)
VALUES (2, 1, 2345, 'YYNN');
-- Update the number_of_attempts on games table after each attempt
UPDATE games SET number_of_attempts = (SELECT COUNT(*) FROM guesses WHERE game_id = 1) WHERE id = 1;
-- Check if player_answer == secret_code, update games.result to True, game ends, and update UI


INSERT INTO guesses(player_id, game_id, player_guess, hint)
VALUES (2, 1, 3456, 'YNYN');
UPDATE games SET number_of_attempts = (SELECT COUNT(*) FROM guesses WHERE game_id = 1) WHERE id = 1;


INSERT INTO guesses(player_id, game_id, player_guess, hint)
VALUES (2, 1, 4566, 'YNYN');
UPDATE games SET number_of_attempts = (SELECT COUNT(*) FROM guesses WHERE game_id = 1) WHERE id = 1;


INSERT INTO guesses(player_id, game_id, player_guess, hint)
VALUES (2, 1, 3456, 'YNYN');
UPDATE games SET number_of_attempts = (SELECT COUNT(*) FROM guesses WHERE game_id = 1) WHERE id = 1;


INSERT INTO guesses(player_id, game_id, player_guess, hint)
VALUES (2, 1, 3456, 'YNYN');
UPDATE games SET number_of_attempts = (SELECT COUNT(*) FROM guesses WHERE game_id = 1) WHERE id = 1;

INSERT INTO guesses(player_id, game_id, player_guess, hint)
VALUES (2, 1, 3456, 'YNYN');
UPDATE games SET number_of_attempts = (SELECT COUNT(*) FROM guesses WHERE game_id = 1) WHERE id = 1;

INSERT INTO guesses(player_id, game_id, player_guess, hint)
VALUES (2, 1, 3456, 'YNYN');
UPDATE games SET number_of_attempts = (SELECT COUNT(*) FROM guesses WHERE game_id = 1) WHERE id = 1;

INSERT INTO guesses(player_id, game_id, player_guess, hint)
VALUES (2, 1, 3456, 'YNYN');
UPDATE games SET number_of_attempts = (SELECT COUNT(*) FROM guesses WHERE game_id = 1) WHERE id = 1;


-- After max_attempt is reached, update the games table
UPDATE games SET result = (SELECT hint from guesses WHERE hint = 'YYYY') WHERE id = 1;


SELECT hint from guesses WHERE hint = 'YYYY'