<script>
  export default {
    data() {
      return {
        number_of_choices: 4,
      }
    },
    props: {
      row: Number,
    },
    // Change the displayed label of row to be user friendly (original start at 0)
    computed: {
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
      guesses() {
        if (this.isActive) {
          this.$store.currentGuess.push("icons")
        }

      }
    }
  }
</script>


<template>
<!--    {{$store.max_attempt_allowed}}-->
    <div :class="{'active-row': isActive, test: true, }">
      <p> {{this.rowLabel}} </p>
      <button v-for="index in number_of_choices" :key="index" class="line"> __ </button>
      <button v-for="index in number_of_choices" :key="index" class="hint"> 🔘 </button>
    </div>
</template>

<style>
.hint {
  font-size: 1rem;
}
</style>