<template>
  <div>
    <h1>Calendr</h1>
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

export default {
  name: "Calendar",
  components: {
    DatePicker,
  },
  data() {
    return {
      date: new Date(),
    };
  },
  methods: {
    handleClick() {
      console.log(this.date.toISOString().slice(0,10))
    },
  },
};
</script>

<style>
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
