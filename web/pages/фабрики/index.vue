<template>
  <div>
    <h1>{{ title }}</h1>
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
  data() {
    return {
      title: 'Фабрики'
    }
  },
  async asyncData({ $axios }) {
    const factoriesPage = await $axios.$get('/factories/')
    factoriesPage.factories = factoriesPage.results
    return factoriesPage
  },
  head() {
    return {
      title: this.title
    }
  }
}
</script>
