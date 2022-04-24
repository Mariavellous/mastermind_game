<script>
  export default {
    data () {
      return {
        my_data: null
      }
    },
    methods: {
      async getGame() {
        const response = await fetch("http://127.0.0.1:5037/games/1")
        const json= await response.json();
        this.my_data = json.guesses

      }
    }
  }

</script>

<template>
  <button @click="getGame"> Get Game </button>
<div v-for="item in this.my_data" :key="item"> {{ item.player_guess }} {{item.hint}}</div>
  <p>Show work here</p>
<!--  {{ this.my_data }}-->
</template>

<style>
p {
  text-color: red;
}
</style>