<template>
  <div>
    <h1>{{ title }}</h1>
    <h2><nuxt-link :to="{ name: 'фабрики' }">фабрики</nuxt-link></h2>
    <h2><nuxt-link :to="{ name: 'проекты' }">проекты</nuxt-link></h2>
    <h2>
      <nuxt-link
        :to="{
          name: 'новости-страница-page',
          params: { page: 1 }
        }"
        >новости</nuxt-link
      >
    </h2>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: 'Persona Mobile'
    }
  },
  head() {
    return {
      title: this.title
    }
  }
}
</script>
