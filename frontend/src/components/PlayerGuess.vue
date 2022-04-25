<script>
  import GuessRow from '@/components/GuessRow.vue'
  export default {
    components: {
      'GuessRow': GuessRow
    },
    mounted() {
      console.log(GuessRow)
    },
    data() {
      return {
        max_attempt_allowed: 10,
      }
    }
  }
</script>


<template>
  <div>
    <h1> Player Guess </h1>
<!--    <p>{{$store.counter}}</p>-->
<!--    Index looping starts at 1 (convert to start at 0)-->
    <div v-for="index in max_attempt_allowed" :key="index" class="playerguess">
      <GuessRow :row="index - 1" />
    </div>

  </div>

</template>

<style>
  button {
    font-size: 5rem
  }

  .line {
    color: darkgrey;

  }

  .hint {
    font-size: 1rem
  }
</style>