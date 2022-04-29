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
    }
  }
</script>

<template>
  <main>
    <h1> Mastermind Game </h1>
    <nav>
            <RouterLink :to="gamesLink">Play</RouterLink>
            <RouterLink v-if="!this.loggedIn" to="/register">Register</RouterLink>
            <RouterLink v-if="!this.loggedIn" to="/login">Login</RouterLink>
            <RouterLink v-if="this.loggedIn" to="/logout">Logout</RouterLink>

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
</style>