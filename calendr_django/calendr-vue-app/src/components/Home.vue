<template>
	<div class="home-container">
		<div class="signup-div-container">
			<h1 class="calendr-h1">Calendr .</h1>
			<div class="signup-container">
				<h2 class="signup-h2">Create an account and start planning!</h2>
				<form v-on:submit.prevent="handleSignup" class="signup-form-container">
					<div class="input-container">
						<input
							type="text"
							placeholder="Username"
							:value="signin"
							name="signin"
							v-on:input="handleChange"
							class="signup-input-form"
						/>
						<br />

						<button type="submit" class="signup-btn">Sign up!</button>
					</div>
				</form>

				<h2 class="calendr-h2-login">Please login</h2>
				<form v-on:submit.prevent="handleLogin" class="login-form-container">
					<div class="input-container">
						<input
							type="text"
							placeholder="Username"
							:value="login"
							name="login"
							v-on:input="handleChange"
							class="signup-input-form"
						/>

						<button type="submit" class="signup-btn">Log in</button>
					</div>
				</form>
			</div>
		</div>
	</div>
</template>

<script>
import { CreateUser, FindUsername } from '../services/endpoints';

export default {
	name: 'Home',
	data: () => ({
		signin: '',
		login: '',
		user: JSON.parse(localStorage.getItem('user')) || null,
	}),

	methods: {
		handleChange(e) {
			// this.$emit('fieldChange', e.target.name, e.target.value);
			this[e.target.name] = e.target.value;
		},
		async handleSignup() {
			const user = await CreateUser(this.signin);
			localStorage.setItem('user', JSON.stringify(user.id));
			this.signin = '';
		},
		async handleLogin() {
			const user = await FindUsername(this.login);
			console.log(user);
			localStorage.setItem('user', JSON.stringify(user));
			this.user = user;
			this.$router.push(`/calendar`);
		},
	},
};
</script>

<style scoped>
.home-container {
	display: flex;
	justify-content: center;
	align-items: center;
	height: 100vh;
	margin: 0 auto;
	background-image: url('https://images.unsplash.com/photo-1543168256-4ae2229821f1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=812&q=80');
	background-size: cover;
	background-position: 25% 25%;
}

.signup-div-container {
}

.calendr-h1 {
	background-color: rgb(235, 225, 220);
	box-shadow: 0.2em 0.2em rgb(247, 235, 235);
	font-family: Roboto;
	font-size: 4em;
	padding: 0 0.6em 0.1em 0.4em;
	width: 45vw;
	z-index: 2;
	position: relative;
}
/*
.calendr-h2 {
	font-family: Roboto;
	font-size: 2em;
	margin: -2.4em 0 1em 4em;
	z-index: 2;
	position: relative;
} */

.signup-form-container {
	margin: 0 auto;
}

.signup-container {
	/* width: 50vw; */
	height: 350px;
	margin: -4em 0 0 2em;
	padding-top: 2em;
	background-color: white;
}

.input-container {
	background-color: white;
	border: solid 1px rgb(204, 204, 204);
	border-radius: 0.2em;
	height: 2em;
	width: 15em;
	/* margin: 0 auto 0.5em; */
	margin: 0 auto;
	text-align: center;
}

.signup-input-form {
	background-color: white;
	border: 0;
	height: 1em;
	margin: 0.5em;
	width: 15em;
}

.signup-input-form::placeholder {
	font-family: 'Roboto', sans-serif;
}

.signup-h2 {
	text-align: center;
	font-family: 'Lato', sans-serif;
}

/* 
.input-container-btn {
	background-color: white;
	border-radius: 0.2em;
	height: 2em;
	width: 15em;
	margin: 0 auto 0.5em;
} */

.signup-btn {
	background-color: rgb(235, 225, 220);
	width: 12em;
	border: 0;
	margin-top: 0.7em;
	border-radius: 0.2em;
	height: 2.5em;
	font-family: 'Roboto', sans-serif;
	font-weight: bold;
	transition: 0.8s;
}

.signup-btn:hover {
	background-color: rgb(162, 230, 162);
	width: 18em;
	transition: 0.8s;
	/* margin:1em; */
}
.login-div-container {
	margin: 0 auto;
}

.login-container {
	/* height: 20vh; */
	width: 50vw;
	margin: -2em 2em 0 3em;
	background-color: white;
}

.calendr-h1-login {
	background-color: rgb(235, 225, 220);
	box-shadow: 0.2em 0.2em rgb(247, 235, 235);
	font-family: Roboto;
	font-size: 4em;
	padding: 0 0.6em 0.1em 0.4em;
	width: 45vw;
}

.calendr-h2-login {
	margin-top: 2em;
	font-family: Roboto;
	/* font-size: 2em; */
	text-align: center;
	/* padding: 1em 0 0 0; */
}
</style>
