<script setup>
defineProps({
  msg: {
    type: String,
    required: true
  }
})
</script>

<template>
  <body>
  <div class="container">
    <div class="row">
        <p> Are you a foodie? Join us here. </p>
            <form action="{{ url_for('register') }}" method="post" name="sentMessage" id="contactForm" novalidate>
              <label>Name</label>
              <input type="text" class="form-control" placeholder="Name" name="name" id="name" required data-validation-required-message="Please enter your name.">
              <p class="help-block text-danger"></p>
              <label>Email Address</label>
              <input type="email" class="form-control" placeholder="Email Address" name="email" id="email" required data-validation-required-message="Please enter your email address.">
              <label>Password</label>
              <input type="tel" class="form-control" placeholder="Password" name="password" id="password" required data-validation-required-message="Please enter your password.">
              <p class="help-block text-danger"></p>
          <br>
          <button type="submit" class="btn btn-primary" id="sendMessageButton">Submit</button>
          </form>
      </div>
    </div>
  </body>

</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}

</style>
