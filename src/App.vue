<template>
  <div id="app">
    <img src="./assets/logo.png">
    <router-view/>
    <div id="app">
      <button @click="SelectWinner()">Select a Winner</button>
      <p>
        {{winner}}
      </p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'App',
  data() {
    return {
      names: null,
      winner: null,
    }
  },
  mounted: function() {
    this.FetchData();
  },
  methods: {
    FetchData: function() {
      var app = this;
      axios.get("/api_example/").then(response => {
        app.names = response.data.names;
      });
    },
    SelectWinner: function() {
      var winner = this.names[Math.floor(Math.random()*this.names.length)];
      this.winner = winner;
    },
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
