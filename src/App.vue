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
      if (this.cas_id == undefined) {
        this.$router.push('/login')
      } else {
        this.$store.dispatch('user/getRole', this.cas_id)
      }
      
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
