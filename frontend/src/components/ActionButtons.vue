<script>
  export default {
    data() {
      return {
        info: []

      }
    },
    methods: {
      select(event) {
        this.$store.addEmojiGuess(event.target.value)
        // console.log(guess)
      },
      undo() {
        this.$store.deleteLastEmoji()
      },
      submit() {
        this.$store.submitGuess()
      }
    }
  }
</script>

<template>
  <div>
    <div class="wrap">
      <h1> ICON CHOICES </h1>
      <button @click="select" value="🤵‍♂"> 🤵‍♂️️‍</button>
      <button @click="select" value="👰‍♀"> 👰‍♀️</button>
      <button @click="select" value="💒"> 💒</button>
      <button @click="select" value="🔔"> 🔔</button>
      <button @click="select" value="💐"> 💐</button>
      <button @click="select" value="❤️"> ❤️</button>
      <button @click="select" value="🫶"> 🫶</button>
      <button @click="select" value="🎊"> 🎊</button>
    </div>

    <button @click="submit"> Submit </button>
    <div>  <button @click="undo"> Undo </button></div>

  </div>
{{ this.info }}
</template>

<style>
button {
  font-size: 5rem
}
</style>

