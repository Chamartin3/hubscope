<template lang='pug'>
    .row.text-center.primary.darken-1.white--text 
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
      range: {}
    }
  },
  methods: {
    readable(val) {
      if (val) return readableDate(val)
      else return 'Selecione fecha'
    },
    resetBegin () { this.begin = null },
    resetEnd () { this.end = null }
  },
  watch: {
    end(val){
      if(val) this.$emit('inputend',this.end)
    },   
    begin(val){
      if(val) this.$emit('inputbegin',this.begin)
    }
  }

}
</script>