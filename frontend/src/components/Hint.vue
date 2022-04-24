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
    <h1> Hint </h1>
    <div class="playerguess">
      <button v-for="index in number_of_choices" :key="index" class="hint"> 🔘 </button>
    </div>

  </div>

</template>

<style>
.hint {
  font-size: 1rem;
  color: darkred;

}
</style>