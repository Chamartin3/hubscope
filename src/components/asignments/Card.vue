<template lang='pug'>
v-card.pointer(dark color='primary lighten-1')
  .container
    .row.text-center
      .col
        .display-1 {{ asignment.name }}
    hr
    .row.text-center
      .col
</template>
<script>
export default {
  name: 'asignmentCard',
  props:['asignment']
}
</script>