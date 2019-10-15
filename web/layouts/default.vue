<template>
  <div>
    <nav>
      <ul>
        <li><nuxt-link :to="{ name: 'index' }">главная</nuxt-link></li>
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
