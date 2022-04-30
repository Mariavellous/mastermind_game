import { defineStore } from 'pinia'
import router from '../router'

export const useGameStore = defineStore({
  id: 'game',

  state: () => ({
    currentGuess: [],
    activeRow: 0,
    max_attempts_allowed: 0,
    number_of_attempts: 0,
    max_guesses_allowed: 4,
    gameId: null,
    guesses: [],
    result: null,
    played_on: null,
    secretCode: null,
    themes: {
      wedding: {
          "0": "🤵‍♂️", "1": "👰‍♀️", "2": "💒", "3": "🔔",
          "4": "💐", "5": "❤️", "6": "🫶", "7": "🎊",
          "empty-emoji": "__", "empty-hint": "🔘"
        },
    },
    currentPlayer: {
      id: null,
      first_name: null,
      last_name: null,
      email_address: null,
    },
    gamesList: [],

  }),

  actions: {
    addEmojiGuess(emoji) {
      if (this.currentGuess.length < this.max_guesses_allowed){
        this.currentGuess.push(emoji)
        return this.currentGuess
      }
    },
    deleteLastEmoji() {
      this.currentGuess.pop()
    },
    async submitGuess() {
      const response = await fetch(`/games/${this.gameId}/guesses`, {
        method: 'POST',
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(this.currentGuess)
      })
      const gameData = await response.json();
      this.updateGameboard(gameData)
    },
    // makes a GET https request and returns the specific game_id#
    async play() {
      const response = await fetch (`/games/${this.gameId}`, {
        method: 'GET',
        credentials: "include",
        headers: {
          "Content-Type": "application/json"
        }
      })
      const gameData = await response.json();
      this.updateGameboard(gameData)
    },

    updateGameboard(gameData) {
      // extract the list of guesses entry from guess table database
      this.guesses = gameData.guesses
      this.result = gameData.game.result
      this.max_attempts_allowed = gameData.game.max_attempts_allowed
      this.number_of_attempts = gameData.game.number_of_attempts
      this.played_on = gameData.game.played_on
      // active row becomes row[last index] + 1
      this.activeRow = gameData.guesses.length
      // erases the previous guess and starts over (empty list)
      this.currentGuess = []
      this.gameId = gameData.game.id
      this.secretCode = gameData.game.secret_code
    },

    async register(newPlayer) {
      const response = await fetch (`/players`, {
        method: 'POST',
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(newPlayer)
      })
      const currentPlayerData = await response.json();
      // newly registered user as the currentPlayer (ready to play)
      this.updateCurrentPlayer(currentPlayerData)
      // lead to display Play game or see list of games
      await router.push({ path: '/games' })
    },

    async autoLogin(){
      const response = await fetch(`/auto_login`, {
        method: 'POST',
      })
      const playerData = await response.json();
      this.updateCurrentPlayer(playerData)
    },
    async login(player) {
      const response = await fetch(`/login`, {
        method: 'POST',
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(player)
      })
      const playerData = await response.json();
      // successful login player becomes currentPlayer (ready to play)
      this.updateCurrentPlayer(playerData)
      // lead to display Play game or see list of games
      await router.push({ path: '/games' })
    },

    // retrieves player information and update currentPlayer
    updateCurrentPlayer(player) {
      this.currentPlayer.id = player.id
      this.currentPlayer.first_name = player.first_name
      this.currentPlayer.last_name = player.last_name
      this.currentPlayer.email_address =player.email_address
    },

    async getGames() {
      const response = await fetch(`/games`, {
        method: 'GET',
        credentials: "include",
        headers: {
          "Content-Type": "application/json"
        },
      })
      // retrieve list of games data from database
      const gamesData = await response.json();
      this.gamesList = gamesData
      console.log(this.gamesList)

    },
    async newGame() {
      const response = await fetch("/games", {
        method: 'POST',
        credentials: 'include',
        headers: {
          "Content-Type": "application/json"
      },
      })
      // retrieves data about new game_id
      const gameData = await response.json();
      this.updateGameboard(gameData)
      console.log(this.gameId)
      await router.push({ path: `/games/${this.gameId}` })
    },
    async logout() {
      const response = await fetch("/logout", {
        method: 'DELETE',
        credentials: 'include',
        headers: {
          "Content-Type": "application/json"
        },
      })

      this.currentPlayer = {
        id: null,
        first_name: null,
        last_name: null,
        email_address: null,
      }
      await router.push({path:`/`})

    }

  }
})

