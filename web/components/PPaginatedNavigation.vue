<template>
  <ul>
    <li v-if="showLeftArrow">
      <nuxt-link
        :to="{
          name: routeName,
          params: { page: 1 }
        }"
        >Первая страница</nuxt-link
      >
    </li>
    <li v-for="page of pagesRangeWithinWidth" :key="page">
      <nuxt-link
        v-if="page !== currentPage"
        :to="{
          name: routeName,
          params: { page: page }
        }"
        >{{ page }}</nuxt-link
      >
      <div v-else>{{ page }}</div>
    </li>
    <li v-if="showRightArrow">
      <nuxt-link
        :to="{
          name: routeName,
          params: { page: totalPages }
        }"
        >Последняя страница</nuxt-link
      >
    </li>
  </ul>
</template>

<script>
const validateNumberOrNull = (prop) => typeof prop === 'number' || prop === null
export default {
  props: {
    currentPage: {
      required: true,
      validator: Number
    },
    prevPage: {
      required: true,
      validator: validateNumberOrNull
    },
    nextPage: {
      required: true,
      validator: validateNumberOrNull
    },
    totalPages: {
      required: true,
      validator: Number
    },
    routeName: {
      required: true,
      type: String
    },
    width: {
      required: true,
      type: Number,
      default: 4
    }
  },
  computed: {
    showLeftArrow() {
      return this.currentPage > this.width
    },
    showRightArrow() {
      return this.currentPage < this.totalPages - this.width
    },
    pagesRangeWithinWidth() {
      const left = Math.max(1, this.currentPage - this.width)
      const right = Math.min(this.totalPages, this.currentPage + this.width)
      return [...Array(right - left + 1).keys()].map((e) => e + left)
    }
  }
}
</script>
