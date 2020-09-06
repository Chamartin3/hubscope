<template lang="pug">
LightCard(
  title="Reportes por entregar"
  :sub="sumary.total + ' reportes por entregar'"
  )

  reportForm(ref="reportForm")
  .row.justify-space-around(v-if="sumary.total>0")
    .col.text-center
      v-progress-circular.white-text(
        :size="80"
        :width="10"
        :value="sumary.atrasada/sumary.total*100"
        color="red"
        ) {{ sumary.atrasada/sumary.total*100 }} %
      p.text-uppercase.font-weight-light.caption.px-3
        | Reportes Atrasados
    .col.text-center
      v-progress-circular.white-text(
        :size="80"
        :width="10"
        :value="sumary.esperando/sumary.total*100"
        color="orange"
        ) {{ sumary.esperando/sumary.total*100 }} %
      p.text-uppercase.font-weight-light.caption.px-3
        | Reportes por entregar
    .col.text-center
      v-progress-circular.white-text(
        :size="80"
        :width="10"
        :value="sumary.abierta/sumary.total*100"
        color="yellow darken-2"
        ) {{ sumary.abierta/sumary.total*100 }} %
      p.text-uppercase.font-weight-light.caption.px-3
        | Reportes en espera
  .container(v-if="sumary.total>0")
    .row(v-for="report in items")
      .col
        v-card
          .container
            .row.justify-space-between.mx-1
              .col
                h3 {{ report.metric.name }}
                strong.text-uppercase.caption
                  | {{ report | simpleperiod }}
              reportStatus.align-end(:status="report.status")
            .row.justify-space-around
              .col.text-center
                .overline
                  | Fecha esperada de reporte
                .overline
                  | Despues del {{ report.end | date }}
                .overline
                  | Antes del {{ report.deadline | date }}
              .col.text-end
                v-btn.primary.dark(
                  :disabled="report.status === 'esperando'"
                  small
                  @click="$emit('editReport', report)" ) Llenar

</template>
<script>
import reportStatus from './Status'
import reportForm from './Form'
import { base, serverSide } from '#/Lists'
import { Filters } from './utils'

export default {
  name: 'PendingReports',
  components: { reportStatus, reportForm },
  mixins: [ base, serverSide, Filters ],
  data () {
    return {
      modelName: 'report',
      listMethod: 'allPending',
      sumary: {},
      pagination: {},
      params: {
        per_page: 30
      }
    }
  },
  mounted () {
    this.resultActions.push(this.extractSumary)
  },
  methods: {
    extractSumary (response) {
      this.items = response.results
      this.sumary = response.sumary
      this.pagination = response.pagination
      return response.results
    }
  }

}
</script>
