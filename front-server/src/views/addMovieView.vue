<template>
  <div>
    <h1 class="text-start">원하는 영화를 검색해 보세요!</h1>
    <br>
    <form @submit.prevent="findmovie">
        <div class="search-container">
            <input type="text" v-model="content" class="search-input me-3" placeholder="영화 검색">
            <button type="submit" id="submit" class="search-button">검색</button>
        </div>
    </form>
    <div v-if="movies">
        <br>
        <br>
        <h1 class="text-start">검색된 영화를 보여줄게요</h1>
        <div class="row row-cols-1 row-cols-md-4 g-4 my-5">
            <div class="col" v-for="movie in movies" :key="movie.id">
                <div class="card h-100">
                    <MovieModal :movie="movie"/>
                </div>
            </div>   
        </div>
    </div>

    <div v-else>
        <br>
        <br>
        <h1 class="text-start">검색된 영화가 없습니다..</h1>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
import MovieModal from '@/components/MovieModal.vue'

export default {
 name : 'SearchView',
 data(){
    return{
        content : null,
        movies : null,
    }
 },
 components:{
    MovieModal
 },

 methods:{
    findmovie(){
        axios({
          method: 'get',
          url: `https://api.themoviedb.org/3/search/movie?query=${this.content}&include_adult=false&language=ko-KR&page=1`,
           headers: {
            accept: 'application/json',
            Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiNjY5ZDdlOGM3YjljZDNlNmQ2OWQyMmM2NTQzYmU2ZCIsInN1YiI6IjYzZDMxN2I5ZTcyZmU4MDA4NDkxNmNmZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.8DnMZoPyVRhKNXbZJpqls78v7McdxjsUkYNrrmcXR1g'
          }
        })
        .then((res) => {
          console.log(res.data.results)
          const movies = res.data.results
          axios({
            method : 'post',
            url: `${API_URL}/movies/addmovies/`,
            data: {
              movies
            }
          })
          .then(()=>{
            if (movies.length != 0){
              this.movies = movies
            }
          })
        })
        .catch((err) => {
          alert('검색된 영화가 없습니다!')
          console.log(err)
        })
    }
 }
}
</script>

<style>
.search-container {
  display: flex;
  align-items: center;
}

.search-input {
  padding: 8px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  flex: 1;
}

.search-button {
  padding: 8px 16px;
  font-size: 16px;
  border: none;
  background-color: #f2f2f2;
  border-radius: 4px;
  cursor: pointer;
}
</style>