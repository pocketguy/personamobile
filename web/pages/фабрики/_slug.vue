<template>
  <div>
    <pre><code>{{ factory }}</code></pre>
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
  }
}
</script>
