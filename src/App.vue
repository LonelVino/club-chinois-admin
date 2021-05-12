<template>
  <div id="app">
    <router-view/>
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
      // env.API_URL: in development confition, the path is in the /config/dev.env.js
      axios.get(process.env.API_URL + "/django_api/user/all_names").then(response => {
        app.names = response.data.names;
      });
    },
    // SelectWinner: function() {
    //   var winner = this.names[Math.floor(Math.random()*this.names.length)];
    //   this.winner = winner;
    // },
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
}
</style>
