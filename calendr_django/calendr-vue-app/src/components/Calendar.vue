<template>
  <div>
    <p>This is Calendar</p>
    <button v-on:click="handleClick"></button>
    <DatePicker v-model="date"> </DatePicker>
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
      console.log(this.date);
    },
  },
};
</script>

<style></style>
