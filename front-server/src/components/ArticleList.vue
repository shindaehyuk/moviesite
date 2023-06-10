<template>
  <div class="article-list" v-if="articles">
    <ArticleListItem 
    v-for="article in articles" :key="article.id" :article="article"
    />
  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem'

export default {
  name: 'ArticleList',
  components: {
    ArticleListItem,
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  },
  created(){
  },
  data(){
    return{
    }
  },

  methods:{
  }
}
</script>

<style>
.article-list {
  text-align: start;
}
</style>
