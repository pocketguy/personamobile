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
  async asyncData({ $axios, route }) {
    const slug = encodeURIComponent(route.params.slug)
    const factory = await $axios.$get(`/factories/${slug}/`)
    return {
      factory
    }
  },
  head() {
    return {
      title: this.factory.name,
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: this.factory.description
        }
      ]
    }
  }
}
</script>
