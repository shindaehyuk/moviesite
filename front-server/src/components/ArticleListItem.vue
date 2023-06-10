<template>
  <div>
    <br>
    <hr>
    <h1>제목 : 
    <router-link class="rotuer-link-class fs-1 text-secondary" :to="{
      name: 'DetailView',
      params: {id: article.id }}">
      {{ article.title }} 
    </router-link>
    </h1>
    <div class="article_data">
      <br>
      <span class="me-5">작성자 : {{article.username}}</span>
      <span>작성시간 : {{ article.created_at.slice(0, 10) }} </span>
    </div>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  }
}
</script>

<style>

</style>
