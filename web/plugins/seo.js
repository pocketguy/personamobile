export default ({ env, route }, inject) => {
  inject('seoHead', (title, description, image, imageAlt) => {
    const url = `${env.baseUrl}${route.fullPath}`
    return {
      title,
      meta: [
        // hid is used as unique identifier. Do not use `vmid` for it as it will not work
        {
          hid: 'description',
          name: 'description',
          content: description
        },
        // Open Graph
        {
          name: 'og:title',
          content: title
        },
        {
          name: 'og:description',
          content: description
        },
        {
          name: 'og:type',
          content: 'website'
        },
        {
          name: 'og:url',
          content: url
        },
        {
          name: 'og:image',
          content: image
        },
        // Twitter Card
        {
          name: 'twitter:card',
          content: 'summary'
        },
        // { name: 'twitter:site', content: '@personamobile.ru' },
        {
          name: 'twitter:title',
          content: title
        },
        {
          name: 'twitter:description',
          content: description
        },
        { name: 'twitter:image', content: image },
        { name: 'twitter:image:alt', content: imageAlt }
      ]
    }
  })
}
