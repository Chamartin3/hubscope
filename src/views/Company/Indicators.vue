<template lang="pug">
.container
  .row.justify-center
    .col
      IndicatorList(:globalFilter="{'company__id':instance.id}")

</template>
<script>
import IndicatorList from '@/components/indicators/List.vue'
import Card from '@/components/indicators/Card.vue'
import iteratorList from '@/layouts/templates/Lists/iteratorList.js'
export default {
  name: 'Indicadores',
  components: { IndicatorList },
  props: ['instance']
}
</script>
