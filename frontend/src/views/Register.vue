<script>
  export default {
    data() {
      return {
        newPlayer: {
          first_name: "",
          last_name: "",
          email_address: "",
          password: "",
        }
      }
    },
    methods: {
      submit() {
        this.$store.register(this.newPlayer)
      }
    }
  }


</script>

<template>
  <div class=input-wrapper>
    <form>
    <h1> Ready to be a code master? Join here! </h1>
    <label>First Name</label>
    <input type="text" class=register-form v-model="newPlayer.first_name" placeholder="First Name" required
           data-validation-required-message="Please enter your first name.">
    <label>Last Name</label>
    <input type="text" class=register-form v-model="newPlayer.last_name" placeholder="Last Name" required
           data-validation-required-message="Please enter your last name.">
    <label>Email Address</label>

    <input type="email" class="register-form" placeholder="Email Address" v-model="newPlayer.email_address" required
           data-validation-required-message="Please enter your email address.">
i
    <label>Password</label>
    <input type="password" class="register-form" placeholder="Password" v-model="newPlayer.password" required
           data-validation-required-message="Please enter your password.">
    <br>
    <button type="submit" class="send-button" @click="submit">Register</button>
    </form>
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

  label {
    font-size: 1.25rem;
  }

  input {
    font-family: sans-serif;
    font-size: 20px;
    width: 50%;
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
