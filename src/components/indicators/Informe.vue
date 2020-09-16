<template lang='pug'>
.container.justify-space-around
  .row.justify-center
    //- .col.text-center.overline.mx-2(v-if="params")
  .row(v-resize="onResize")
    .col-12.col-sm-8
      v-card.blue-grey.lighten-5
        .container
          h3.overline.text-center(v-if="params") {{ params | rangoFechas }}
          //- Reportes desde
          //-   | &nbsp;
          //-   | {{ params.begin |  readableDate }}
          //-   | &nbsp;
          //-   | hasta
          //-   | &nbsp;
          //-   | {{ params.end | readableDate }}
          .ma-3
            timeSeries(
            ref="timeSeries"
            :light="true",
            v-model="params"
            :dataname="indicatorname"
            :day_results="instance")
    .col-12.col-sm-4.text-center(v-if="instance")
      v-card.blue-grey.lighten-5
        header.blue-grey.lighten-4.pa-2
          .overline Metricas utilizadas
        .container
          MetricCard(v-for="metric in metrics"
          :key="metric.id"
          :metric="metric")
      v-tooltip(top)
        template(v-slot:activator='{ on }')
          v-card.blue-grey.lighten-5( v-on='on')
            header.blue-grey.lighten-4.pa-2.mt-5
              .overline Dias reportados
              .overline en este periodo
            .container
              v-progress-circular.white-text(
              :size="100"
              :width="15"
              :value="instance.delivery_rate"
              color="secondary"
              ) {{ instance.delivery_rate }} %
        span
          | {{ instance.reported_days }} dias reportados de {{ instance.days_to_report }} dias a reportar
      v-card.blue-grey.lighten-5.mt-5
        header.blue-grey.lighten-4.pa-2
          .overline Reportes Enviados
          .overline en este periodo
        .container
          .display-3.font-weight-thin {{ instance.total_reports }}
          v-btn( color="secondary" text @click="$emit('period', params)" ) ver reportes

</template>
<script>
import moment from 'moment'
import { readableDate, simpleRange } from '@/components/utils'
import ReportsTable from '@/components/reports/Table'
import timeSeries from '../charts/timeSeries.vue'
import MetricCard from '@/components/metrics/Card.vue'
export default {
  name: 'InformeIndicator',
  components: { timeSeries, ReportsTable, MetricCard },
  filters: {
    readableDate
  },
  filters: {
    rangoFechas (item) {
      return simpleRange(item.begin, item.end)
    }
  },
  props: ['indicator', 'indicatorname', 'metrics'],
  data () {
    return {
      Model: this.$django.models.indicator,
      method: 'inform',
      instance: null,
      loading: false,
      // end: moment(),
      // begin: moment().subtract(1,'months'),
      // period_size:7,
      params: null,
      report_detail: null,
      report_table: false
    }
  },
  watch: {
    indicator: { handler: 'getInstance' },
    params: { handler: 'getInstance' }
  },
  mounted () {
    this.getInstance()
    this.onResize()
  },
  methods: {

    onResize () {
      if (this.$refs.timeSeries) this.$refs.timeSeries.rerender()
    },
    async getInstance () {
      if (!this.params) return
      this.loading = true
      this.instance = await this.Model[this.method](
        this.indicator,
        this.params)
      this.loading = false
    }
  }
}
</script>
