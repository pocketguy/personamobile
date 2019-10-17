<template>
  <div>
    <h1>{{ post.title }}</h1>
    <p><img :src="post.cover.file" :alt="post.cover.description" /></p>
    <p-dynamic-html :content="post.text"></p-dynamic-html>
    <!-- <pre><code>{{ post }}</code></pre> -->
  </div>
</template>

<script>
import PDynamicHtml from '~/components/PDynamicHtml.vue'
export default {
  components: {
    PDynamicHtml
  },
  computed: {
    firstParagraph() {
      const a = this.post.text.match(/<p>(.*?)<\/p>/)
      return a[1]
    },
    seoTitle() {
      return this.post.seo_title || this.post.title
    },
    seoDescription() {
      return this.post.seo_description || this.firstParagraph
    },
    seoImage() {
      return this.post.cover.file
    },
    seoImageAlt() {
      return this.post.cover.description
    }
  },
  async asyncData({ $axios, route }) {
    const slug = encodeURIComponent(route.params.slug)
    const post = await $axios.$get(`/posts/${slug}/`)
    return {
      post
    }
  },
  head() {
    return this.$seoHead(
      this.seoTitle,
      this.seoDescription,
      this.seoImage,
      this.seoImageAlt
    )
  }
}
</script>
