<template lang="pug">
v-card.blue-grey.lighten-5
  header.text-center.blue-grey.lighten-4.py-2
    strong {{ title }}

  .text-center.primary.py-1(v-if="sub")
    .overline.white--text {{ sub }}
  slot
</template>
<script>
export default {
  props: [
    'title',
    'sub'
  ]
}
</script>
