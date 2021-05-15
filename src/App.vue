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
    this.Init();
  },
  computed: {
    cas_id() { return this.$store.cas_id },
    role() { return this.$store.role}
  },
  methods: {
    Init: function() {
      this.$store.dispatch('user/getRole', this.cas_id)
      this.$store.dispatch('user/getInfo', 2)    
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
}
</style>
