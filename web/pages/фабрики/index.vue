<template>
  <div>
    <ul>
      <li v-for="factory of factories" :key="factory.id">
        {{ factory.name }}
        <nuxt-link
          :to="{ name: 'фабрики-slug', params: { slug: factory.slug } }"
          >подробнее</nuxt-link
        >
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  async asyncData({ $axios }) {
    const factories = await $axios.$get('/factories/')
    return { factories }
  }
}
</script>
