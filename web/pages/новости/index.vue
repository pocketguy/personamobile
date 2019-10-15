<template>
  <div>
    <h1>{{ title }}</h1>
    <ul>
      <li v-for="post of posts" :key="post.id">
        {{ post.title }}
        <nuxt-link
          :to="{
            name: 'новости-slug',
            params: { slug: post.slug }
          }"
        >
          подробнее
        </nuxt-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: 'Новости'
    }
  },
  async asyncData({ $axios }) {
    const posts = await $axios.$get('/posts/')
    return { posts }
  },
  head() {
    return {
      title: this.title
    }
  }
}
</script>
