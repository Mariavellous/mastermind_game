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
    },
  },
  computed: {
    gameCompleted() {
      if (this.$store.result !== null) {
        return true
      }
      return false
    }
  }
}
</script>

<template>
  <div class="action-buttons centered-flexbox">
    <div class="wrap centered-flexbox">
      <h1> Choices </h1>
      <button @click="select" :disabled="gameCompleted" value="0">🤵‍♂</button>
      <button @click="select" :disabled="gameCompleted" value="1">👰‍♀️‍️</button>
      <button @click="select" :disabled="gameCompleted" value="2">💒</button>
      <button @click="select" :disabled="gameCompleted" value="3">🔔</button>
      <button @click="select" :disabled="gameCompleted" value="4">💐</button>
      <button @click="select" :disabled="gameCompleted" value="5">❤️</button>
      <button @click="select" :disabled="gameCompleted" value="6">🥰</button>
      <button @click="select" :disabled="gameCompleted" value="7">🎊</button>
    </div>

    <button @click="submit" :disabled="gameCompleted" class="submit"> Submit</button>
    <div>
      <button @click="undo" :disabled="gameCompleted"> Undo</button>
    </div>
  </div>
</template>

<style>
button {
  font-size: 2rem;
}

.wrap,
.action-buttons {
  margin-left: 25px;
  flex-direction: column;
}

.submit {
  margin-top: 10px;
  margin-bottom: 10px;
}
</style>

