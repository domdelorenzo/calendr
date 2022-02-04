<template>
  <div>
    <h1>Calendr</h1>
    <a href="">Logout</a>
    <div>
      <VCalendar class="events-calendar" is-expanded :attributes="attributes">
        <template v-slot:day-content="{ day, attributes }">
          <span>{{ day.day }}</span>
          <div>
            <p :key="attr.key" v-for="attr in attributes" class="event" @click="testClick(attr)">
              {{ attr.customData.title }}
            </p>
          </div>
        </template>
      </VCalendar>
    </div>
    <div class="form-container">
      <form @submit="submitEvent">
        <input type="text" placeholder="title" @input="handleChange" />
        <input type="text" placeholder="description" @input="handleChange" />
        <button type="submit">Create Event</button>
      </form>
      <div class="calendar-div" v-on:click="handleClick">
        <DatePicker is-expanded v-model="date" />
      </div>
    </div>
  </div>
</template>

<script>
import DatePicker from 'v-calendar/lib/components/date-picker.umd';
import VCalendar from 'v-calendar/lib/components/calendar.umd';
import { GetUser } from '../services/endpoints';
import axios from 'axios';

export default {
  name: "Calendar",
  components: {
    DatePicker,
    VCalendar,
  },
  props: {
    user: null,
  },
  data() {
    return {
      userdata: {},
      date: "",
      attributes: [],
      newEvent: {
        user_id: this.user.id,
      },
    };
  },
  mounted() {
    this.getEvents();
  },
  methods: {
    handleClick() {
      this.newEvent = { ...this.newEvent, date: this.date.toISOString().slice(0, 10) };
    },
    async getEvents() {
      let res = await GetUser(this.user.id);
      this.userData = res;
      for (let i = 0; i < this.user.events.length; i++) {
        let res = await axios.get(this.user.events[i]);
        let year = parseInt(res.data.date.slice(0, 4));
        let month = parseInt(res.data.date.slice(5, 7));
        let day = parseInt(res.data.date.slice(8, 10));
        this.attributes.push({ key: [i] + 1, customData: { title: res.data.title }, dates: new Date(year, month - 1, day), userData: res });
      }
    },
    testClick(e) {
      console.log(e);
    },
    handleChange(e) {
      this.newEvent = { ...this.newEvent, [e.target.placeholder]: e.target.value, date: this.date };
    },
    submitEvent(e) {
      e.preventDefault();
      console.log(this.newEvent);
    },
  },
};
</script>

<style scoped>
::-webkit-scrollbar {
	width: 0px;
}
::-webkit-scrollbar-track {
	display: none;
}
.events-calendar {
	max-width: 95%;
}
.vc-day {
	height: 100px;
	/* max-width: 100px; */
	overflow-y: auto;
	overflow-x: auto;
	border: 0.5px solid lightgray;
	padding-top: 8px;
}
.event {
	border: 0.2px solid lightgray;
	background-color: rgb(199, 229, 247);
	margin: 5px 5px;
	padding: 5px;
}
.vc-header {
	background-color: rgb(199, 229, 247);
}

a {
	position: absolute;
	top: 10%;
	right: 10%;
}
.form-container {
	display: flex;
	justify-content: space-around;
}
form,
.calendar-div {
	/* width: 40%; */
}
form {
	/* display: flex;
	flex-direction: column;
	align-items: center;
	gap: 2em;
	padding: 2em; */
}
input,
button {
	width: 60%;
}
</style>
