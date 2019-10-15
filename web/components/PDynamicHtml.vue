<script>
export default {
  props: {
    content: {
      type: String,
      required: true
    }
  },
  render(createElement, ctx) {
    return createElement({
      template: `<div>${this.content}</div>`
    })
  }
}
</script>
