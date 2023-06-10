<template>
  <div>
    <MovieList/>
  </div>
</template>

<script>
// import axios from 'axios'
import MovieList from '../components/MovieList.vue'

// const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'MovieView',
  components: {
    MovieList,
  },
  data(){
    return{
    }
  },
  created(){
    this.getUser()
  },

  methods:{
    getUser(){
      this.$store.dispatch('getUser')
    }
  }
}
</script>

<style>

</style>