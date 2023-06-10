<template>
  <div>
    <h1 class="text-start mb-5"><b>좋아요 TOP 20</b></h1>
    <div class="row row-cols-1 row-cols-md-5 g-4 my-5">
      <div class="col" v-for="movie in most_movies" :key="movie.id">
        <div class="card h-100">
          <MovieModal :movie="movie"/>
        </div>
      </div>   
    </div>
  </div>
</template>

<script>
import MovieModal from '../components/MovieModal.vue'

export default {
  name : 'LikeView',

  components:{
    MovieModal
  },

  data(){
    return{
    }
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    },
    user(){
      return this.$store.state.user.pk
    },
    most_movies(){
      return this.$store.state.most_movies
    },
  },

  created(){
    this.checkLogin()
    this.getLikeRec()
  },
  
  methods:{
    checkLogin(){
      if (this.isLogin){
        this.$store.dispatch('getUser')
      }else{
        alert('로그인이 필요한 페이지입니다...')
        this.$router.push({ name: 'LogInView' })
      }
    },
    getLikeRec(){
      this.$store.dispatch('getLikeRec')
    }, 
  }
  
}
</script>

<style>

</style>