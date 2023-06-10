<template>
  <div>
    <div class="actor_top">
      <h1 class="text-start border-bottom border-3 border-warning">인물</h1>
    </div>
    
    <div class="actor_body d-flex">
      <img :src="`https://image.tmdb.org/t/p/w500${userdata.profile_path}`" alt="actor" style="width: 200px; height: 300px;">
      <div class="actor_data text-start ms-4">
        <p class="mt-2 fs-5"><b> {{ userdata.name }} </b></p>
        <p> 출생 : {{ userdata.birthday }} </p>
        <p> 국적 : {{ userdata.place_of_birth }} </p>
      </div>
    </div>
    <hr>

    <div class="actor_footer">
      <h3>필모그래피</h3>
      <div class="row row-cols-1 row-cols-md-4 g-4 my-5">
        <div class="col" v-for="movie in movies" :key="movie.id">
          <div class="card h-100">
            <MovieModal :movie="movie"/>
          </div>
          {{ movie.title }}
        </div>   
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieModal from '@/components/MovieModal.vue'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name:'ActorView',

  data(){
    return{
      id : this.$route.params.id,
      userdata : '',
      movies : '',
    }
  },

  components:{
    MovieModal
  },

  created(){
    this.getDetail()
    this.getMovie()
  },

  methods:{
    getDetail(){
      axios({
        method : 'get',
        url : `https://api.themoviedb.org/3/person/${this.$route.params.id}?language=en-US`,
        headers: {
          accept: 'application/json',
          Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiNjY5ZDdlOGM3YjljZDNlNmQ2OWQyMmM2NTQzYmU2ZCIsInN1YiI6IjYzZDMxN2I5ZTcyZmU4MDA4NDkxNmNmZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.8DnMZoPyVRhKNXbZJpqls78v7McdxjsUkYNrrmcXR1g'
        }
      })
      .then(res=>{
        this.userdata = res.data
      })
      .catch((err)=>{
        console.log(err)
        this.$router.push({name: 'NotFound404'})
      }) 
    },

    getMovie(){

      axios({
        method : 'get',
        url: `https://api.themoviedb.org/3/person/${this.$route.params.id}/movie_credits?language=en-US`,
        headers: {
          accept: 'application/json',
          Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiNjY5ZDdlOGM3YjljZDNlNmQ2OWQyMmM2NTQzYmU2ZCIsInN1YiI6IjYzZDMxN2I5ZTcyZmU4MDA4NDkxNmNmZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.8DnMZoPyVRhKNXbZJpqls78v7McdxjsUkYNrrmcXR1g'
        }
      })
      .then(res=>{
        const _ = require('lodash')
        const movies = _.orderBy(res.data.cast, ['release_date'], ['desc']).slice(0, 12);
        axios({
          method : 'post',
          url: `${API_URL}/movies/addmovies/`,
          data: {
            movies
          }
        })
        .then(()=>{
          this.movies = movies
        })
      })
      .catch(err=> {console.log(err)})
    },
  }
}
</script>

<style>

</style>