<template>
  <div>
    <nav>
      <ul>
        <li><nuxt-link :to="{ name: 'index' }">главная</nuxt-link></li>
        <li><nuxt-link :to="{ name: 'фабрики' }">фабрики</nuxt-link></li>
        <li><nuxt-link :to="{ name: 'новости' }">новости</nuxt-link></li>
      </ul>
    </nav>
    <nuxt />
  </div>
</template>
