import {createRouter, createWebHashHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Register from '../views/Register.vue'
import Games from '../views/Games.vue'
import Login from '../views/Login.vue'
import PlayMode from '../views/PlayMode.vue'

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/games',
      name: 'games',
      component: Games
    },
    {
      path: '/login',
      name: 'name',
      component: Login
    },
    {
      path: '/games/:id',
      name: 'gameid',
      component: PlayMode
    },
  ]
})

export default router
