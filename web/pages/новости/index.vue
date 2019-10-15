<template>
  <div>
    <ul>
      <li v-for="post of posts" :key="post.id">
        {{ post.title }}
        <nuxt-link :to="{ name: 'новости-slug', params: { slug: post.slug } }"
          >подробнее</nuxt-link
        >
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  async asyncData({ $axios }) {
    const posts = await $axios.$get('/posts/')
    return { posts }
  }
}
</script>
