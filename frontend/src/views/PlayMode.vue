<script >
  import ActionButtons from '@/components/ActionButtons.vue'
  import Gameboard from '@/components/Gameboard.vue'
  // import Hint from '@/components/GuessRow.vue'
  export default {
    components: {
      "ActionButtons": ActionButtons,
      "Gameboard": Gameboard
    },
    mounted() {
      this.$store.play()

  },
  }
</script>



<template>
<!--  {{this.$store.play}}-->
  <ActionButtons/>
  <Gameboard/>

<!--  <Hint/> -->


</template>

<style>

</style>