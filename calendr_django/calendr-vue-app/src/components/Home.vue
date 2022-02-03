<template>
    <div>
        <h1>Calendr</h1>
        <div class="user-forms">
            <div class="signup">
                <h2>Sign up</h2>
                <form v-on:submit.prevent='handleSignup'>
                    <input 
                        type="text" 
                        placeholder="Username"
                        :value="signin"
                        name="signin"
                        v-on:input='handleChange'
                    />
                    <button type="submit">Sign Up</button>
                </form>
            </div>
            <div class="login">
                <h2>Log in</h2>
                <form v-on:submit.prevent='handleLogin'>
                    <input 
                        type="text" 
                        placeholder="Username"
                        :value="login"
                        name="login"
                        v-on:input='handleChange'
                    />
                    <button type="submit">Log in</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import {CreateUser} from '../services/endpoints'
export default {
    name: 'Home',
    data: () => ({
        signin: '',
        login: '',
        // user: JSON.parse(localStorage.getItem('user')) || null,
    }),
    methods: {
        handleChange(e) {
            this[e.target.name] = e.target.value
        },
        async handleSignup() {
            console.log(`${this.signin} signed up`)
            const user = await CreateUser(this.signin)
            this.user = user
        },
        handleLogin() {
            console.log(`${this.login} logged in`)
        },
        // async submitUsername(){
        //     const user = await CreateUser(this.signin)
        //     // localStorage.setItem('user', JSON.stringify(user))
        
        //     this.user = user
        //     // this.$socket.emit('userConnected', { username: user.username })

        // }
    }
}
</script>

<style scoped>
    .user-forms {
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        height: 300px;
    }
    form {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    form input, form button {
        margin: 1em auto;
    }
    .signup, .login {
        width: 50%;
    }
    .signup {
        border-right: 1px solid black;
        margin-left: 10%;
    }
    .login {
        border-left: 1px solid black;
        margin-right: 10%;
    }
</style>