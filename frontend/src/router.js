import { createRouter, createWebHistory } from 'vue-router'
import Home from './views/Home.vue'
import About from './views/About.vue'
import CarInput from './views/CarInput.vue'

const routes = [
  {
    name: 'Home',
    path: '/',
    component: Home
  },
  {
    name: 'About',
    path: '/about',
    component: About
  },
  {
    name: 'CarInput',
    path: '/add-car',
    component: CarInput
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router