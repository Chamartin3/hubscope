<template lang="pug">
.container.mb-5.fluid.fill-height.primary.darken-2
  .row.justify-center
    .col
      List(:company="instance")

</template>
<script>
import List from '@/components/indicators/List.vue'
export default {
  props: ['instance'],
  name: 'Indicadores',
  components:{ List },
}
</script>
