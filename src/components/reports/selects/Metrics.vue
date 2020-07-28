<template lang='pug'>
  v-select(
      dark
      label="Metricas Reportadas"
      :items="items", 
      item-text="name"
      item-value="name"
      v-model="value")
</template>
<script>

export default {
  name: 'resportedMetricSelect',
  props: ['company'],
  data() {
    return {
      value: null,
      items: []
    }
  },
  methods: {
    async getItems(){
      let model = this.$django.models.company
      this.items = await model.reportsByMetric(this.company)
    },
    reset() {
      this.value=null
    }
  },
  watch: {
    value(val){
      if(val) this.$emit('input',val)
    },   
  },
  mounted() {
    this.getItems()
  }
}
</script>