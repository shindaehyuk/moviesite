<template>
  <div id="app" class="container-wrapper">
    <nav v-if="!iconVisible" class="navbar navbar-expand-sm bg-body-white bg-white fixed-top">
      <div class="container-fluid">

        <a class="navbar-brand" href="http://localhost:8080/"><img src="./assets/logo.png" alt="logo" class="logo"><span class="logo_word fs-2 ms-3">Film Oasis</span></a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto mt-5 mt-sm-0 me-3">
            <li class="nav-item mx-1 me-4" v-if="isLogin">
                <i @click="logout" class="bi bi-door-open pe-auto text-primary" style="font-size: 35px; cursor:pointer;"></i><br>
                <span @click="logout" class="account text-secondary" style="cursor:pointer; font-size:12px;"><b>로그아웃</b></span>
            </li>
            <li class="nav-item mx-1 me-4" v-else>
              <router-link :to="{ name: 'LogInView' }" class="router-link-class text-secondary" style="font-size:12px;">
                <i class="bi bi-door-closed text-primary"  style="font-size: 35px;"></i><br>
                로그인
              </router-link>
            </li>
            <li class="nav-item mx-1 me-4">
              <router-link :to="{ name: 'SignUpView' }" class="router-link-class text-secondary" style="font-size:12px;">
                <i class="bi bi-person-add text-primary" style="font-size: 35px;"></i><br>
                회원가입
              </router-link>
            </li>
            <li class="nav-item mx-1">
              <router-link :to="{ name: 'UserInfo' }" class="router-link-class text-secondary" style="font-size:12px;">
                <i class="bi bi-person text-primary" style="font-size: 35px;"></i><br>
                My Oasis
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <nav v-if="!iconVisible" class="navbar navbar-expand bg-body-white bg-white border-bottom border-primary fixed-top " style="margin-top: 90px;">
      <div class="container-fluid">
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
          <ul class="navbar-nav">
            <li class="nav-item ms-3 me-4 mt-1">
              <router-link :to="{ name: 'MovieView' }" class="text-secondary text-decoration-none">Movie</router-link>
            </li>
            <li class="nav-item me-2">
              <div class="dropdown" >
                <button class="btn btn-white text-secondary dropdown-toggle "
                 type="button" data-bs-toggle="dropdown" aria-expanded="false">
                  <b>Like Movies</b>
                </button>
                <ul class="dropdown-menu" >
                  <router-link :to="{ name: 'LikeView' }" class="text-secondary text-decoration-none ms-1">Like & Recommend</router-link>
                  <br> 
                  <router-link :to="{ name: 'LikeTopView' }" class="text-secondary text-decoration-none ms-1">Like Top20</router-link> 
                </ul>
              </div>
            </li>

            <li class="nav-item me-3">
              <div class="dropdown">
                <button class="btn btn-white text-secondary dropdown-toggle "
                 type="button" data-bs-toggle="dropdown" aria-expanded="false">
                  <b>Search Movies</b>
                </button>
                <ul class="dropdown-menu">
                  <router-link :to="{ name: 'addMovieView' }" class="text-secondary text-decoration-none ms-5">영화검색</router-link> 
                  <br>
                  <router-link :to="{ name: 'addActorView' }" class="text-secondary text-decoration-none ms-5">배우검색</router-link>  
                </ul>
              </div>
            </li>

            <li class="nav-item mt-1 me-4"> 
              <router-link :to="{ name: 'ArticleView' }" class="text-secondary text-decoration-none">커뮤니티</router-link> 
            </li>
          </ul>
        </div>
      </div>
    </nav>
    



    <nav v-if="iconVisible" style="padding:0;" class="navbar navbar-expand-lg bg-body-white bg-white fixed-top border-bottom border-5 border-warning">
      <div class="container-fluid bg-light">
        <a class="navbar-brand" href="http://localhost:8080/">
          <img src="./assets/logo.png" alt="logo" class="logo">
          <span class="logo_word fs-2 ms-3 me-4 text-warning">Film Oasis</span>
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item me-4 mt-1">
              <router-link :to="{ name: 'MovieView' }" class="text-warning text-decoration-none">Movie</router-link>
            </li>
            <li class="nav-item me-4">
              <div class="dropdown">
                <button class="btn btn-white text-warning dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                  <b>Like Movies</b>
                </button>
                <ul class="dropdown-menu text-center">
                  <router-link :to="{ name: 'LikeView' }" class="text-warning text-decoration-none">Like & Recommend</router-link>
                  <br> 
                  <router-link :to="{ name: 'LikeTopView' }" class="text-warning text-decoration-none">Like Top20</router-link> 
                </ul>
              </div>
            </li>
            <li class="nav-item me-4">
              <div class="dropdown">
                <button class="btn btn-white text-warning dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                  <b>Search Movies</b>
                </button>
                <ul class="dropdown-menu text-center">
                  <router-link :to="{ name: 'addMovieView' }" class="text-warning text-decoration-none ">영화검색</router-link> 
                  <br>
                  <router-link :to="{ name: 'addActorView' }" class="text-warning text-decoration-none  ">배우검색</router-link>  
                </ul>
              </div>
            </li>
            <li class="nav-item mt-1 me-4"> 
              <router-link :to="{ name: 'ArticleView' }" class="text-warning text-decoration-none">커뮤니티</router-link> 
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <div class="scroll-icon" v-if="iconVisible" @click="scrollToTop">
      <i class="bi bi-arrow-up-circle-fill"></i>
    </div>
    
    <div class="scroll-text text-warning" v-if="iconVisible">
      <a href="https://www.megabox.co.kr/" class="btn btn-warning rounded-5 btn-lg">예매하기</a>
    </div>

    <router-view :key="$route.fullPath" style="margin-top: 170px;"/>
  </div>
</template>


<script>

export default {
  name : 'App',
  data(){
    return{
      iconVisible: false
    }
  },

  computed: {
    isLogin(){
      return this.$store.getters.isLogin
    },
  },

  mounted() {
  window.addEventListener('scroll', this.handleScroll);
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.handleScroll);
  },

  methods : {
    logout(){
      if (confirm("정말 로그아웃하시겠습니까?")) {
        this.$store.commit('LOGOUT_USER')
        this.$router.push({name : 'LogInView'})
      }
    },
    handleScroll() {
      // 스크롤 이벤트 발생 시 아이콘의 표시 여부를 업데이트합니다.
      this.iconVisible = window.scrollY > 0;
    },

    scrollToTop() {
      // 클릭 이벤트 처리 메서드입니다. 페이지를 맨 위로 스크롤합니다.
      window.scrollTo({
        top: 0,
        behavior: 'smooth' // 부드러운 스크롤 효과를 위해 'smooth' 옵션 사용
      });
    },
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.container-wrapper {
    width: 60%;
    margin: 0 auto;
  }
.logo {
  height: 70px;
  width: 110px;
}

.logo_word {
  color : royalblue
}

.account {
  font-size: 10px;
}

.router-link-class {
  text-decoration: none; /* 밑줄 없애기 */
}

.dropdown-toggle{
  border: none;
}

.dropdown-toggle:focus {
  border: none;
}

.scroll-icon {
  position: fixed;
  bottom: 20px;
  right: 20px;
  cursor: pointer;
  font-size: 50px;
}

.scroll-text {
  position: fixed;
  bottom: 100px;
  right: 20px;
  cursor: pointer;
  font-size: 10px;
}

/* .dropbox */



</style>