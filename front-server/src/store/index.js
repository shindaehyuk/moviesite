import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    articles: [
    ],
    user : '',
    token: null,
    movie_title : '',
    recommendation_movies : '',
    like_movies : '',
    rec_movies: '',
    most_movies: '',
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    // signup & login -> 완료하면 토큰 발급
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name : 'MovieView'}) // store/index.js $router 접근 불가 -> import를 해야함
    },
    GET_USER(state, data){
      state.user = data
    },
    LOGOUT_USER(state){
      state.token = null
      state.articles = null
      state.user = null
    },
    DELETE_TOKEN(state){
      state.token = null
      state.articles = null
      state.user = null
    },
    REC_MOVIES(state, data){
      state.recommendation_movies = data
    },
    LIKE_REC(state, data){
      state.like_movies = data.user_movies
      state.rec_movies = data.movies
      state.most_movies = data.top_movies
    },
  },

  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/articles/`,
        headers : {
          Authorization : `Token ${context.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          context.commit('GET_ARTICLES', res.data)
        })
        .catch(() => {
          alert('작성된 게시글이 없습니다.!')
          context.commit('GET_ARTICLES', [])
      })
    },

    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
          alert('아이디가 존재하거나 비밀번호가 맞지 않습니다.')
          console.log(err)
      })
    },

    login(context, payload) {
      console.log(payload)
      const username = payload.username
      const password = payload.password

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
      .then((res) => {
        console.log(res)
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err) => {
        alert('아이디가 존재하지 않거나 비밀번호가 틀립니다.')
        console.log(err)
      })
    },
      

    getUser(context){
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers : {
          Authorization : `Token ${context.state.token}`
        }
      })
        .then((res) => {
          context.commit('GET_USER', res.data)
        })
      .catch((err) => {
        console.log(err)
        console.log('유저정보가 없습니다.!')
      })

    },

    recommendation(context, movie_id){
      axios({
        method : 'get',
        url: `https://api.themoviedb.org/3/movie/${movie_id}/recommendations?language=ko-KR&page=1`,
         headers: {
          accept: 'application/json',
          Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiNjY5ZDdlOGM3YjljZDNlNmQ2OWQyMmM2NTQzYmU2ZCIsInN1YiI6IjYzZDMxN2I5ZTcyZmU4MDA4NDkxNmNmZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.8DnMZoPyVRhKNXbZJpqls78v7McdxjsUkYNrrmcXR1g'
        }
      })
      .then((res) =>{
        const movies = res.data['results']
        context.commit('REC_MOVIES', movies)

        axios({
          method : 'post',
          url: `${API_URL}/movies/addmovies/`,
          data: {
            movies
          }
        })
        .then(()=>{
        })
      })
      .catch((res)=>{
        console.log(res)
      }) 

    },

    getLikeRec(context){
      const user = context.state.user.pk
      axios({
        method: 'get',
        url: `${API_URL}/movies/${context.state.user.pk}/recommend_movies/`,
        data: {user},
        headers : {
        Authorization : `Token ${context.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          context.commit('LIKE_REC', res.data)
        })
        .catch((err) => {
            console.log(err)
        })
    },

    mostLiked(context){
      axios({
        method: 'get',
        url: `${API_URL}/movies/most_liked/`,
        headers : {
        Authorization : `Token ${context.state.token}`
        }
      })
      .then((res) => {
        console.log(res)
        context.commit('MOST_LIKED', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },



    
  },
  modules: {
  }
})
