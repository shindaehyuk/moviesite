<template>
  <div>
    <div class="box-size">
      <div class="responsive-iframe">
        <iframe class="shadow-lg p-3 mb-5 bg-body-primary rounded" id="player" type="text/html" :src="url" frameborder="0" allowfullscreen></iframe>
      </div>
      <br>
    </div>

    <div class="container-fluid">
      <h1 class="text-start my-5">
        <span @click="toggle1" class="text-primary">인기순 &nbsp;|</span>
        <span @click="toggle2" class="text-primary ms-3">평점순 &nbsp;|</span>
        <span @click="toggle3" class="text-primary ms-3">최신순</span>
      </h1>
      <div class="row row-cols-1 row-cols-md-5 g-4 mb-5" >
        <div class="col" v-for="movie in movies" :key="movie.id" :movie="movie">
          <MovieModal :movie="movie"/>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import MovieModal from '@/components/MovieModal'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieList',

  components:{
    MovieModal
  },

  data(){
      return{
          movies : '',
          url : '',
          title:'',
          q : '',
          rankmovies : '',
          popularmovies : '',
          newmovies : '',
  
      }
  },

  created(){
    this.movieList()
    this.rankList()
    this.newList()
  },

  methods:{

    movieList(){
      axios({
          method: 'get',
          url: `${API_URL}/movies/popular_movies/`,
      })
      .then((res) => {
        console.log(res)
          this.movies = res.data.popular_movies
          this.popularmovies = res.data.popular_movies
          const randomIndex = Math.floor(Math.random() * this.movies.length);
          const randomMovie = this.movies[randomIndex];
          this.q = randomMovie.title
          this.youtube()
      })
      .catch((err) => {
          console.log(err)
      })
    },

    rankList(){
      axios({
          method: 'get',
          url: `${API_URL}/movies/rank_movies/`,
      })
      .then((res) => {
          this.rankmovies = res.data.rank_movies
      })
      .catch((err) => {
          console.log(err)
      })
    },

    newList(){
      axios({
          method: 'get',
          url: `${API_URL}/movies/new_movies/`,
      })
      .then((res) => {
          this.newmovies = res.data.new_movies
      })
      .catch((err) => {
          console.log(err)
      })
    },

    youtube(){
      axios({
        methods : 'get',
        url : 'https://www.googleapis.com/youtube/v3/search',
        params:{
          // key:'AIzaSyABa4lTtmjVeLK3VRgy1qhfekP2s4opp8w',
          key:'AIzaSyBjzEnBTudsvky6RziKLxenIMhAJKB0a28',
          // key : 'AIzaSyAY3KpvqWI5GhSQUhf8Mjn1wq8bqVht1sI',
          q: this.q + '예고편',
          type:'viedo',
          part:'snippet',
        }
      })
      .then((res) =>{
        this.url = `http://www.youtube.com/embed/${res.data.items[0].id.videoId}?autoplay=1&mute=1&loop=1&playlist=${res.data.items[0].id.videoId}&modestbranding=1`
        this.title = res.data.items[0].snippet.title
      })
      .catch((res)=>{
        console.log(res)
      }) 
    },

    toggle1(){
      this.movies = this.popularmovies
    },
    toggle2(){
      this.movies = this.rankmovies
    },
    toggle3(){
      this.movies = this.newmovies
    }
  },
}


</script>

<style>
.responsive-iframe {
  position: relative;
  padding-bottom: 56.25%;
  height: 0;
}

.responsive-iframe iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
.box-size{
  width: 100%;
  /* margin-left */
}
</style>  