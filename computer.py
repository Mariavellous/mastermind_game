# make API requests
import requests
THEME_MAP = {
    "0": "🤵", "1": "👰️", "2": "💒", "3": "🔔",
    "4": "💐", "5": "❤️", "6": "🫶", "7": "🎊"
    }


class Computer:
  def __init__(self):
    pass


# Retrieves randomize integers using random.org API and converts it into emojis.
# Current Theme: Wedding Emojis
  def get_secret_code(self):
      RANDOM_INTEGER_URL_API = "https://www.random.org/integers/"
      params = {
          "num": 4,
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

# Convert random_integers to emoji
      random_emojis = []
      for item in random_integers:
          random_emojis.append(THEME_MAP[item])

      return random_emojis
