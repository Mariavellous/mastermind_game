import { defineStore } from 'pinia'

export const useGameStore = defineStore({
  id: 'game',


  state: () => ({
    currentGuess: ["4","3"],
    activeRow: 0,
    counter: 0,
    max_attempt_allowed: 10,
    max_guesses_allowed: 4,

  }),


  actions: {
    addEmojiGuess(emoji) {
      this.currentGuess.push(emoji)
    },

    myCoolAdder() {
      this.activeRow += 1
    }


  }
})

