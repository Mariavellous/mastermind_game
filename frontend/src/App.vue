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
    mounted() {
      this.$store.autoLogin()
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
    },
    methods: {
      logout() {
        this.$store.logout()
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
            <div v-if="this.loggedIn" class="greeting">  Hi, {{this.$store.currentPlayer.first_name}} </div>

            <RouterLink :to="gamesLink" class="navigation" >Play</RouterLink>
            <RouterLink v-if="!this.loggedIn" to="/register" class="navigation" >Register</RouterLink>
            <RouterLink v-if="!this.loggedIn" to="/login" class="navigation" >Login</RouterLink>
            <RouterLink @click="logout" v-if="this.loggedIn" to="/" class="navigation" >Logout</RouterLink>
          </nav>
        </div>

      </div>

    </div>
    <div class="content centered-flexbox">
      <router-view/>
      <div id="modals"></div>
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
    position: relative;
    width: 100%;
    overflow: scroll;
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


  .vue-universal-modal {
    display: flex;
    justify-content: center;
    align-items: center;
    overscroll-behavior: contain;
    overflow-y: auto;
    width: 100%;
    height: 100%;
    left: 0;
    top: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, .8);
    text-align: left;
    position:absolute;
  }

  .modal {
    width: 300px;
    padding: 30px;
    box-sizing: border-box;
    background-color: #fff;
    font-size: 20px;
    text-align: center;
    border-radius: 10px;
  }

  .greeting{
    margin-right: 15px;
  }

</style>
