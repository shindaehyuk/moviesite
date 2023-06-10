<template>
  <div>
    <div class="article_top text-start">
      <h1> {{ article?.title }} </h1>
    </div>
    <hr>

    <div class="article_body text-start">
      <p class="fs-4" style="height: 200px"> {{ article?.content }}</p>
      <p>작성시간 : {{ formatDate(article?.created_at) }}</p>
    </div>
    <hr>

    <div class="article_footer d-flex justify-content-between">
      <p> 작성자 : {{ article?.username }} </p>
      <div class="btn_pack">
      <button v-if="article?.username==User" @click="articledelete" type="button" class="btn btn-sm btn-danger me-3" >삭제하기</button>
       
      <router-link v-if="article?.username==User" :to="{ name: 'UpdateView' , params:{id: article?.id, title: article?.title, content: article?.content}} ">
        <button type="button" class="btn btn-sm btn-warning me-3" >수정하기</button>
      </router-link>

      <router-link :to="{ name: 'ArticleView' }" type="button" class="btn btn-info btn-sm ">
        뒤로가기
      </router-link>
      </div>    
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  data() {
    return {
      article: null
    }
  },
  computed:{
    User(){
      return this.$store.state.user.username
    }
  },
  created() {
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/articles/${ this.$route.params.id }/`,
      })
      .then((res) => {
        console.log(res)
        this.article = res.data
      })
      .catch((err) => {
        console.log(err)
        this.$router.push({name: 'NotFound404'})
      })
    },

    formatDate(dateString) {
      if (dateString) {
        const date = new Date(dateString);
        return date.toLocaleDateString('ko-KR', { year: 'numeric', month: 'long', day: 'numeric' });
      }
      return '';
    },
    
    articledelete(){
      axios({
        method: 'delete',
        url: `${API_URL}/movies/articles/${ this.$route.params.id }/`,
      })
      .then(() => {
        this.$router.push({name : 'ArticleView'})
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }
}

</script>

