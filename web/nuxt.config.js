import axios from 'axios'

export default {
  mode: 'universal',
  /*
   ** Headers of the page
   */
  head: {
    titleTemplate: '%s - Persona Mobile',
    title: 'Persona Mobile',
    htmlAttrs: {
      lang: 'ru'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: 'Представительство итальянаских фабрик в России'
      }
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }]
  },
  /*
   ** Customize the progress-bar color
   */
  loading: { color: '#fff' },
  /*
   ** Global CSS
   */
  css: [],
  /*
   ** Plugins to load before mounting the App
   */
  plugins: [],
  /*
   ** Nuxt.js dev-modules
   */
  buildModules: [
    // Doc: https://github.com/nuxt-community/eslint-module
    '@nuxtjs/eslint-module'
  ],
  /*
   ** Nuxt.js modules
   */
  modules: [
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    '@nuxtjs/sitemap'
  ],
  /*
   ** Axios module configuration
   ** See https://axios.nuxtjs.org/options
   */
  axios: {
    baseURL: process.env.AXIOS_BASE_URL,
    browserBaseURL: process.env.AXIOS_BROWSER_BASE_URL
  },
  sitemap: {
    routes: async () => {
      const mapping = {
        factories: 'фабрики',
        posts: 'новости',
        projects: 'проекты'
      }

      const result = []
      for (const k in mapping) {
        const v = mapping[k]
        const { data } = await axios.get(`${process.env.AXIOS_BASE_URL}${k}/`)
        data.forEach((e) => {
          result.push({
            url: `/${v}/${e.slug}`,
            lastmod: e.updated_at
          })
        })
      }
      return result
    }
  },
  /*
   ** Build configuration
   */
  build: {
    /*
     ** You can extend webpack config here
     */
    extend(config, ctx) {
      config.resolve.alias.vue = 'vue/dist/vue.common'
    }
  }
}
