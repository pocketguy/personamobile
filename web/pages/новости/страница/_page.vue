<template>
  <div>
    <h1>{{ title }}</h1>
    <ul>
      <li v-for="post of posts" :key="post.id">
        {{ post.title }}
        <nuxt-link
          :to="{
            name: 'новости-slug',
            params: { slug: post.slug }
          }"
          >подробнее</nuxt-link
        >
      </li>
    </ul>
    <p-paginated-navigation
      :current-page="current_page"
      :prev-page="previous_page_number"
      :next-page="next_page_number"
      :total-pages="total_pages"
      :route-name="'новости-страница-page'"
    />
  </div>
</template>

<script>
import PPaginatedNavigation from '~/components/PPaginatedNavigation.vue'
export default {
  components: {
    PPaginatedNavigation
  },
  data() {
    return {
      title: 'Новости'
    }
  },
  async asyncData({ $axios, route }) {
    const page = encodeURIComponent(route.params.page)
    const postsPage = await $axios.$get(`/posts/?page=${page}`)
    postsPage.posts = postsPage.results
    return postsPage
  },
  head() {
    return {
      title: this.title
    }
  }
}
</script>
