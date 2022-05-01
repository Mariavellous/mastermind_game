<script>
import router from "../router";

export default {
  name: "Games.vue",
  data() {
    return {
      mode: 4,
    }
  },
  mounted() {
    this.$store.getGames()
  },
  methods: {
    async select(gameId) {
      this.$store.gameId = gameId
      await router.push({path: `/games/${gameId}`})
    },
    async startGame() {
      await this.$store.newGame(this.mode)
    },
    resultEmoji(result) {
      if (result === true) {
        return "🎉"
      } else if (result === false) {
        return "😭"
      }
    }
  }
}

</script>

<template>

  <main>
    <h1> Mastermind Game </h1>
    <h5 class="emoji-title">🤵‍♂️👰‍♀💒🔔💐❤️🫶🎊️</h5>
    <div class="record">
      <div>Won: {{ this.$store.gamesWon }}&nbsp;</div>
      <div>Lost: {{ this.$store.gamesLost }}</div>
    </div>


    <!--      will route to new game -->
    <!--      Player choose difficulty level : defaults to medium (length of 4)-->
    <div class="centered-flexbox new-game-container">
      <select v-model="mode" class="select">
        <option value="3">easy</option>
        <option value="4" selected="selected">medium</option>
        <option value="5">hard</option>
      </select>
      <div @click="startGame" class="play-game"> New Game</div>
    </div>

    <!--      if list of games exist, display it here -->
    <ul class="">
      <li
          v-for="game in this.$store.gamesList"
          :key="game"
          class="game-link"
          @click="select(game.id)"
      >
        <span>Game:{{ game.id }}</span>&nbsp;
        <span>{{ new Date(game.played_on).toDateString() }}&nbsp;&nbsp;{{ resultEmoji(game.result) }}</span>

      </li>
    </ul>

  </main>
</template>


<style scoped>
.game-link {
  cursor: pointer;
  background: royalblue;
  padding: 10px 0;
  color: white;
  font-size: 2rem;
  text-align: center;
  border-radius: 10px;
  margin-bottom: 10px;
  padding: 5px;
}

.play-game {
  cursor: pointer;
  background: orange;
  padding: 10px 0;
  color: white;
  font-size: 2rem;
  text-align: center;
  border-radius: 10px;
  padding: 5px;
  flex-grow: 1;
  margin-left: 10px;
}

h1 {
  font-weight: bold;
  font-size: 2.75rem;
  top: -10px;
  padding-top: 3rem;
  padding-bottom: 5rem;
}

nav {
  font-size: 2rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin: 5rem;
}

nav a {
  padding: 5px 10px;
  width: 100%;
  background: royalblue;
  text-align: center;
  border-radius: 8px;
  color: white;
  margin-bottom: 10px;
}

a.play {
  background-color: orange;
}

h1 {
  text-align: center;
  padding-bottom: 10px;
}

.emoji-title {
  font-size: 5rem;
  text-align: center;
}

.record {
  display: flex;
  justify-content: center;
  font-size: 30px;
  font-weight: 600;
}

ul {
  padding-inline-start: 0
}

.select {
  cursor: pointer;
  background: orange;
  padding: 10px 0;
  color: white;
  font-size: 1.5rem;
  text-align: center;
  border-radius: 10px;
  margin-top: 10px;
  margin-bottom: 10px;
  padding: 5px;
}

.new-game-container {
  margin-bottom: 30px;
}
</style>