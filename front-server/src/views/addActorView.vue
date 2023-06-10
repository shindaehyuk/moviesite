<template>
  <div>
    <h1 class="text-start">원하는 배우를 검색해 보세요!</h1>
    <br>
    <form @submit.prevent="getactor">
        <div class="search-container">
            <input type="text" v-model="content" class="search-input me-3" placeholder="배우 검색">
            <button type="submit" id="submit" class="search-button">검색</button>
        </div>
    </form>
    <div v-if="actors">
        <br>
        <br>
        <h1 class="text-start">검색된 배우를 보여줄게요</h1>
        <div class="row row-cols-1 row-cols-md-4 g-4 my-5">
            <div class="col" v-for="actor in actors" :key="actor.id">
                <div class="card h-100 rounded">
                  <img @click="movefilm(actor.id)" class="rounded" :src="`https://image.tmdb.org/t/p/w500${actor.profile_path}`" alt="">
                </div>
            </div>   
        </div>
    </div>

    <div v-else>
        <br>
        <br>
        <h1 class="text-start">검색된 배우가 없습니다..</h1>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
 name : 'SearchView',
 data(){
    return{
        content : null,
        actors : null,
    }
 },
 components:{
 },

 methods:{
    getactor() {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/search/person?query=${this.content}&include_adult=false&language=ko-KR&page=1`,
        headers: {
          accept: 'application/json',
          Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiNjY5ZDdlOGM3YjljZDNlNmQ2OWQyMmM2NTQzYmU2ZCIsInN1YiI6IjYzZDMxN2I5ZTcyZmU4MDA4NDkxNmNmZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.8DnMZoPyVRhKNXbZJpqls78v7McdxjsUkYNrrmcXR1g'
        }
      })
      .then((res) => {
        if (res.data.results.length != 0){
          this.actors = res.data.results
        }
      })
      .catch((err) => {
          console.log(err)
      })
    },
    movefilm(actor_id){
      this.$router.push({name: 'ActorView' ,params: {id: actor_id }})
    }
 }
}
</script>

<style scoped>
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
.card {
  position: relative;
  z-index: 1;
}

.router-link-class {
  position: relative;
  z-index: 2;
}


</style>