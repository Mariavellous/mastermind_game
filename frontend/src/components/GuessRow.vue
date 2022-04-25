<script>
  export default {
    props: {
      row: Number,
    },
    // Computed: tracks other reactive state. Automatically updates it when its dependencies change
    computed: {
      // Change the displayed label of row to be user friendly (original start at 0)
      rowLabel() {
        return this.row + 1
      },
    // Checks if current row is active
      isActive() {
        if(this.$store.activeRow === this.row) {
          return true
        }
        return false
      },
      // Displays player's guesses on active row
      guesses() {
        // Still display empty_box as placeholder if emojis > max_choices_allowed
        if (this.isActive) {
          let copy = Array.from(this.$store.currentGuess)
          if (copy.length < this.$store.max_guesses_allowed) {
            let num_empty_box = this.$store.max_guesses_allowed - copy.length
            for(let i = 0; i < num_empty_box; i++) {
              copy.push("__")
            }
            return copy
          }
          return copy
        }
        return ["__", "__", "__", "__"]
      }
    }
  }
</script>


<template>
<!--    {{$store.max_attempt_allowed}}-->
<!--Displays player_guess and hint together as one row. Identifies self if active -->
    <div :class="{'active-row': isActive, test: true, }">
      <p> {{this.rowLabel}} </p>
      <button v-for="emoji in guesses" :key="emoji" class="line"> {{emoji}}</button>
      <button v-for="index in this.$store.max_guesses_allowed" :key="index" class="hint"> 🔘 </button>
    </div>
</template>

<style>
.hint {
  font-size: 1rem;
}
</style>