<template lang='pug'>
v-card.primary.darken-1
  header.text-center.primary.white--text
    .col
      .display-1 {{ goal.indicatorname }}
      .overline.white--text {{ goal | period }}

  .container
    .row.justify-space-around
      .col-12.col-md-3.text-center
        .row.justify-center
          Completation(
          @completed="goal.completed=true"
          @reopened="goal.reopened=false"
          :id="goal.id"
          :completation="goal.completed"
          )
          Status.mx-3(
          :indicatorname="goal.indicatorname"
          :status="goal.status")
    .row.white--text
      .col
        LevelBar(:logro="goal.goal", :intermedio="goal.fail.split(',')[0]")
    .row
      .col.white--text.text-center
        v-tooltip(top)
          template(v-slot:activator='{ on }')
            .ma-3( v-on='on')
              v-progress-circular.white-text(
              :size="100"
              :width="15"
              :value="goal.acomplishment * 100"
              color="secondary"
              ) {{ goal.acomplishment * 100  }} %
              .overline Avance de Meta
      .col.white--text.text-center
        v-tooltip(top)
          template(v-slot:activator='{ on }')
            .ma-3( v-on='on')
              v-progress-circular.white-text(
              :size="100"
              :width="15"
              :value="goal.report_rate"
              color="secondary"
              ) {{ goal.report_rate }} %
              .overline Dias reportados
              .overline en este periodo
    .row
      .col
        trendChart(
          :results="goal.chart",
          :expected="goal.expected",
          :goal="goal.goal",
          :intermediate="goal.fail.split(',')[0]"
          :dataname="goal.indicatorname"
        )
    .row.justify-center.text-center
      DeleteConfirmation(
      model="goal"
      ref="DeleteConf"
      customMessage="¿Desea eliminar esta meta?"
      @success="$emit('deletedGoal')")
      v-btn( v-django-groups="'Admin'" large color="red" text @click="$refs.DeleteConf.open(goal.id)" )
        | Eliminar Meta
      //- .d-inline.mr-2.ma-2

    //- .col-md-4.col-sm-12
</template>
<script>''
import { period } from '@/components/utils'
import Status from './Status'
import Completation from './Completation'
import LevelBar from './LevelBar'
import trendChart from '@/components/charts/acumulado'
export default {
  name: 'Goal',
  components: { Status, trendChart, Completation, LevelBar },
  filters: { period },
  props: ['xgoal'],
  data () {
    return {
      goal: { ...this.xgoal }
    }
  }

}
</script>
