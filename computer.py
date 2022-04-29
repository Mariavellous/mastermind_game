# make API requests
import requests

class Computer:
  def __init__(self, id):
    self.id = id

    # Retrieves randomize integers using random.org API and converts it into emojis.
    # Current Theme: Wedding Emojis
  def get_secret_code(self, num):
      RANDOM_INTEGER_URL_API = "https://www.random.org/integers/"
      params = {
          "num": num,
          "min": 0,
          "max": 7,
          "col": 1,
          "base": 10,
          "format": "plain",
          "rnd": "new",
      }
      response = requests.get(f"{RANDOM_INTEGER_URL_API}",
                              params=params)
      response.raise_for_status()
      random_integers = response.text.replace("\n", "")
      return random_integers


# compares if current_guess == secret code
  def compare_current_guess(self, secret_code, new_guess):
    # create an empty string for hint
    hint = ""
    # if guess[i] equal to right value and index of secret_code, replace both value to None and add "Y" to hint
    for i in range(len(secret_code)):
      if new_guess[i] == secret_code[i]:
          secret_code[i] = None
          new_guess[i] = None
          hint = hint + "Y"

    # if new_guess[i] != none and in secret_code, remove new_guess[i] from secret code and add "M" to hint
    for i in range(len(new_guess)):
      if new_guess[i] != None and new_guess[i] in secret_code:
          hint = hint + "M"
          secret_code.remove(new_guess[i])
    return hint