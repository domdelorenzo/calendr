import VueRouter from 'vue-router'

import Home from './components/Home.vue'
import Calendar from './components/Calendar.vue'


const routes = [
  { path: '/home', component: Home, name: 'Home' },
  { path: '/calendar/:id', component: Calendar, name: 'Calendar' }
]

export default new VueRouter({
  routes,
  mode: 'history'
})