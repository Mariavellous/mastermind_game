
-- DROP TABLE IF EXISTS mastermind;
-- DROP TABLE IF EXISTS guesses, games, players;
-- CREATE DATABASE mastermind;
-- CREATE SCHEMA public;

CREATE TABLE IF NOT EXISTS players(
    id INTEGER PRIMARY KEY  AUTOINCREMENT,
    first_name VARCHAR(30) NOT NULL CHECK (length(first_name) > 0),
    last_name VARCHAR(30) NOT NULL CHECK (length(last_name) > 0),
    email_address VARCHAR(50) UNIQUE NOT NULL CHECK(email_address LIKE '%@%.%'),
    password VARCHAR NOT NULL CHECK (length(password) > 6)
);

CREATE TABLE IF NOT EXISTS games(
    id INTEGER CONSTRAINT game_id PRIMARY KEY AUTOINCREMENT,
    player_one_id INTEGER NOT NULL,
    player_two_id INTEGER,
    result BOOLEAN DEFAULT NULL,
    secret_code VARCHAR(30) NOT NULL,
    number_of_attempts INTEGER DEFAULT 0,
    max_attempts_allowed INTEGER DEFAULT 10 NOT NULL,
    played_on timestamp,
    CONSTRAINT player_one_id_fk FOREIGN KEY (player_one_id) REFERENCES players (id),
    CONSTRAINT player_two_id_fk FOREIGN KEY (player_two_id) REFERENCES players (id)
);

CREATE TABLE IF NOT EXISTS guesses(
    id INTEGER CONSTRAINT table_id PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL,
    game_id INTEGER NOT NULL,
    player_guess VARCHAR(30) NOT NULL,
    hint VARCHAR(6) NOT NULL,
    CONSTRAINT player_id_fk FOREIGN KEY (player_id) REFERENCES players (id),
    CONSTRAINT game_id_fk FOREIGN KEY (game_id) REFERENCES games (id)
);

--
-- -- Create initial players
-- INSERT INTO players(first_name, last_name, email_address, password)
-- VALUES('Melanie', 'Alcaide', 'mariamelanie@gmail.com', 'melanie');
--
-- INSERT INTO players(first_name, last_name, email_address, password)
-- VALUES ('Computer', 'Computer', 'example@gmail.com', 'example');
--
-- INSERT INTO games(player_one_id, player_two_id, secret_code, max_attempts_allowed, played_on)
-- VALUES (1, 2, '1234', 8, CURRENT_TIMESTAMP);
--
-- -- Try to guess the secret code
-- INSERT INTO guesses(player_id, game_id, player_guess, hint)
-- VALUES (2, 1, 2345, 'YYNN');
-- -- Update the number_of_attempts on games table after each attempt
-- UPDATE games SET number_of_attempts = (SELECT COUNT(*) FROM guesses WHERE game_id = 1) WHERE id = 1;
-- -- Check if player_answer == secret_code, update games.result to True, game ends, and update UI
--
--
-- INSERT INTO guesses(player_id, game_id, player_guess, hint)
-- VALUES (2, 1, 3456, 'YNYN');
-- UPDATE games SET number_of_attempts = (SELECT COUNT(*) FROM guesses WHERE game_id = 1) WHERE id = 1;
--
--
-- INSERT INTO guesses(player_id, game_id, player_guess, hint)
-- VALUES (2, 1, 4566, 'YNYN');
-- UPDATE games SET number_of_attempts = (SELECT COUNT(*) FROM guesses WHERE game_id = 1) WHERE id = 1;
--
--
-- INSERT INTO guesses(player_id, game_id, player_guess, hint)
-- VALUES (2, 1, 3456, 'YNYN');
-- UPDATE games SET number_of_attempts = (SELECT COUNT(*) FROM guesses WHERE game_id = 1) WHERE id = 1;
--
--
-- INSERT INTO guesses(player_id, game_id, player_guess, hint)
-- VALUES (2, 1, 3456, 'YNYN');
-- UPDATE games SET number_of_attempts = (SELECT COUNT(*) FROM guesses WHERE game_id = 1) WHERE id = 1;
--
-- INSERT INTO guesses(player_id, game_id, player_guess, hint)
-- VALUES (2, 1, 3456, 'YNYN');
-- UPDATE games SET number_of_attempts = (SELECT COUNT(*) FROM guesses WHERE game_id = 1) WHERE id = 1;
--
-- INSERT INTO guesses(player_id, game_id, player_guess, hint)
-- VALUES (2, 1, 3456, 'YNYN');
-- UPDATE games SET number_of_attempts = (SELECT COUNT(*) FROM guesses WHERE game_id = 1) WHERE id = 1;
--
-- INSERT INTO guesses(player_id, game_id, player_guess, hint)
-- VALUES (2, 1, 3456, 'YNYN');
-- UPDATE games SET number_of_attempts = (SELECT COUNT(*) FROM guesses WHERE game_id = 1) WHERE id = 1;
--
--
-- -- After max_attempt is reached, update the games table
-- UPDATE games SET result = (SELECT hint from guesses WHERE hint = 'YYYY') WHERE id = 1;
--
--
-- SELECT hint from guesses WHERE hint = 'YYYY'