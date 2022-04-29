<script>
</script>

<template>
  <main>
    <h1> Mastermind Game </h1>
    <nav>
      <RouterLink to="/games">Play</RouterLink>
      <RouterLink to="/register">Register</RouterLink>
      <RouterLink to="/login">Login</RouterLink>

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