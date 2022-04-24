<script>
  export default {
    data() {
      return {
        number_of_choices: 4,
        max_attempt_allowed: 10
      }
    }
  }
</script>


<template>
  <div>
    <h1> Player Guess </h1>
    <div v-for="index in max_attempt_allowed" :key="index" class="playerguess">
      {{ index }} <button v-for="index in number_of_choices" :key="index" class="line"> __
      </button>
      <button v-for="index in number_of_choices" :key="index" class="hint"> 🔘 </button>

    </div>

  </div>

</template>

<style>
  button {
    font-size: 5rem
  }

  .line {
    color: darkgrey;

  }

  .hint {
    font-size: 1rem
  }
</style>