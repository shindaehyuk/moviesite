<template>
  <div>
    <div class="d-flex justify-content-between">
      <h1>My Page</h1>
      <button style="width: 100px; height: 50px;" 
      type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
      회원탈퇴
      </button>
    </div>
    <hr>
    <h3 class="text-start">내가 쓴 글</h3>
    <br>
    <div  v-for="(article, index) in articles" :key="article.pk">
      <div v-if="index < 5">
        <h5 class="text-start">제목 : {{article.title}}
          <router-link :to="{
          name: 'DetailView',
          params: {id: article.id }}">
          DETAIL
        </router-link>
        </h5>
        <hr>
      </div>
    </div>
    <h3 class="text-start">내가 좋아요한 영화</h3>
    <div class="row row-cols-1 row-cols-md-4 g-4 my-5">
      <div class="col" v-for="movie in like_movies" :key="movie.id">
        <div class="card h-100">
          <MovieModal :movie="movie"/>
        </div>
      </div>
    </div>




    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">정말로 탈퇴하시겠습니까?</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-footer col">
            <button @click="deleteToken" style="width: 50%; height: 50px;" type="button" class="btn btn-secondary col">YES</button>
            <button id="modaloff" style="width: 50%; height: 50px;" type="button" class="btn btn-secondary col" data-bs-dismiss="modal">NO</button> 
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieModal from '../components/MovieModal.vue'

export default {
  name: 'UserInfo',

  data(){
    return{
      articles : '',
      comments : '',
    }
  },

  components:{
    MovieModal
  },

  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    },
    user(){
        return this.$store.state.user.username
    },
    like_movies(){
      return this.$store.state.like_movies
    }
    
  },

  created() {
    this.getUser()
    this.Myarticle()
    this.Mycomment()
    this.getLikeRec()
  },

  methods: {
    getUser(){
      if (this.isLogin){
        this.$store.dispatch('getUser')
      }else{
        alert('로그인이 필요한 페이지입니다...')
        this.$router.push({ name: 'LogInView' })
      }
    },

    deleteToken(){
      const username = this.user
      const modaloff = document.querySelector('#modaloff')

      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movies/userdelete/`,
        data : {
          username
        },
      })
      .then(() => {
        this.$store.commit('DELETE_TOKEN')
        modaloff.click()
        alert('탈퇴가 완료되었습니다.')
        this.$router.push({name: 'LogInView'})
      })
      .catch((err) => {
        console.log(err)
      })
    },

    Myarticle(){
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/userinfo/${this.$store.state.user.pk}/`,
        headers : {
          Authorization : `Token ${this.$store.state.token}`
        },
      })
      .then((res) => {
        this.articles = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },

    Mycomment(){
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/comments/user/${this.$store.state.user.pk}/`,
        headers : {
          Authorization : `Token ${this.$store.state.token}`
        },
      })
      .then((res) => {
        console.log(res)
        this.comments = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },

    getLikeRec(){
      this.$store.dispatch('getLikeRec')
    },

  } 
}

</script>

<style>

</style>
