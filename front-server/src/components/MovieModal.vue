<template>
  <div class="card h-100 shadow-lg">
    <img style="height:100%" @click="active" type="button" data-bs-toggle="modal" :data-bs-target="`#${movie.id}`" 
      class="card-img-top rounded poster_img" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
    >
    <div class="modal fade" :id="movie.id"  tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog ">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-1" id="exampleModalLabel">{{ movie?.title }}</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" style="width:100px;"></button>
          </div>
          <div class="modal-body">
            <img :src="`https://image.tmdb.org/t/p/w500${movie?.poster_path}`" alt="" 
            class="mb-4" style="height:360px; width: 260px;">
            <br>
            <div class="d-flex  justify-content-center"> 
              <p class="me-4">평점 : {{ movie?.vote_average }}점</p>
              <a v-show="Liked"  @click="addLike" class="position-relative">
                <i class="bi bi-heart-fill text-decoration-none text-danger heart" style="cursor:pointer;"></i>
                <span class="ms-2 position-absolute top-0 start-100 translate-middle badge rounded-pill bg-warning">
                  {{total_likes}} 
                  <span class="visually-hidden">{{total_likes}}명이 이 영화를 좋아</span>
                </span>
              </a>

              <a v-show="!Liked" @click="addLike" class="position-relative">
                <i class="bi bi-heart text-decoration-none text-danger heart" style="cursor:pointer;"></i>
                <span class="ms-2 position-absolute top-0 start-100 translate-middle badge rounded-pill bg-warning">
                  {{total_likes}} 
                  <span class="visually-hidden">{{total_likes}}명이 이 영화를 좋아</span>
                </span>
              </a>
              
            </div>
            <div> 개봉일 : {{ movie.release_date }} </div><hr>
            <p> {{ movie.overview }} </p>

          
            <div v-if="comments" class="align-items-center"> 
              <div v-for="comment in comments" :key="comment.id">
                <hr>
                  <div>
                    <span class="me-1"> {{ comment.username }} ㅣ</span>
                    <span class="text-warning"> {{ comment.star }} </span><br>
                    <span class=""> {{ comment.content }} </span>
                  </div>
              </div>
            </div>

          </div>
          <div class="modal-footer">
            <router-link :to="{name: 'MovieDetailView',
              params: {id: movie.id }}">
              <button @click="recommendation" type="button" class="btn btn-secondary " data-bs-dismiss="modal" aria-label="DETAIL">자세히 보기</button>
            </router-link>
              <button id="modaloff" type="button" class="btn btn-secondary " data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script>
  import axios from 'axios'
  // import * as bootstrap from 'bootstrap'
  const API_URL = 'http://127.0.0.1:8000'
  
  export default {
    name: 'MovieModal',

    data() {
      return {
        content : null,
        comments : null,
        total_likes : '',

        id :this.movie.id,
        Liked : '',
        modaltoken: false,
      }
    },

    props:{
      movie : Object
    },
    
    computed: {
      isLogin(){
        return this.$store.getters.isLogin
      },
    },

    methods: {

      modaloff(){
        const off = document.querySelector('#modaloff')
        off.click()
      },

      active(){
        this.showComment()
        this.firstLike()
      },

      showComment() {
        axios({
            method: 'get',
            url: `${API_URL}/movies/${this.movie.id}/comments/detail/`,
        })
        .then((res) => {
          this.comments = res.data
        })
        .catch((err) => {
            console.log(err)
        })
      },

      addLike(){
        if (!this.isLogin){
          alert('로그인이 필요한 페이지입니다...')
          this.modaloff()
          this.$router.push({ name: 'LogInView' })
          return
        }
        const id = this.id
        axios({
          method: 'post',
          url: `${API_URL}/movies/${this.movie.id}/movie_likes/`,
          data:{
              id
            },
          headers : {
            Authorization : `Token ${this.$store.state.token}`
          }
        })
        .then((res) => {
          this.total_likes = res.data.total_likes
          this.Liked = res.data.liked
          if(this.$route.path ==='/like'){
            window.location.reload()
          }
          if(this.$route.path ==='/liketop'){
            window.location.reload()
          }
          if(this.$route.path ==='/userinfo'){
            window.location.reload()
          }
          
        })
        .catch((err) => {
            console.log(err)
            this.$router.push({name: 'NotFound404'})
        })
      },

      firstLike(){
        if (!this.isLogin){
          const id = this.id
          axios({
              method: 'get',
              url: `${API_URL}/movies/${this.id}/first_likes/`,
              data:{
                id
              },
          })
          .then((res) => {
            this.total_likes = res.data.total_likes
            this.Liked = res.data.liked
          })
          .catch((err) => {
            console.log(err)
          })

        }else{
          const id = this.id
          axios({
              method: 'get',
              url: `${API_URL}/movies/${this.id}/movie_likes/`,
              data:{
                id
              },
              headers : {
              Authorization : `Token ${this.$store.state.token}`
            }
          })
          .then((res) => {
            this.total_likes = res.data.total_likes
            this.Liked = res.data.liked
            console.log(this.total_likes)
            console.log(this.Liked)
          })
          .catch((err) => {
            console.log(err)
            this.$router.push({name: 'NotFound404'})
          })
        }
        
      },

      recommendation(){
        this.$store.dispatch('recommendation', this.movie.id)
      },

      
    }
  }
  </script>

<style>
.poster_img{
  overflow: hidden; 
}

.poster_img{
  object-fit:cover;     
  transform:scale(1.0);        
  transition: transform .5s;
  z-index : 1; 
}

.poster_img:hover{ 
  transform:scale(1.3);
  transition: transform .5s;
  z-index :  2;
}

@font-face {
    font-family: 'KCC-Ganpan';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2302@1.0/KCC-Ganpan.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}
div{
  font-family: 'KCC-Ganpan';
}

</style>