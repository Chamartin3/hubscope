<template lang='pug'>
.container(fluid).white--text.primary.darken-1
  v-select(
    dark
    label="Status de reporte"
    :items="items", 
    v-model="value")
    template( #selection="{ item }")
      reportStatus(v-if="value" :status="value")
</template>
<script>
import reportStatus from '../Status'
import { Statuses } from '../utils'
export default {
  name: 'StatusSelect',
  components:{reportStatus},
  data() {
    return {
      value: null,
      items: Object.keys(Statuses),
    }
  },
  watch: {
    value(val){
      this.$emit('input',val)
    },   
  }
}
</script>