<template>
  <div class="main">
    <p-logo class="logo" />
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
  max-height: 100px;
  max-width: 100%;
}
</style>
