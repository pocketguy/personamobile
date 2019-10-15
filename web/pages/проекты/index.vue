<template>
  <div>
    <h1>{{ title }}</h1>
    <ul>
      <li v-for="project of projects" :key="project.id">
        {{ project.name }}
        <nuxt-link
          :to="{ name: 'проекты-slug', params: { slug: project.slug } }"
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
      title: 'Проекты'
    }
  },
  async asyncData({ $axios }) {
    const projectsPage = await $axios.$get('/projects/')
    projectsPage.projects = projectsPage.results
    return projectsPage
  },
  head() {
    return {
      title: this.title
    }
  }
}
</script>
