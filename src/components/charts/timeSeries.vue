<template lang="pug">
.container
  .row.justify-center
    .col
      barChart(
      v-if="chartData"
      ref="barChart"
      :chartData='chartData'
      :text_color="light ? 'black': 'white'"
      :height="310")
  .row.justify-space-around
    div
      v-menu.primary(
        ref="periodmenu"
        dark
        v-model='periodmenu'
        :close-on-content-click='false'
        transition='scale-transition'
        max-width='180px')
        template(v-slot:activator='{ on }')
          .col.text-center
            v-chip(
              color="primary darken-3"
              @click='periodmenu = true') {{ params.period_size }}
            .overline Dias
        .container.primary.justify-center
          .row.justify-center
            .col.text-center
              v-text-field(
              min="1"
              label="Tamaño de los periodos"
              suffix="dias"
              type="number"
              v-model="params.period_size")
          .row.justify-space-around
            v-btn(color='red' x-small  @click='periodmenu = false') Cancelar
            v-btn(color='green' x-small  @click='$refs.periodmenu.save(params)') OK

    div
      DaySelect(
        desc="inicio"
        :max="params.end"
        :txtfilter="readable" v-model="params.begin")

      DaySelect(
        desc="final"
        :min="params.begin"
        :txtfilter="readable" v-model="params.end")

</template>
<script>
import moment from 'moment'
import barChart from './barChart'
import { readableDate, SSDATE_FORMAT, simpleRangeMini } from '@/components/utils'

moment.locale('es')
export default {
  components: {
    barChart
  },
  filters: {
    readableDate,
    smaldate (val) {
      return moment(val).format('d-m-Y')
    },
    readable (val) {
      return moment(val).format('dddd, DD MMMM YYYY')
    }
  },
  props: [
    'day_results',
    'dataname',
    'light'
  ],
  data () {
    return {
      labels: [],
      values: [],
      chartData: null,
      periodmenu: false,
      beginmenu: false,
      endmenu: false,
      params: {
        end: moment().toISOString(),
        begin: moment().subtract(1, 'months').toISOString(),
        period_size: 7
      }
    }
  },
  watch: {
    params: {
      deep: true,
      immediate: true,
      handler: 'dispatchParams'
    },
    day_results: {
      deep: true,
      immediate: true,
      handler (val) {
        if (!val) return
        if (!val.val_in_periods) return
        val = val.val_in_periods
        const self = this

        let labels = []
        let values = []
        for (let i = 0; i < val.length; i++) {
          const dia = val[i]
          Object.entries(dia).forEach(([key, value]) => {
            labels.push(self.filterLabels(key))
            values.push(value)
          })
        }
        this.chartData = {
          labels: labels,
          datasets: [
            {
              label: this.dataname,
              backgroundColor: '#F27023',
              data: values
            }
          ]
        }
        if (this.$refs.barChart) {
          this.$refs.barChart.render()
        }
      }
    }
  },
  mounted () {
    this.dispatchParams()
  },
  methods: {
    readable (val) {
      return moment(val).format('dddd, DD MMMM YYYY')
    },
    rerender () {
      if (this.$refs.barChart) this.$refs.barChart.render()
    },
    dispatchParams () {
      let params = { ...this.params }
      params.begin = moment(params.begin).format('Y-MM-DD')
      params.end = moment(params.end).format('Y-MM-DD')
      this.$emit('input', params)
    },
    filterLabels (label) {
      const FORMAT = 'DD-MMM YY'
      let d = label.split('-')

      let b = moment(d[0], 'DD/MM/YY')
      let e = moment(d[1], 'DD/MM/YY')
      return simpleRangeMini(b, e)
    }
  }
}
</script>

<style>
  .small {
    max-width: 600px;
    margin:  150px auto;
  }
</style>
