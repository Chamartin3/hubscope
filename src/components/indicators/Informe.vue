<template lang='pug'>
.container.justify-space-around
  .row.justify-center
    .col.text-center.overline.mx-2(v-if="params")
      h3 Reportes desde
        | &nbsp;
        | {{ params.begin |  readableDate }} 
        | &nbsp;
        | hasta
        | &nbsp;
        | {{ params.end | readableDate }}
  .row(v-resize="onResize")
    .col-12.col-sm-8
      .ma-3
        timeSeries(
        ref="timeSeries"
        v-model="params"
        :dataname="indicatorname"
        :day_results="instance")
    .col-12.col-sm-4.text-center(v-if="instance")
      v-tooltip(top)
        template(v-slot:activator='{ on }')
          .ma-3( v-on='on')
            v-progress-circular.white-text(
            :size="100"
            :width="15"
            :value="instance.delivery_rate"
            color="secondary"
            ) {{ instance.delivery_rate }} %
            .overline Dias reportados
            .overline en este periodo
        span 
          | {{ instance.reported_days }} dias reportados de {{ instance.days_to_report }} dias a reportar
      .ma-3
        .display-3
          p.font-weight-thin {{ instance.total_reports }}
        .overline Reportes Enviados
        .overline en este periodo

          

</template>
<script>
import moment from 'moment'
import { readableDate } from '@/components/utils'
import timeSeries from '../charts/timeSeries.vue'
export default {
  name: 'InformeIndicator',
  props: ['indicator','indicatorname'],
  components: { timeSeries },
  data() {
    return {
      Model: this.$django.models.indicator,
      method: 'inform',
      instance: null,
      loading: false,
      // end: moment(),
      // begin: moment().subtract(1,'months'),
      // period_size:7,
      params:null
    }
  },
  watch: { 
    indicator: { handler: 'getInstance' },
    params: { handler: 'getInstance' },
  },
  filters: {
    readableDate
  },
  methods:{
    onResize(){
      if(this.$refs.timeSeries) this.$refs.timeSeries.rerender()
    },
    async getInstance () {
      if (!this.params) return
      this.loading = true
      this.instance = await this.Model[this.method](
        this.indicator, 
        this.params)
      this.loading = false
    }
  },
  mounted(){   
   this.getInstance() 
   this.onResize()
  }
}
</script>