<template lang="pug">
.container
  .row.justify-center(v-resize="onResize")
    .col
      trendChart(
      v-if="chartData"
      :chartData='chartData'
      ref="trendChart"
      :height="310")
</template>
<script>
import trendChart from './trendChart'
import { filterLabels } from '@/components/utils'
export default {
  name: 'TrendChart',
  components: { trendChart },
  props: [
    'results',
    'expected',
    'goal',
    'intermediate',
    'dataname' ],
  data () {
    return {
      chartData: null
    }
  },
  watch: {
    'this.$refs.trendChart': {
      immediate: true,
      handler (val) {
        if (val) val.render()
      }
    },
    results: {
      handler: 'processResults'
    }
  },
  mounted () {
    this.onResize()
  },
  methods: {
    onResize () {
      this.processResults(this.results)
      if (this.$refs.trendChart) this.$refs.trendChart.render()
    },
    filterLabels,
    computeTrendline (end, periods, begin = 0) {
      let total = end - begin
      let size = total / (periods.length) - 1
      let jumps = []
      let acumulator = begin
      for (let i = 0; i < periods.length; i++) {
        jumps.push(acumulator)
        acumulator = acumulator + size
      }
      return jumps
    },
    computeData (chartData) {
      const self = this
      let labels = []
      let values = []
      for (let i = 0; i < chartData.length; i++) {
        const dia = chartData[i]
        Object.entries(dia).forEach(([key, value]) => {
          labels.push(self.filterLabels(key))
          values.push(value)
        })
      }
      return [values, labels ]
    },
    goalLine (labels) {
      let line = []
      for (let i = 0; i < labels.length; i++) {
        line.push(this.goal)
      }
      return line
    },
    intermediateLine (labels) {
      let line = []
      for (let i = 0; i < labels.length; i++) {
        line.push(this.intermediate)
      }
      return line
    },
    processResults (val) {
      if (!val) return
      let datatuple = this.computeData(val)
      let labels = datatuple[1]
      let values = datatuple[0]
      let begin = values[0] ? values[0] : 0
      let trendline = this.computeTrendline(this.expected, labels, begin)
      let goalLine = this.goalLine(labels)
      let intermediateLine = this.intermediateLine(labels)

      let datasets = []
      // Tendencia
      const Trend = {
        type: 'line',
        label: 'Tendencia',
        data: trendline,
        borderColor: '#25AAE1'
      }
      datasets.push(Trend)

      const Goal = {
        type: 'line',
        label: 'Meta del periodo',
        data: goalLine,
        borderColor: '#4CAF50'
      }
      datasets.push(Goal)
      if (this.intermediate) {
        const Intermediate = {
          type: 'line',
          label: 'Meta intermedia',
          data: intermediateLine,
          borderColor: '#ffff00'
        }
        datasets.push(Intermediate)
      }
      const Barras = {
        type: 'bar',
        label: this.dataname,
        data: values,
        backgroundColor: 'rgba(242, 112, 35,0.8)'
      }
      datasets.push(Barras)
      this.chartData = {
        labels: labels,
        datasets: datasets
      }
    }
  }
}
</script>
