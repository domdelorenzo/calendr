<template>
  <div>
    <h1>Calendr</h1>
    <a @click="logout" href="">Logout</a>
    <div>
      <VCalendar class="events-calendar" is-expanded :attributes="attributes">
        <template v-slot:day-content="{ day, attributes }">
          <span>{{ day.day }}</span>
          <div>
            <p :key="attr.key" v-for="attr in attributes" class="event">
              {{ attr.customData.title }} 
              <button v-on:click.prevent='deleteEvent(attr.customData.id)'>
                Delete
              </button>
            </p>
          </div>
        </template>
      </VCalendar>
    </div>
    <div class="form-container">
      <form @submit="submitEvent">
        <input type="text" placeholder="title" :value="newEvent.title" @input="handleChange" />
        <input type="text" placeholder="description" :value="newEvent.description" @input="handleChange" />
        <button type="submit">Create Event</button>
      </form>
      <div class="calendar-div" v-on:click="handleClick">
        <DatePicker is-expanded v-model="date" />
      </div>
    </div>
  </div>
</template>

<script>
import DatePicker from "v-calendar/lib/components/date-picker.umd";
import VCalendar from "v-calendar/lib/components/calendar.umd";
import { GetUser, PostEvent, DeleteEvent } from "../services/endpoints";
import axios from "axios";

export default {
  name: "Calendar",
  components: {
    DatePicker,
    VCalendar,
  },
  data() {
    return {
      userData: {},
      date: new Date(),
      attributes: [],
      user: JSON.parse(localStorage.getItem("user")) || null,
      newEvent: {
        user_id: null,
        date: '',
        description: '',
        title: ''
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
        date: this.date.toISOString().slice(0, 10) };
    },
    handleChange(e) {
      this.newEvent = { 
        ...this.newEvent, 
        [e.target.placeholder]: e.target.value, 
        date: this.date.toISOString().slice(0, 10) };
    },
    async submitEvent(e) {
      e.preventDefault();
			await PostEvent({...this.newEvent, user_id: this.user.id})
			this.getEvents()
      this.newEvent = {
        date: this.newEvent.date,
        description: '',
        title: ''
      }
    },
    logout() {
      localStorage.clear();
      this.user = null;
      this.username = "";
      this.$router.push(`/home`);
    },
    async deleteEvent(id) {
      console.log(`${id}`);
      await DeleteEvent(id);
      this.attributes = []
      this.getEvents()
    }
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

/* a {
	position: absolute;
	top: 10%;
	right: 10%;
} */
.form-container {
  display: flex;
  justify-content: space-around;
}

/* .calendar-div {
  width: 40%;
}

form {
  display: flex;
	flex-direction: column;
	align-items: center;
	gap: 2em;
	padding: 2em;
} */
input,
button {
  width: 60%;
}
</style>
