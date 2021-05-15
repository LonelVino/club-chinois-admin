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
    // this.Init();
  },
  computed: {
    cas_id() { return this.$store.getters.cas_id },
    role() { return this.$store.getters.role}
  },
  created() {

    // //在页面刷新时将vuex里的信息保存到localStorage里
    // window.addEventListener("beforeunload",()=>{
    //   sessionStorage.setItem("cas_id",JSON.stringify(this.$store.getters))
    //   console.log('BEFOREUNLOAD: STORE/GETTERS/CAS_ID:', sessionStorage.getItem("cas_id"))
    // });

    // //在页面加载时读取localStorage里的状态信息
    // if (sessionStorage.getItem("cas_id") ) {
    //   this.$store.replaceState(Object.assign({}, this.$store.getters, JSON.parse(sessionStorage.getItem("store"))))
    //   // console.log('CREATED: STORE/GETTERS/CAS_ID:', this.$store.getters.cas_id)
    //   setTimeout(function () {
    //     localStorage.removeItem("cas_id");
    //   },300)
    // } 
  },
  methods: {
    Init: function() {

      if (this.$store.getters.cas_id == undefined || this.$store.getters.cas_id == 0) {
        if (this.$route.path != '/login') {
          this.$router.push('/')
        }        
      } else {
        this.$store.dispatch('user/getRole', this.$store.getters.cas_id)
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
