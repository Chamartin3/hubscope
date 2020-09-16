<template lang="pug">
.container
  .row.text-center.justify-center
    InficatorForm(
      @created="$refs.IndicatorList.listObjects()"
      ref="IndicatorForm")
  .row
    .col-md-8.text-center
      v-btn( text small color="secondary" @click="$refs.IndicatorForm.open()" ) Crear Indicador
      IndicatorList(ref="IndicatorList")
    .col-md-4
      MetricTable

</template>
<script>
import iteratorList from '@/layouts/templates/Lists/iteratorList.js'
import IndicatorCard from '@/components/indicators/MiniCard.vue'
import IndicatorList from '@/components/indicators/List.vue'
import MetricTable from '@/components/metrics/Table.vue'
import InficatorForm from '@/components/indicators/Form.vue'

export default {
  name: 'Indicadores',
  components: {
    IndicatorCard,
    MetricTable,
    IndicatorList,
    InficatorForm
  }
}

</script>
