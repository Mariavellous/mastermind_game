import { defineStore } from 'pinia'

export const useGameStore = defineStore({
  id: 'game',


  state: () => ({
    currentGuess: [],
    activeRow: 0,
    counter: 0,
    max_attempt_allowed: 10,
    max_guesses_allowed: 4,
    my_data: null,
    gameId: 1,

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
      const response = await fetch("http://127.0.0.1:5037/games/1/guesses",{
          method: 'POST',
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(this.currentGuess)
        })
        await response.raise_for_status()
        const json = await response.json();
        this.my_data = json.guesses
      return this.my_data
    },

    myCoolAdder() {
      this.activeRow += 1
    }


  }
})

