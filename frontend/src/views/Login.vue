<script>
export default {
  data() {
    return {
      player: {
        email_address: "reach@linkedin.com",
        password: "reach",
      }
    }
  },
  methods: {
    submit() {
      this.$store.login(this.player)
    }
  }
}


</script>

<template>
  <div class=input-wrapper>
    <h1> Welcome Back! </h1>
    <h3> For demo: Please use given login info below to login. </h3>
    <label>Email Address</label>
    <input type="email" class="register-form" placeholder="Email Address" v-model="player.email_address" required
           data-validation-required-message="Please enter your email address.">
    <label>Password</label>
    <input type="password" class="register-form" placeholder="Password" v-model="player.password" required
           data-validation-required-message="Please enter your password.">
    <br>
    <button type="submit" class="send-button" @click="submit">Login</button>
  </div>

</template>

<style scoped>
h1 {
  font-weight: bold;
  font-size: 2.75rem;
  top: -10px;
  padding-top: 3rem;
  padding-bottom: 5rem;
}

h3 {
  font-style: italic;
  padding-bottom: 1rem;
  font-weight: normal;
}

label {
  font-size: 1.25rem;
}

input {
  font-family: sans-serif;
  font-size: 20px;
  width: 100%;
  background: none;
  color: black;
  border: 1px solid royalblue;
  border-radius: 5px;
  padding: 10px

}

.input-wrapper {
  margin: 2rem;
  font-size: 1rem;
}

.send-button {
  color: white;
  background-color: royalblue;
  border: none;
  border-radius: 5px;
  padding: 10px 40px;
  font-size: 2rem;
  cursor: pointer;
}

.send-button:disabled {
  opacity: 0.5;
}

.register-form {
  margin-top: 5px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 1rem;
  margin-bottom: 1rem;
}

</style>