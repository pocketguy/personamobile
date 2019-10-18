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
  plugins: ['~/plugins/seo.js'],
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
  axios: {},
  sitemap: {
    routes: async () => {
      const mapping = {
        factories: {
          urlPart: 'фабрики',
          paginate: false
        },
        posts: {
          urlPart: 'новости',
          paginate: true
        },
        projects: {
          urlPart: 'проекты',
          paginate: false
        }
      }

      const result = []

      for (const k in mapping) {
        const urlPart = mapping[k].urlPart
        const paginate = mapping[k].paginate

        let url = null

        if (paginate) {
          url = `${process.env.API_URL}${k}`
        } else {
          url = `${process.env.API_URL}${k}/?page_size=999999`
        }

        const { data } = await axios.get(url)

        data.results.forEach((e) => {
          result.push({
            url: `/${urlPart}/${e.slug}`,
            lastmod: e.updated_at
          })
        })

        if (paginate) {
          for (let i = 1; i <= data.total_pages; i++) {
            result.push(`/${urlPart}/страница/${i}`)
          }
        }
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
