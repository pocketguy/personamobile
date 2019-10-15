<template>
  <div>
    <h1>{{ post.title }}</h1>
    <p><img :src="post.cover.file" :alt="post.cover.description" /></p>
    <p-dynamic-html :content="post.text"></p-dynamic-html>
    <pre><code>{{ post }}</code></pre>
  </div>
</template>

<script>
import PDynamicHtml from '~/components/PDynamicHtml.vue'
export default {
  components: {
    PDynamicHtml
  },
  async asyncData({ $axios, route }) {
    const slug = encodeURIComponent(route.params.slug)
    const post = await $axios.$get(`/posts/${slug}/`)
    return {
      post
    }
  },
  head() {
    return {
      title: this.post.seo_title || this.post.title,
      meta: [
        // hid is used as unique identifier. Do not use `vmid` for it as it will not work
        {
          hid: 'description',
          name: 'description',
          content: this.post.seo_description
        }
      ]
    }
  }
}
</script>
