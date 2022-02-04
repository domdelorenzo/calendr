<template>
	<div class="Calendar">
		<h1 class="calendar-h1">
			Calendr <button @click="logout" class="logout-btn">Logout</button>
		</h1>

		<div class="form-container">
			<div class="calendar-div" v-on:click="handleClick">
				<DatePicker is-expanded v-model="date" class="date-picker" />
			</div>

			<form @submit="submitEvent" class="input-form-div">
				<h2 class="calendar-event-h2">Add an event!</h2>
				<div class="input-form-container">
					<input
						type="text"
						placeholder="Event Title"
						:value="newEvent.title"
						@input="handleChange"
						class="title-input"
					/>
				</div>

				<div class="input-form-container">
					<input
						type="text"
						placeholder="Event Description"
						:value="newEvent.description"
						@input="handleChange"
						class="title-input"
					/>

					<br /><br />

					<button type="submit" class="create-event-btn">Create Event</button>
				</div>
			</form>
		</div>

		<div class="events-calendar-container">
			<VCalendar class="events-calendar" is-expanded :attributes="attributes">
				<template v-slot:day-content="{ day, attributes }">
					<span class="calendar-days">{{ day.day }}</span>
					<div>
						<p :key="attr.key" v-for="attr in attributes" class="event">
							{{ attr.customData.title }}

							<button
								v-on:click.prevent="deleteEvent(attr.customData.id)"
								class="delete-btn"
							>
								<span class="trash-icon">🗑</span>
							</button>
						</p>
					</div>
				</template>
			</VCalendar>
		</div>
	</div>
</template>

<script>
import DatePicker from 'v-calendar/lib/components/date-picker.umd';
import VCalendar from 'v-calendar/lib/components/calendar.umd';
import { GetUser, PostEvent, DeleteEvent } from '../services/endpoints';
import axios from 'axios';
export default {
	name: 'Calendar',
	components: {
		DatePicker,
		VCalendar,
	},
	data() {
		return {
			userData: {},
			date: new Date(),
			attributes: [],
			user: JSON.parse(localStorage.getItem('user')) || null,
			newEvent: {
				user_id: null,
				date: '',
				description: '',
				title: '',
			},
		};
	},
	mounted() {
		this.getEvents();
	},
	methods: {
		async getEvents() {
			let res = await GetUser(parseInt(this.user.id));
			this.userData = res;
			for (let i = 0; i < this.userData.events.length; i++) {
				let res = await axios.get(this.userData.events[i]);
				let year = parseInt(res.data.date.slice(0, 4));
				let month = parseInt(res.data.date.slice(5, 7));
				let day = parseInt(res.data.date.slice(8, 10));
				this.attributes.push({
					key: [i] + 1,
					customData: { title: res.data.title, id: res.data.id },
					dates: new Date(year, month - 1, day),
				});
			}
		},
		handleClick() {
			this.newEvent = {
				...this.newEvent,
				date: this.date.toISOString().slice(0, 10),
			};
		},
		handleChange(e) {
			this.newEvent = {
				...this.newEvent,
				[e.target.placeholder]: e.target.value,
				date: this.date.toISOString().slice(0, 10),
			};
		},
		async submitEvent(e) {
			e.preventDefault();
			await PostEvent({ ...this.newEvent, user_id: this.user.id });
			this.getEvents();
			this.newEvent = {
				date: this.newEvent.date,
				description: '',
				title: '',
			};
		},
		logout() {
			localStorage.clear();
			this.user = null;
			this.username = '';
			this.$router.push(`/home`);
		},
		async deleteEvent(id) {
			console.log(`${id}`);
			await DeleteEvent(id);
			this.attributes = [];
			this.getEvents();
		},
	},
};
</script>

<style>
::-webkit-scrollbar {
	width: 0px;
}
::-webkit-scrollbar-track {
	display: none;
}

.Calendar {
	width: 100vw;
	text-align: center;
}

.events-calendar-container {
	display: flex;
	width: 75vw;
	margin: 0 auto;
}

.vc-day {
	/* height: 100px; */
	/* max-width: 100px; */
	border: solid 0.2px lightgray;
	/* border-right: solid 0.2px lightgray; */
	/* background-color: rgb(243, 240, 240); */
	/* border-radius: 1em; */
	/* height: 10em; */
	margin: 0.2em;
	border-radius: 0.3em;
	overflow-y: auto;
	overflow-x: auto;
	padding-top: 8px;
	text-align: center;
}

.date-picker {
	border: 0;
}

.calendar-days {
	text-align: center;
}

.event {
	text-transform: capitalize;
	background-color: rgb(199, 229, 247);
	margin: 5px 5px;
	padding: 5px;
	border-radius: 0.5em;
}

.input-form-container {
	background-color: white;
	border: solid 1px rgb(204, 204, 204);
	border-radius: 0.1em;
	height: 2em;
	width: 15em;
	margin: 0 auto 0.5em;
	text-align: center;
	/* border: solid 1px blue; */
}

.form-container {
	display: flex;
	flex-wrap: wrap;
	width: 50vw;
	margin: 0 auto;
	/* border: solid 1px red; */
	align-items: center;
}

.vc-header {
	background-color: rgb(248, 220, 183);
}

.vc-weeks {
	/* Updates the WEEKS  */
}

.input-form-div {
	margin: 0 auto;
}

.calendar-div {
	width: 50%;
	margin-top: 2em;
}

.calendar-div div {
	border: 0;
}

.title-input {
	background-color: white;
	border: 0;
	height: 1em;
	margin: 0.5em;
	width: 15em;
}

.create-event-btn {
	background-color: rgb(235, 225, 220);
	border: 0;
	border-radius: 0.2em;
	height: 2.5em;
	font-family: 'Roboto', sans-serif;
	font-weight: bold;
	transition: 0.8s;
}

.create-event-btn:hover {
	background-color: rgb(162, 230, 162);
	width: 18em;
	transition: 0.8s;
}

.delete-btn {
	background-color: rgb(235, 225, 220);
	border: 0;
	border-radius: 2.5em;
	width: 2em;
	height: 2.5em;
	margin-left: 2em;
	font-family: 'Roboto', sans-serif;
	font-weight: bold;
	transition: 0.8s;
}

.delete-btn:hover {
	background-color: rgb(224, 156, 156);
	border: 0;
	border-radius: 0.2em;
	height: 2.5em;
	font-family: 'Roboto', sans-serif;
	font-weight: bold;
	transition: 0.8s;
}

.trash-icon {
	font-size: 20px;
}

.calendar-h1 {
	background-color: rgb(235, 225, 220);
	box-shadow: 0.2em 0.2em rgb(247, 235, 235);
	font-family: Roboto;
	font-size: 4em;
	/* padding: 0 0.6em 0.1em 0.4em; */
	width: 90%;
	margin: 0 auto;
}

.calendar-event-h2 {
	font-family: Roboto;
	text-align: center;
}

.logout-btn {
	border: 0;
	border-radius: 2.5em;
	/* width: 2em; */
	/* height: 2.5em; */
	margin-left: 10em;
	font-family: 'Roboto', sans-serif;
	font-weight: bold;
	transition: 0.8s;
}

.delete-btn:hover {
	background-color: rgb(235, 225, 220);
	border: 0;
	border-radius: 0.2em;
	height: 2.5em;
	font-family: 'Roboto', sans-serif;
	font-weight: bold;
	transition: 0.8s;
}
</style>
