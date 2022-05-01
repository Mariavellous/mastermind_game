<script>
import GuessRow from '@/components/GuessRow.vue'

export default {
  components: {
    'GuessRow': GuessRow
  },
  mounted() {
    console.log(GuessRow)
  },
  computed: {
    attemptsLeft() {
      return this.$store.max_attempts_allowed - this.$store.number_of_attempts
    }
  }
}
</script>


<template>
  <div class="gameboard">
    <h1> Player Guess </h1>
    <!--    <p>{{$store.counter}}</p>-->
    <!--    Index looping starts at 1 (convert to start at 0)-->
    <div v-for="index in this.$store.max_attempts_allowed" :key="index" class="playerguess">
      <GuessRow :index="index - 1"/>
    </div>
    <h1> Remaining Guess Allowed:{{ this.attemptsLeft }} </h1>
  </div>

</template>

<style scoped>

.gameboard {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

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