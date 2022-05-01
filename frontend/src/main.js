import {createApp} from 'vue'
import {createPinia} from 'pinia'

import App from './App.vue'
import router from './router'
import {useGameStore} from './stores/gamestore'

import VueUniversalModal from 'vue-universal-modal'

const app = createApp(App)
app.use(VueUniversalModal, {
  teleportTarget: '#modals'
})
app.use(createPinia())
app.use(router)

app.config.globalProperties.$store = useGameStore();
app.config.globalProperties.$router = router
app.config.devtools = true

app.mount('#app')
