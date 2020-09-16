<template lang="pug">
v-card(:width="width" ).blue-grey.lighten-5
  header.text-center.blue-grey.lighten-4.py-2
    strong.ma-2 {{ title }}

  .text-center.primary.py-1(v-if="sub")
    .overline.white--text {{ sub }}
  slot
</template>
<script>
export default {
  props: {
    title: {
      type: String,
      default: null
    },
    sub: {
      type: String,
      default: null
    },
    width: {
      type: String,
      default: null
    }

  }
}
</script>
