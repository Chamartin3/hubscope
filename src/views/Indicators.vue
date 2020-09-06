<template lang="pug">
.container
  .justify-space-around
    IndicatorCard(v-for="item in items" :indicator="item")
  .col-md-4
    MetricList

</template>
<script>
import iteratorList from '@/layouts/templates/Lists/iteratorList.js'
import IndicatorCard from '@/components/indicators/MiniCard.vue'
import MetricList from '@/components/metrics/List.vue'

export default {
  name: 'Indicadores',
  components: {
    IndicatorCard,
    MetricList
  },
  mixins: [iteratorList],
  data () {
    return {
      modelName: 'indicator',
      listMethod: 'list'
    }
  }
}
</script>
