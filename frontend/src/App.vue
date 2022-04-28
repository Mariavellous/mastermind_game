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
    }
  }
</script>

<template>

  <main class="centered-flexbox">
    <div class="header centered-flexbox">
      <div class="wrapper centered-flexbox">
        <div class="left">left</div>
        <div class="space"></div>
        <div class="right">
          <nav>
            <RouterLink to="/">Home</RouterLink>
            <RouterLink to="/games">Play</RouterLink>
            <RouterLink to="/register">Register</RouterLink>
          </nav>
        </div>
      </div>
    </div>
    <div class="content centered-flexbox">
      <router-view/>
    </div>
    <div class="footer centered-flexbox"> End</div>
  </main>
</template>

<style>
  /*@import '@/assets/base.css';*/
  * {
    margin: 0;
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
    background-color: darkgrey;
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
    background-color: darkgrey;
  }

</style>
