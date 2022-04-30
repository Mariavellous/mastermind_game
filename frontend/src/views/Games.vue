<script>
  import router from "../router";

  export default {
    name: "Games.vue",
    mounted() {
      this.$store.getGames()
    },
    methods: {
      async select(gameId) {
        this.$store.gameId = gameId
        await router.push({ path: `/games/${gameId}` })
      },
      async startGame() {
        await this.$store.newGame()
      }
    }
  }

</script>

<template>

    <main>
    <h1> Mastermind Game </h1>
    <h5 class="emoji-title">🤵‍♂️👰‍♀💒🔔💐❤️🫶🎊️</h5>

    <nav>
<!--      will route to new game -->
<ul @click="startGame" class="play-game"> New Game </ul>
    </nav>
      <!--      if list of games exist, display it here -->
      <ul class="">
        <li
            v-for="game in this.$store.gamesList"
            :key="game"
            class="game-link"
            @click="select(game.id)"
        >
          Game:{{ game.id }} Played On:{{ new Date(game.played_on).toDateString() }}
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
    margin-bottom: 10px;
    padding: 5px;
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
</style>