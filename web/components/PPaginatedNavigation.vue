<template>
  <ul>
    <li v-if="prevPage !== null">
      <nuxt-link
        :to="{
          name: routeName,
          params: { page: prevPage }
        }"
        >{{ prevPage }}</nuxt-link
      >
    </li>
    <li>{{ currentPage }}</li>
    <li v-if="nextPage !== null">
      <nuxt-link
        :to="{
          name: routeName,
          params: { page: nextPage }
        }"
        >{{ nextPage }}</nuxt-link
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
      validator: validateNumberOrNull
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
      validator: validateNumberOrNull
    },
    routeName: {
      required: true,
      type: String
    }
  }
}
</script>
