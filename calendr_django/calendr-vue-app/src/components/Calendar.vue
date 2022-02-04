<template>
  <div>
    <h1>Calendr</h1>
    <a href="">Logout</a>
    <div>
      <VCalendar class="events-calendar" is-expanded :attributes="attributes">
        <template v-slot:day-content="{ day, attributes }">
          <span>{{ day.day }}</span>
          <div>
            <p :key="attr.key" v-for="attr in attributes" class="event">
              {{ attr.customData.title }}
            </p>
          </div>
        </template>
      </VCalendar>
    </div>
    <div class="form-container">
      <form>
        <input type="text" placeholder="event name" />
        <input type="text" placeholder="description" />
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
import { GetUser } from "../services/endpoints";
import axios from "axios";

export default {
  name: "Calendar",
  components: {
    DatePicker,
    VCalendar,
  },
  data() {
    return {
      user: {},
      date: new Date(),
      attributes: [],
    };
  },
  mounted() {
    this.getEvents();
  },
  methods: {
    handleClick() {
      console.log(this.date.toISOString().slice(0, 10));
    },
    async getEvents() {
      let res = await GetUser(this.$route.params.id);
      this.user = res;
      // console.log(this.user.events)
      for (let i = 0; i < this.user.events.length; i++) {
        let res = await axios.get(this.user.events[i]);
        // this.userEvents.push(res.data);
        let year = parseInt(res.data.date.slice(0, 4))
        let month = parseInt(res.data.date.slice(5, 7))
        let day = parseInt(res.data.date.slice(8, 10))
        this.attributes.push({key: [i]+1, customData: { title: res.data.title}, dates: new Date(year, month-1, day)})
      }
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
  width: 40%;
}
form {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2em;
  padding: 2em;
}
input,
button {
  width: 60%;
}
</style>
