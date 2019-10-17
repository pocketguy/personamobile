<template>
  <div>
    <h1>{{ factory.name }}</h1>
    <p><img :src="factory.cover.file" :alt="factory.cover.description" /></p>
    <p>{{ factory.description }}</p>
    <!-- <pre><code>{{ factory }}</code></pre> -->
  </div>
</template>

<script>
export default {
  computed: {
    seoTitle() {
      return this.factory.name
    },
    seoDescription() {
      return this.factory.description
    },
    seoImage() {
      return this.factory.cover.file
    },
    seoImageAlt() {
      return this.factory.cover.description
    }
  },
  async asyncData({ $axios, route }) {
    const slug = encodeURIComponent(route.params.slug)
    const factory = await $axios.$get(`/factories/${slug}/`)
    return {
      factory
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
