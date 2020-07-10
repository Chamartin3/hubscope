<template lang='pug'>
.container.mb-5.fluid.fill-height.primary.darken-2
  .row.justify-space-around
    .overline.white--text {{ goal | period }}
    .col-12.col-md-3.text-center
      .row.justify-center
        Completation(
        :id="goal.id"
        :completation="goal.completed"
        )
        Status.mx-3(
        :indicatorname="goal.indicatorname"
        :status="goal.status")
  .row.white--text
    .col
      .overline
        h3 Avance de meta
  .row
    .col.col-xs-12
      v-progress-linear(
        :value='(goal.acomplishment)*100' 
        color='secondary' 
        height='20')
        template(v-slot='{ value }')
          strong {{ Math.ceil(value) }}%
  .row.white--text
    .col
      .overline
        h3 Reportes Enviados
  .row
    .col.col-xs-12
      v-progress-linear(
        :value='goal.report_rate' 
        color='secondary' 
        height='20')
        template(v-slot='{ value }')
          strong {{ Math.ceil(value) }}%
  .row
    trendChart(
    :results="goal.chart", 
    :expected="goal.expected", 
    :goal="goal.goal", 
    :dataname="goal.indicatorname" 
    )
      
    //- .d-inline.mr-2.ma-2

      
    //- .col-md-4.col-sm-12
</template>
<script>''
import { period } from '@/components/utils'
import Status from './Status'
import Completation from './Completation'
import trendChart from '@/components/charts/acumulado'
export default {
  name: 'Goal',
  props: ['goal'],
  components: { Status, trendChart, Completation },
  filters: { period }

}
</script>