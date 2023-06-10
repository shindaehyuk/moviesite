<!-- views/CreateView.vue -->
<template>
  <div class="border rounded bg-light"  >
    <h1 class="mt-5">이 영화를 추천합니다!</h1>
    <form @submit.prevent="createArticle">
      <label for="title" class="mt-3 mb-3 me-3">영화 제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content" class="mb-2">추천 이유 : </label><br>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit" class="mt-3 btn btn-info" value="작성 완료">
    </form>
    <router-link :to="{ name: 'ArticleView' }" type="button" class="mb-5 btn btn-secondary btn-sm mt-4">
        뒤로가기
    </router-link>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CreateView',
  data() {
    return {
      title: null,
      content: null,
      search : '',
      movies : '',
    }
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    },
  },
  created(){
    this.getUser()
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

    createArticle() {
      const title = this.title
      const content = this.content

      if (!title) {
        alert('제목 입력해주세요')
        return
      } else if (!content){
        alert('내용 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/movies/articles/`,
        data: { title, content},
        headers : {
          Authorization : `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.$router.push({name: 'ArticleView'})
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
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
