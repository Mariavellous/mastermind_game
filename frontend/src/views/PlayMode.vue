<script>
import ActionButtons from '@/components/ActionButtons.vue'
import Gameboard from '@/components/Gameboard.vue'
// import Hint from '@/components/GuessRow.vue'
export default {
  data() {
    return {
      isShow: false,
    }
  },
  components: {
    "ActionButtons": ActionButtons,
    "Gameboard": Gameboard
  },
  mounted() {
    this.$store.gameId = this.$router.currentRoute.value.params.id
    this.$store.play()
  },
  computed: {
    // server only sends this when game is over
    secretCode() {
      return this.$store.secretCode.split('').map(number => {
        return this.$store.themes.wedding[number]
      }).join('')
    }
  },
  // Game ended if $store.result is either true or false.
  watch: {
    '$store.result'() {
      if (this.$store.result !== null) {
        this.isShow = true
      }
    },
  }
}
</script>


<template>
  <div class="playmode">
    <!--show player if they won or not-->
    <Modal v-model="isShow">
      <div class="modal">
        <p v-if="this.$store.result === true">🎉 You won!</p>
        <p v-if="this.$store.result === false">😭 You Lost</p>
        <p>Secret Code was {{ this.secretCode }}</p>
      </div>
    </Modal>

    <Gameboard class="top"/>
    <ActionButtons class="top"/>

  </div>
</template>

<style scoped>

.playmode {
  display: flex;
  align-items: flex-start;
}
</style>