<template>
  <div>
    <nav>
      <ul>
        <li>
          <nuxt-link :to="{ name: 'index_page' }">
            <p-logo class="logo" />
          </nuxt-link>
        </li>
        <li><nuxt-link :to="{ name: 'фабрики' }">фабрики</nuxt-link></li>
        <li><nuxt-link :to="{ name: 'проекты' }">проекты</nuxt-link></li>
        <li>
          <nuxt-link
            :to="{
              name: 'новости-страница-page',
              params: { page: 1 }
            }"
            >новости</nuxt-link
          >
        </li>
      </ul>
    </nav>
    <nuxt />
  </div>
</template>

<script>
import PLogo from '~/components/PLogo.vue'
export default {
  components: {
    PLogo
  }
}
</script>

<style scoped>
.logo {
  width: 200px;
}
</style>
