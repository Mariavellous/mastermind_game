<script>
  export default {
    data() {
      return {
        my_data: null
      }
    },
    mounted() {
      console.log("Im here")
    },
    methods: {
      async getGame() {
        const response = await fetch("http://127.0.0.1:5037/games/1")
        const json = await response.json();
        this.my_data = json.guesses

      },

      async incrementCounter() {
        this.$store.myCoolAdder()
      }
    }
  }

</script>

<template>
  <div>
    <p>{{$store.counter}}</p>
    <button @click="incrementCounter">Increment Counter</button>
    <button @click="getGame"> Get Game</button>
    <div v-for="item in this.my_data" :key="item"> {{ item.player_guess }} {{item.hint}}</div>
  </div>
  <!--  {{ this.my_data }}-->
</template>

<style scoped>
  button {
    font-size: 10px;
  }

  p {
    text-color: red;
  }
</style>