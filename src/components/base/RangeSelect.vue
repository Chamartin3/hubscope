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
      .caption.red--text(v-if="errors && errors.begin") {{ errors.begin }}
      DaySelect(
        desc="final"
        :min="begin"
        :txtfilter="readable" 
        v-model="end")
      .caption.red--text(v-if="errors && errors.end") {{ errors.end }}

</template>
<script>
import moment from 'moment'
import {readableDate} from '@/components/utils'
export default {
  props:['errors'],
  name: 'DayRangeSelect',
  data() {
    return {
      end: null,
      begin:null,
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
      let date = moment(val)
      this.$emit('inputend',this.end)
      this.$emit('input',{
        end:this.end,
        begin:this.begin
      })      
    },   
    begin(val){
      this.$emit('inputbegin',this.begin)
      this.$emit('input',{
        end:this.end,
        begin:this.begin
      })
    }
  }

}
</script>