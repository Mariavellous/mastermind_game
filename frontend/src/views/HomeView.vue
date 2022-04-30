<script>
  export default {
    computed: {
      loggedIn() {
        if (this.$store.currentPlayer.email_address !== null) {
          return true
        }
        return false
      },
      gamesLink() {
        if (this.loggedIn) {
          return "/games"
        } else {
          return "/login"
        }
      }
    },
    methods: {
      logout() {
        this.$store.logout()
      }
    }
  }
</script>

<template>
  <main>
    <h1> Mastermind Game </h1>
    <h5 class="emoji-title">🤵‍♂️👰‍♀💒🔔💐❤️🫶🎊️</h5>
    <nav>
            <RouterLink :to="gamesLink" class="play">Play</RouterLink>
            <RouterLink v-if="!this.loggedIn" to="/login">Login</RouterLink>
            <RouterLink v-if="!this.loggedIn" to="/register">Register</RouterLink>
            <div v-if="this.loggedIn" @click="logout" class="logout">Logout</div>

    </nav>

  </main>
</template>

<style scoped>
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

  .logout {
    padding: 5px 10px;
    cursor: pointer;
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