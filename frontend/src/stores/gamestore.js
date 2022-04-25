import { defineStore } from 'pinia'

export const useGameStore = defineStore({
  id: 'game',


  state: () => ({
    currentGuess: [],
    activeRow: 0,
    counter: 0,
    max_attempt_allowed: 1

  }),


  actions: {
    addEmojiGuess(emoji) {
      this.currentGuess.push(emoji)
      this.counter++
    },

    myCoolAdder() {
      this.activeRow += 1
    }


  }
})

