<script>
  export default {
    data() {
      return {
        THEME_MAP: this.$store.themes.wedding
      }
    },
    props: {
      index: Number,
      guess: Object,
    },
    // Computed: tracks other reactive state. Automatically updates it when its dependencies change
    computed: {
      // Change the displayed label of row to be user friendly (original start at 0)
      rowLabel() {
        return this.index + 1
      },
    // Checks if current row is active
      isActive() {
        if(this.$store.activeRow === this.index) {
          return true
        }
        return false
      },
      playerGuessData() {
        // 5 < 5
        if (this.index < this.$store.guesses.length) {
          return this.$store.guesses[this.index].player_guess
        } else if (this.isActive) {
          return this.$store.currentGuess
        } else {
          return []
        }
      },
      hintData() {
        // 5 < 5
        if (this.index < this.$store.guesses.length){
          return this.$store.guesses[this.index].hint
        }
        return []
      },
      // Displays player's guesses on active row
      guesses() {
        // Still display empty_box as placeholder if emojis > max_choices_allowed
        let copy = Array.from(this.playerGuessData)
        if (copy.length < this.$store.max_guesses_allowed) {
          let num_empty_box = this.$store.max_guesses_allowed - copy.length
          for (let i = 0; i < num_empty_box; i++) {
            copy.push("empty-emoji")
          }
        }
        // debugger
        return copy
      },

      hints() {
        // Displays hints if this is active and button is submitted
        // if (this.isActive) {
          let copy = Array.from(this.hintData)
          if (copy.length < this.$store.max_guesses_allowed) {
            let num_empty_box = this.$store.max_guesses_allowed - copy.length
            for(let i = 0; i < num_empty_box; i++) {
              copy.push("🔘")
            }
          }
        return copy
        // }
      }
    }
  }
</script>


<template>
<!--Displays player_guess and hint together as one row. Identifies self if active -->
    <div :class="{'active-row': isActive, 'centered-flexbox': true, 'guess-row': true}">
      <h1> {{this.rowLabel}} </h1>
      <button v-for="(emoji,index) in guesses" :key="index" class="line">{{THEME_MAP[emoji]}}</button>
      <div class="hint-container">
        <button v-for="(hint,index) in hints" :key="index" class="hint"> {{hint}} </button>
      </div>

    </div>
</template>

<style scoped>
.hint {
  font-size: 1rem;
}
h1 {
  margin-right: 15px;
  width: 50px;
  text-align: right;
}

.line {
  width: 65px;
  height: 65px;
}

.hint {
  width: 30px;
  height: 30px;
}

</style>