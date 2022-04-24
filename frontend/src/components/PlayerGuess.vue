<script>
  export default {
    data() {
      return {
        number_of_choices: 4
      }
    }
  }
</script>


<template>
  <div>
    <h1> Player Guess </h1>
    <div class="playerguess">
      <button v-for="index in number_of_choices" :key="index" class="red"> __
      </button>
    </div>

  </div>

</template>

<style>
  button {
    font-size: 5rem
  }

  .red {
    color: darkred;

  }
</style>