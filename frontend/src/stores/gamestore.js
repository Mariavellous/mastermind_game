import { defineStore } from 'pinia'

export const useGameStore = defineStore({
  id: 'game',


  state: () => ({
    currentGuess: [],
    activeRow: 0,
    counter: 0,
    max_attempt_allowed: 10,
    max_guesses_allowed: 4,

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
    submitGuess() {
      console.log(this.currentGuess)
      return this.currentGuess
    },

    myCoolAdder() {
      this.activeRow += 1
    }


  }
})

