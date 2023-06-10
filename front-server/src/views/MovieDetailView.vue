<template>
  <div>
    <h1 style="text-align:left;" >  {{ movie?.title }}</h1>
    <div class="top d-flex  justify-content-between">
      <img :src="`https://image.tmdb.org/t/p/w500${movie?.poster_path}`" alt="" 
        class="border border-3 me-5 rounded shadow-lg" style="height:360px; width: 260px;">
      <iframe class="shadow-lg p-3 mb-4 bg-body-primary rounded border border-3" id="player" type="text/html" width="900" height="360"
      :src="url" frameborder="0"></iframe>
      <hr>
    </div>
    
    <div class="middle">
      <div class="text-start mt-3 mb-4">
        <span class="me-4">감독 : </span>
        <router-link class="router-link-class" :to="{name: 'ActorView',params: {id: director[0].id }}">
          <span class="text-secondary">{{ director[0].name }} </span>
        </router-link>
      </div>


      <div class="actor row mb-4">
        <span class="text-start"> 출연진 : </span> 
        <div v-for="actor in cast" :key="actor.id" class="col d-flex justify-content-center align-items-center">
          <span class="me-4 ms-2">
            <router-link class="router-link-class" :to="{name: 'ActorView',params: {id: actor.id }}">
              <span class="text-secondary">{{ actor.name }} </span>
            </router-link>
          </span>
        </div>
      </div>
      
      <div class="middle_top d-flex align-items-center">
        <p class="text-start">개봉일 : {{ movie?.release_date }} ㅣ</p>
        <a class="mb-3" v-if="Liked" @click="addLike">
          <i class="bi bi-heart-fill text-decoration-none text-danger heart"></i>
        </a>
        <a class="mb-3" v-else @click="addLike">
          <i class="bi bi-heart text-decoration-none text-danger heart"></i>
        </a>
        <p>ㅣ {{total_likes}}명이 이 영화를 좋아합니다</p>
      </div>
      
      <hr>
      
      <div class="middle_bottom">
        <p> {{ movie?.overview }} </p>
      </div>
    </div>

    <hr>   
      
    <button type="button" class="btn btn-primary my-3" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@mdo">리뷰 작성하기</button>
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">평점 작성</h1>
            <button id="modaloff" type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <h3>{{ movie?.title }}</h3><hr>
            <form @submit.prevent="createComment">
              <label for="exampleFormControlTextarea1" class="form-label">내용 : </label>
              <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" v-model="content" placeholder="내용을 입력해주세요" @input="limitText"></textarea>
              <br>
              <div class="col">
                <label for="inputState" class="form-label">평점을 추가해주세요!</label>
                <select id="inputState" class="form-select" v-model="star">
                  <option disabled selected>Choose...</option>
                  <option class="text-warning">★☆☆☆☆</option>
                  <option class="text-warning">★★☆☆☆</option>
                  <option class="text-warning">★★★☆☆</option>
                  <option class="text-warning">★★★★☆</option>
                  <option class="text-warning">★★★★☆</option>
                  <option class="text-warning">★★★★★</option>
                </select>
              </div>
              <br>
              <input type="submit" class="btn btn-warning col" id="submit" data-bs-dismiss="modal" value="작성하기">
            </form>
          </div>
        </div>
      </div>
    </div> 
    <div class="bottom">
      <div v-if="comments"> 
        <div v-for="comment in comments" :key="comment.id">
          <hr>
          <div class="d-flex justify-content-between">
            <li class=" d-flex align-items-center">
              <span class="me-4">{{ comment.username }}</span>
              <span class="me-4 text-warning">{{ comment.star}}</span>
              <span>{{ comment.content}}</span>
              
            </li>
            <button v-if="comment.user=== user" @click="deleteComment(comment.id)" class="btn btn-sm btn-danger"> 삭제</button>
          </div>
          <!-- <button @click="deleteComment"> 삭제 </button>
          <button @click="updateComment"> 수정 </button> -->
        </div>
      </div>
    </div>
   
    
    <hr>
    <h1 class="text-start">함께 시청한 콘텐츠</h1>
    <div id="carouselExampleIndicators" class="carousel slide">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <div class="row ">
            <div class="col">
              <MovieModal :movie="recommendation_movies[0]" />
            </div>
            <div class="col">
              <MovieModal :movie="recommendation_movies[1]" />
            </div>
            <div class="col">
              <MovieModal :movie="recommendation_movies[2]" />
            </div>
            <div class="col">
              <MovieModal :movie="recommendation_movies[3]" />
            </div>
          </div>
        </div>
        <div class="carousel-item">
          <div class="row">
            <div class="col">
              <MovieModal :movie="recommendation_movies[4]" />
            </div>
            <div class="col">
              <MovieModal :movie="recommendation_movies[5]" />
            </div>
            <div class="col">
              <MovieModal :movie="recommendation_movies[6]" />
            </div>
            <div class="col">
              <MovieModal :movie="recommendation_movies[7]" />
            </div>
          </div>
        </div>
        <div class="carousel-item">
          <div class="row">
            <div class="col">
              <MovieModal :movie="recommendation_movies[8]" />
            </div>
            <div class="col">
              <MovieModal :movie="recommendation_movies[9]" />
            </div>
            <div class="col">
              <MovieModal :movie="recommendation_movies[10]" />
            </div>
            <div class="col">
              <MovieModal :movie="recommendation_movies[11]" />
            </div>
          </div>
        </div>
      </div>
      <br>
      <br>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
</template>


<script >
  import MovieModal from '../components/MovieModal.vue';

  import axios from 'axios';
  const API_URL = 'http://127.0.0.1:8000'

  export default {
    name: 'MovieDetailView',

    components:{
      MovieModal
    },

    computed:{
      recommendation_movies(){
        return this.$store.state.recommendation_movies
      },
      isLogin(){
        return this.$store.getters.isLogin
      },
      user(){
        return this.$store.state.user.pk
      }
    },
 
    data() {
      return {
        movie : null,
        content : '',
        comments : null,
        total_likes : '',

        url : '',
        title:'',
        Liked : '',
        star: null,
        
        cast : '',
        director : '',
      }
    },
  
    created() {
      this.getMovieDetail()
      this.showComment()
      this.firstLike()
      this.getactor()
    },

    methods: {

      limitText() {
        if (this.content.length > 50) {
          this.content = this.content.slice(0, 50);
        }
      },

      showSelectedOption() {
        console.log(this.star);
      },

      getMovieDetail() {
        axios({
          method: 'get',
          url: `${API_URL}/movies/${this.$route.params.id}/`,
        })
        .then((res) => {
          this.q = res.data.title
          this.movie = res.data
          this.youtube()
        })
        .catch((err) => {
          console.log(err)
        })
      },

      showComment() {
        axios({
            method: 'get',
            url: `${API_URL}/movies/${this.$route.params.id}/comments/detail/`,
        })
        .then((res) => {
          this.comments = res.data
        })
        .catch((err) => {
            console.log(err)
        })
      },

      createComment() {
        const content = this.content
        const star = this.star

        if (!this.isLogin){
          alert('로그인이 필요한 페이지입니다...')
          this.modaloff()
          this.$router.push({ name: 'LogInView' })
        }
        else if (!content) {
          alert('제목을 입력해주세요!');
          return
        }
        else if (!star) {
          alert('별점을 선택해주세요!');
          return
        }

        axios({
            method: 'post',
            url: `${API_URL}/movies/${this.$route.params.id}/comments/`,
            data: {content, star},
            headers : {
            Authorization : `Token ${this.$store.state.token}`
            }
        })
        .then(() => {
            this.showComment()
            this.content = null
            this.star = null
        })
        .catch((err) => {
          console.log(err)
        })
      },

      deleteComment(comment_id) {
        axios({
            method: 'delete',
            url: `${API_URL}/movies/${this.$route.params.id}/comments/detail/${comment_id}`,
            headers : {
            Authorization : `Token ${this.$store.state.token}`
            }
        })
        .then(() => {
          this.showComment()
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
        }
         axios({
            method: 'post',
            url: `${API_URL}/movies/${this.$route.params.id}/movie_likes/`,
            headers : {
            Authorization : `Token ${this.$store.state.token}`
            }
        })
        .then((res) => {
          this.total_likes = res.data.total_likes
          this.Liked = res.data.liked
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
          this.$router.push({name: 'NotFound404'})
        })
      },

      firstLike(){
        if (!this.isLogin){
          axios({
              method: 'get',
              url: `${API_URL}/movies/${this.$route.params.id}/first_likes/`,
          })
          .then((res) => {
            this.total_likes = res.data.total_likes
            this.Liked = res.data.liked
          })
          .catch((err) => {
            this.$router.push({name: 'NotFound404'})
            console.log(err)
          })
        }else{
          axios({
              method: 'get',
              url: `${API_URL}/movies/${this.$route.params.id}/movie_likes/`,
              headers : {
              Authorization : `Token ${this.$store.state.token}`
            }
          })
          .then((res) => {
            this.total_likes = res.data.total_likes
            this.Liked = res.data.liked
          })
          .catch((err) => {
            console.log(err)
            this.$router.push({name: 'NotFound404'})
          })
        }
      },

      youtube(){
        axios({
          method : 'get',
          url : 'https://www.googleapis.com/youtube/v3/search',
          params:{
            // key:'AIzaSyABa4lTtmjVeLK3VRgy1qhfekP2s4opp8w',
            key:'AIzaSyBjzEnBTudsvky6RziKLxenIMhAJKB0a28',
            q: this.movie.title +'메인 예고편',
            type:'viedo',
            part:'snippet',
          }
        })
        .then((res) =>{
          this.url = `http://www.youtube.com/embed/${res.data.items[0].id.videoId}`
          this.title = res.data.items[0].snippet.title
        })
        .catch((res)=>{
          console.log(res)
        }) 
      },

      modaloff(){
        const modaloff = document.querySelector('#modaloff')
        modaloff.click()
      },

      getactor() {
        axios({
            method: 'get',
             url: `https://api.themoviedb.org/3/movie/${this.$route.params.id}/credits?language=en-US`,
             headers: {
              accept: 'application/json',
              Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiNjY5ZDdlOGM3YjljZDNlNmQ2OWQyMmM2NTQzYmU2ZCIsInN1YiI6IjYzZDMxN2I5ZTcyZmU4MDA4NDkxNmNmZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.8DnMZoPyVRhKNXbZJpqls78v7McdxjsUkYNrrmcXR1g'
            }
        })
        .then((res) => {
          this.cast = res.data.cast.slice(0, 5)
          const crews = res.data.crew

          this.director= crews.filter(crew => crew.job === 'Director');
        })
        .catch((err) => {
          this.$router.push({name: 'NotFound404'})
          console.log(err)
        })
      },


    },
  }
  </script>

<style>

.carousel-inner {
  overflow: visible;
  position: relative;
}

</style>