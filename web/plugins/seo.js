export default ({ req, route }, inject) => {
  inject('seoHead', (title, description, image, imageAlt) => {
    let url = null
    if (process.server) {
      const proto = req.headers['x-forwarded-proto']
      const host = req.headers['x-forwarded-host']
      const port = req.headers['x-forwarded-port']
      url = `${proto}://${host}:${port}${route.fullPath}`
    } else {
      url = window.location.href
    }
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
