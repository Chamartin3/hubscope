<template lang="pug">
LightCard(
  title="Reportes por entregar"
  )

  reportForm(ref="reportForm" @edited="listObjects")
  .row.justify-space-around(v-if="sumary.total>0")
    .col.text-center
      v-progress-circular.white-text(
        :size="90"
        :width="10"
        :value="perc(sumary,'atrasada')"
        color="red"
        ) {{ perc(sumary,'atrasada') }} %
      p.text-uppercase.font-weight-light.caption.px-3
        | Reportes Atrasados
    .col.text-center
      v-progress-circular.white-text(
        :size="90"
        :width="10"
        :value="perc(sumary,'abierta')"
        color="green darken-2"
        ) {{ perc(sumary,'abierta') }} %
      p.text-uppercase.font-weight-light.caption.px-3
        | Reportes por entregar
    .col.text-center
      v-progress-circular.white-text(
        :size="90"
        :width="10"
        :value="perc(sumary,'esperando')"
        color="orange"
        ) {{perc(sumary,'esperando') }} %
      p.text-uppercase.font-weight-light.caption.px-3
        | Reportes en espera

  .row.justify-space-around(v-if="sumary.total>0")
    GeneralPagination(
      circle
      color="secondary"
      v-model="params.page",
      :names="{singular:'reporte por entregar', plural:'reportes por entregar'}"
      :pagination="pagination")
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
import iteratorList from '@/layouts/templates/Lists/iteratorList.js'
import { Filters } from './utils'
export default {
  name: 'PendingReports',
  components: { reportStatus, reportForm },
  mixins: [ iteratorList, Filters ],
  data () {
    return {
      modelName: 'report',
      listMethod: 'allPending',
      sumary: {},
      params: {
        per_page: 3
      }
    }
  },
  mounted () {
    // this.resultActions.push(this.extractSumary)
  },
  methods: {
    setPagination (response) {
      if (response && response.pagination) {
        this.pagination = response.pagination
        this.sumary = response.sumary
        return response.results
      }
      return response
    },
    perc (sumary, attr) {
      let num = sumary[attr] / sumary.total
      return (num * 100).toFixed(2)
    },
    reported () {
      console.log('reportes')
      this.listObjects()
    }
  }

}
</script>
