<script>
  export default {
    data() {
      return {

      }
    },
    methods: {
      select() {
        // go to the respective spot
      }
    }
  }
</script>

<template>
  <div>
    <div class="wrap">
      <h1> ICON CHOICES </h1>
      <button :click="select"> 🤵‍♂️️‍</button>
      <button :click="select"> 👰‍♀️</button>
      <button :click="select"> 💒</button>
      <button :click="select"> 🔔</button>
      <button :click="select"> 💐</button>
      <button :click="select"> ❤️</button>
      <button :click="select"> 🫶</button>
      <button :click="select"> 🎊</button>
    </div>

    <button> Submit </button>

  </div>

</template>

<style>
button {
  font-size: 5rem
}
</style>

