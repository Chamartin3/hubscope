<template lang="pug">
div
  .row.justify-space-around(v-if="!loading")
    GeneralPagination(
      color="secondary"
      v-model="params.page",
      :names="{singular:'indicador', plural:'indicadores'}"
      :pagination="pagination")
  .row.justify-space-around(v-if="loading")
    LoadingComponent
  .row.justify-space-around
    IndicatorCard(v-for="indicator in items" :indicator="indicator")
</template>
<script>
import iteratorList from '@/layouts/templates/Lists/iteratorList.js'
import IndicatorCard from '@/components/indicators/MiniCard.vue'
import MetricTable from '@/components/metrics/Table.vue'

export default {
  name: 'IndicadoresList',
  components: {
    IndicatorCard,
    MetricTable
  },
  mixins: [iteratorList],
  props: {
    globalFilter: {
      type: Object,
      default: () => { return {} }
    }
  },
  data () {
    return {
      modelName: 'indicator',
      listMethod: 'list',
      params: {
        datatable_filters: {
          ...this.globalFilter
        }
      }
    }
  },
  mounted () {
    this.paramFilters.push(this.applyGlobalFilter)
  },
  methods: {
    applyGlobalFilter (params, oldp) {
      console.log(this.generalFilter)
      for (const prop in this.generalFilter) {
        params.datatable_filters[prop] = this.generalFilter[prop]
      }
    }
  }
}
</script>
