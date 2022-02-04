<template>
  <div id="app">
    <router-view header=""></router-view>
    <!--example: <router-link to='/' name="home">Home</router-link> -->
    <header>
      <button @click="clearUser">Logout</button>
    </header>
    <Home 
      v-if="!user"
      @handleSignup="handleSignup"
      @handleLogin="handleLogin"
      :signin="signin"
      :login="login"
      :user="user"
      @fieldChange="fieldChange"
    />
    <Calendar v-else :user="user" />
  </div>
</template>

<script>
import Calendar from './components/Calendar.vue'
import Home from './components/Home.vue'
import {CreateUser, FindUsername} from './services/endpoints'
export default {
  name: 'App',
  data:()=>({
    signin: '',
    login: '',
    user: JSON.parse(localStorage.getItem('user')) || null,
  }),
  components: {
    Home,
    Calendar
  },
  methods: {
    fieldChange(name, value){
      this[name] = value
    },

    async handleSignup() {

      console.log(this.signin)
        console.log(`${this.signin} signed up`)
        const user = await CreateUser(this.signin)
        localStorage.setItem('user', JSON.stringify(user))

    },
    async handleLogin() {
      console.log(this.login)
        const user = await FindUsername(this.login)
        localStorage.setItem('user', JSON.stringify(user))
        this.user = user
        console.log(user)
        console.log(`${this.login} logged in`)
    },
    clearUser() {
        localStorage.clear()
        this.user = null
        // this.username = ''
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
