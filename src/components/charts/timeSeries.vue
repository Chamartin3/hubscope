<template lang="pug">
.container
  .row.justify-center
    .col
      barChart(
      v-if="chartData"
      ref="barChart"
      :chartData='chartData' 
      :height="310")
  .row.justify-space-around
   
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
moment.locale('es');
import barChart from "./barChart";
import {readableDate, SSDATE_FORMAT} from "@/components/utils"
export default {
  props: [
    'day_results', 
    'dataname'
  ],
  components: {
    barChart
  },
  data () {
    return {
      labels: [],
      values:[],
      chartData: null,
      periodmenu:false,
      beginmenu:false,
      endmenu:false,
      params:{
        end: moment().toISOString(),
        begin: moment().subtract(1,'months').toISOString(),
        period_size:7,
      }
    }
  },
  filters: {
    readableDate,
    smaldate(val){
      return moment(val).format('d-m-Y')
    },
    readable(val){
      return moment(val).format('dddd, DD MMMM YYYY')
    }
  },
  methods:{
    readable(val){
      return moment(val).format('dddd, DD MMMM YYYY')
    },
    rerender(){
      if (this.$refs.barChart) this.$refs.barChart.render()
    },
    dispatchParams(){
      let params = { ...this.params }
      params.begin = moment(params.begin).format("Y-MM-DD")
      params.end = moment(params.end).format("Y-MM-DD")
      this.$emit('input', params)
    },
    filterLabels(label){

      const FORMAT = "DD-MMM YY"
      let d = label.split('-')

      let b = moment(d[0], 'DD/MM/YY').format(FORMAT)
      let e = moment(d[1], 'DD/MM/YY').format(FORMAT) 
      
      if (b==e) return `${b}`
      return `${b} a ${e}`
    }
  },
  mounted(){
    this.dispatchParams()
  },
  watch: { 
    params:{
      deep: true,
      immediate: true,
      handler: 'dispatchParams'
    },
    day_results:{
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
          const dia = val[i];
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
  }
}
</script>

<style>
  .small {
    max-width: 600px;
    margin:  150px auto;
  }
</style>