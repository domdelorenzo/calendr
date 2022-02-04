<template>
	<div id="app">
		<router-view header=""></router-view>
		<!-- example: <router-link to="/" name="home">Home</router-link> -->

	</div>
</template>

<script>
// import Calendar from './components/Calendar.vue';
// import Home from './components/Home.vue';
export default {
	name: 'App',

	methods: {

	},
};
</script>

<style>
body {
	margin: 0;
	background-image: url('https://images.unsplash.com/photo-1543168256-4ae2229821f1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=812&q=80');
	background-repeat: repeat;
	background-size: cover;
	background-position: 25% 25%;
	margin: 0;
	height: 100vh;
	width: 100vw;
}

/* 
#app {
	font-family: Avenir, Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
	margin-top: 60px;
} */
</style>
