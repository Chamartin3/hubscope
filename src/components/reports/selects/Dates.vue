<template lang='pug'>
.container
  .row.text-center.primary
    .col
     .overline
        h3 Rango de Fechas
  .row.text-center.primary.darken-1
    .col     
      DaySelect(
        desc="inicio"
        :max="end"
        :txtfilter="readable" 
        v-model="begin")
      DaySelect(
        desc="final"
        :min="begin"
        :txtfilter="readable" 
        v-model="end")

</template>
<script>
import moment from 'moment'
import {readableDate} from '@/components/utils'
export default {
  name: 'DayRangeSelect',
  data() {
    return {
      end: null,
      begin:null,
      range:{
        }
    }
  },
  methods: {
    readable(val) {
      if (val) return readableDate(val)
      else return 'Selecione fecha'
    }
  },
  watch: {
    end(val){
      console.log(val);
      
      let date = moment(val)
      this.$emit('inputend',this.end)
    },   
    begin(val){
      this.$emit('inputbegin',this.begin)
    }
  }

}
</script>