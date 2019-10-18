<template>
  <div class="main">
    <h1><p-logo class="logo" /></h1>
  </div>
</template>

<script>
import PLogo from '~/components/PLogo.vue'
export default {
  layout: 'empty',
  components: {
    PLogo
  },
  data() {
    return {
      title: 'Главная Страница'
    }
  },
  head() {
    return {
      title: this.title
    }
  }
}
</script>

<style scoped>
.main {
  height: calc(100vh - 66px);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.logo {
  height: 100px;
  max-width: 100%;
}
</style>
