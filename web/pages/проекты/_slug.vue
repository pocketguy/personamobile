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
  async asyncData({ $axios, route }) {
    const slug = encodeURIComponent(route.params.slug)
    const project = await $axios.$get(`/projects/${slug}/`)
    return {
      project
    }
  },
  head() {
    return {
      title: this.project.name,
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: this.project.description
        }
      ]
    }
  }
}
</script>
