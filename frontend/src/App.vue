<script>
  import {RouterLink, RouterView} from 'vue-router'
  import Register from '@/views/Register.vue'
  import GetGame from '@/components/GetGame.vue'
  // import PlayMode from '@/views/PlayMode.vue'
  export default {
    components: {
      'Register': Register,
      'RouterView': RouterView,
      'RouterLink': RouterLink
    },

    computed: {
      loggedIn() {
        if (this.$store.currentPlayer.email_address !== null) {
          return true
        }
        return false
      },
      gamesLink(){
        if(this.loggedIn) {
          return "/games"
        } else {
          return "/login"
        }
      }
    }
  }
</script>

<template>

  <main class="centered-flexbox">
    <div class="header centered-flexbox">
      <div class="wrapper centered-flexbox">
        <div class="left">
            <div class="navigation"> <RouterLink to="/">Home</RouterLink> </div>
        </div>
        <div class="space"></div>
        <div class="right">
          <nav>
            <RouterLink :to="gamesLink" class="navigation" >Play</RouterLink>
            <RouterLink v-if="!this.loggedIn" to="/register" class="navigation" >Register</RouterLink>
            <RouterLink v-if="!this.loggedIn" to="/login" class="navigation" >Login</RouterLink>
            <RouterLink v-if="this.loggedIn" to="/logout" class="navigation" >Logout</RouterLink>
          </nav>
        </div>
      </div>
    </div>
    <div class="content centered-flexbox">
      <router-view/>
    </div>
    <div class="footer centered-flexbox"> @Made with Love 👰‍♀️ </div>
  </main>
</template>

<style>
  /*@import '@/assets/base.css';*/
  * {
    margin: 0;
  }

  a {
     text-decoration: none; /* no underline */
  }

  #app {
    height: 100%;
  }

  html {
    height: 100%
  }

  body {
    font-family: sans-serif;
    height: 100%
  }

  .centered-flexbox {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  main {
    flex-direction: column;
    height: 100%;
  }

  .header {
    width: 100%;
    height: 50px;
    background-color: #f2f2f2;
  }

  .header > .wrapper {
    width: 900px;
  }

  .header .left {
    margin-left: 30px;
  }

  .header .right {
    margin-right: 30px;
  }

  .header .space {
    flex-grow: 1;
  }

  .content {
    flex-grow: 1;
  }

  .footer {
    height: 50px;
    width: 100%;
    background-color: #f2f2f2;
  }

  nav {
    display: flex;
  }
  nav .navigation {
    margin-left: 3px;
    margin-right: 3px;
  }

</style>
