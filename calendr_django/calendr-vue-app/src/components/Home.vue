<template>
	<div class="home-container">
		<div class="signup-div-container">
			<h1 class="calendr-h1">Calendr .</h1>
			<!-- <h2 class="calendr-h2">Schedule and Plan your way</h2> -->
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
					</div>

					<div class="input-container">
						<input
							type="text"
							placeholder="Password"
							class="signup-input-form"
						/>
						<br /><br />
						<button type="submit" class="signup-btn">Sign up!</button>
					</div>
				</form>
			</div>
		</div>

		<!-- <div class="user-forms-right-div"></div> -->
		<!-- <div class="login-container">
				<h2>Log in</h2>
				<form v-on:submit.prevent="handleLogin" class="login-form-container">
					<input
						type="text"
						placeholder="Username"
						:value="login"
						name="login"
						v-on:input="handleChange"
						class="login-input-form"
					/>
					<button type="submit" class="login-btn">Log in</button>
				</form> -->
		<!-- </div> -->
	</div>
</template>

<script>
export default {
	name: 'Home',
	props: {
		signin: {
			type: String,
			required: true,
		},
		login: {
			type: String,
			required: true,
		},
	},
	methods: {
		handleChange(e) {
			this.$emit('fieldChange', e.target.name, e.target.value);
			// this[e.target.name] = e.target.value
		},
		handleSignup() {
			this.$emit('handleSignup');
		},
		handleLogin() {
			this.$emit('handleLogin');
		},
	},
};
</script>

<style scoped>
.home-container {
	display: flex;
	align-items: center;
	height: 100vh;
}

.signup-div-container {
	margin: 0 auto;
}

.user-forms-right-div {
	/* margin: 0 auto;
	background-color: gray; */

	/* background-image: url('https://images.unsplash.com/photo-1543168256-4ae2229821f1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=812&q=80'); */
	/* background-repeat: repeat;
	background-size: cover;
	background-position: 25% 75%;
	height: 100vh; */
}

.calendr-h1 {
	background-color: rgb(235, 225, 220);
	font-family: Roboto;
	font-size: 4em;
	padding: 0 0.6em 0.1em 0.6em;
	/* margin-left: 4em; */
	width: 45vw;
	z-index: 2;
	position: relative;
}

.calendr-h2 {
	font-family: Roboto;
	font-size: 2em;
	margin: -2.4em 0 1em 4em;
	z-index: 2;
	position: relative;
}

.signup-container {
	width: 50vw;
	height: 18vh;
	margin: -4em 0 0 2em;
	padding-top: 2em;
	background-color: white;
}

.signup-form-container {
	/* display: flex; */
	/* border: solid 1px red; */
}

.input-container {
	background-color: white;
	border: solid 1px rgb(204, 204, 204);
	border-radius: 0.2em;
	height: 2em;
	width: 15em;
	margin: 0 auto 0.5em;
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
	/* font-weight: bold; */
}

.signup-h2 {
	text-align: center;
	font-family: 'Lato', sans-serif;
	/* color: white; */
}

.input-container-btn {
	background-color: white;
	border-radius: 0.2em;
	height: 2em;
	width: 15em;
	margin: 0 auto 0.5em;
}

.signup-btn {
	background-color: rgb(235, 225, 220);
	border: 0;
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
}

.login-container {
	width: 50%;
}

.login-form-container {
	margin: 0 auto;
	border: solid 2px red;
}

.login-input-form {
	background-color: red;
}

.login-btn {
	border: 0;
}
</style>
