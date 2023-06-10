<!-- views/CreateView.vue -->
<template>
    <div class="border rounded bg-light">
      <h1 class="mt-4 mb-4">게시글 작성</h1>
      <form @submit.prevent="updateArticle">
        <label for="title" class="">영화 제목 : </label>
        <input type="text" id="title" v-model.trim="title"><br>
        <label for="content" class="m-3">추천 이유 : </label><br>
        <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
        <input type="submit" id="submit" class="m-3 btn btn-warning" value="수정 완료">
      </form>
      <router-link :to="{ name: 'DetailView', params:{id:this.$route.params.id}}" type="button" class="btn btn-secondary btn-sm mb-4">
        뒤로가기
      </router-link>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  const API_URL = 'http://127.0.0.1:8000'
  
  export default {
    name: 'UpdateView',
    data() {
      return {
        title: this.$route.params.title,
        content: this.$route.params.content,
      }
    },
    methods: {
      updateArticle() {
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
          method: 'put',
          url: `${API_URL}/movies/articles/${this.$route.params.id}/`,
          data: {title, content},
          headers : {
            Authorization : `Token ${this.$store.state.token}`
          }
        })
        .then(() => {
          this.$router.push({name: 'DetailView', params:{id:this.$route.params.id}})
        })
        .catch((err) => {
          console.log(err)
        })
      }
    }
  }
  </script>
  
  <style>
  
  </style>
  