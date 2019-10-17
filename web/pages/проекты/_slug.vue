<template>
  <div>
    <h1>{{ project.name }}</h1>
    <p><img :src="project.cover.file" :alt="project.cover.description" /></p>
    <p>{{ project.description }}</p>
    <!-- <pre><code>{{ project }}</code></pre> -->
  </div>
</template>

<script>
export default {
  computed: {
    seoTitle() {
      return this.project.name
    },
    seoDescription() {
      return this.project.description
    },
    seoImage() {
      return this.project.cover.file
    },
    seoImageAlt() {
      return this.project.cover.description
    }
  },
  async asyncData({ $axios, route }) {
    const slug = encodeURIComponent(route.params.slug)
    const project = await $axios.$get(`/projects/${slug}/`)
    return {
      project
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
