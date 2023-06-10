import Vue from 'vue'
import VueRouter from 'vue-router'
import ArticleView from '@/views/ArticleView'
import CreateView from '@/views/CreateView'
import DetailView from '@/views/DetailView'
import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import UserInfo from '@/views/UserinfoView'

import MovieView from '@/views/MovieView'
import LikeView from '@/views/LikeView'
import MovieDetailView from '@/views/MovieDetailView'
import ActorView from '@/views/ActorView'
import LikeTopView from '@/views/LikeTopView'
import UpdateView from '@/views/UpdateView'
import addMovieView from '@/views/addMovieView'
import addActorView from '@/views/addActorView'
import NotFound404 from '@/views/NotFound404'


Vue.use(VueRouter)

const routes = [
  
  {
    path: '/',
    name: 'MovieView',
    component: MovieView,
  },

  {
    path: '/article',
    name: 'ArticleView',
    component: ArticleView
  },
 
  {
    path: '/create',
    name: 'CreateView',
    component: CreateView
  },

  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },

  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },
  {
    path: '/userinfo',
    name: 'UserInfo',
    component: UserInfo,
  },

  {
    path: '/like',
    name: 'LikeView',
    component: LikeView,
  },

  {
    path: '/addMovie',
    name: 'addMovieView',
    component: addMovieView,
  },

  {
    path: '/addActor',
    name: 'addActorView',
    component: addActorView,
  },

  {
    path: '/liketop',
    name: 'LikeTopView',
    component: LikeTopView,
  },
  {
    path: '/movies/:id',
    name: 'MovieDetailView',
    component: MovieDetailView,
  },

  {
    path: '/:id',
    name: 'DetailView',
    component: DetailView,
  },

  {
    path: '/actor/:id/',
    name: 'ActorView',
    component: ActorView,
  },

  {
    path: '/create/:id/',
    name: 'UpdateView',
    component: UpdateView
  },

  {
    path: '*',
    name: 'NotFound404',
    component: NotFound404,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})


export default router

