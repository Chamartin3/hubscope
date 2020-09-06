<template lang='pug'>
  v-select(
      :dark="dark"
      label="Metricas Reportadas"
      :items="items",
      item-text="name"
      item-value="name"
      v-model="value")
</template>
<script>

export default {
  name: 'ResportedMetricSelect',
  props: ['company', 'dark'],
  data () {
    return {
      value: null,
      items: []
    }
  },
  watch: {
    value (val) {
      if (val) this.$emit('input', val)
    }
  },
  mounted () {
    this.getItems()
  },
  methods: {
    async getItems () {
      if (!this.company) this.items = await this.$django.models.metric.all()
      else this.items = await this.$django.models.company.reportsByMetric(this.company)
    },
    reset () {
      this.value = null
    }
  }
}
</script>
