<template>
  <div>
    <h1>Calendr</h1>
    <a href="">Logout</a>
    <div>
      <VCalendar class="events-calendar" is-expanded :attributes='attributes'>
        <template v-slot:day-content='{ day, attributes }'>
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
        <input type='text' placeholder='description' />
        <button type="submit">Create Event</button>
      </form>
      <div class="calendar-div" v-on:click='handleClick'>
        <DatePicker is-expanded v-model="date" />
      </div>
    </div>
  </div>
</template>

<script>
import DatePicker from "v-calendar/lib/components/date-picker.umd";
import VCalendar from 'v-calendar/lib/components/calendar.umd';

export default {
  name: "Calendar",
  components: {
    DatePicker,
    VCalendar
  },
  data() {
    return {
      date: new Date(),
      attributes: [
        {
          key: 1,
          customData: {
            title: 'test1'
          },
          dates: new Date(2022, 1, 1)
        },
        {
          key: 2,
          customData: {
            title: 'test2'
          },
          dates: new Date(2022, 1, 5)
        },
        {
          key: 3,
          customData: {
            title: 'test3'
          },
          dates: new Date(2022, 1, 20)
        },
        {
          key: 4,
          customData: { title: 'test4' },
          dates: new Date(2022, 1, 1)
        },
        {
          key: 5,
          customData: { title: 'test5' },
          dates: new Date(2022, 1, 1)
        },
        {
          key: 6,
          customData: { title: 'another test testing the test for tests' },
          dates: new Date(2022, 1, 1)
        },
        {
          key: 7,
          customData: { title: 'test7' },
          dates: new Date(2022, 1, 2)
        }
      ]
    };
  },
  mounted() {
    this.getEvents()
  },
  methods: {
    handleClick() {
      console.log(this.date.toISOString().slice(0,10))
    },
    async getEvents() {
      console.log('events got')
    }
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
    border: .5px solid lightgray;
    padding-top: 8px;
  }
  .event {
    border: .2px solid lightgray;
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
  form, .calendar-div {
    width: 40%;
  }
  form {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2em;
    padding: 2em
  }
  input, button {
    width: 60%;
  }
</style>
