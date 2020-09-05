<template lang="pug">
.container.mb-5.fluid.fill-height
  .row.justify-center
    .col
      StatusSelect(v-model="pfilters.status")


  .row.justify-center
    .col
      ReportsTable(ref="Table")

</template>
<script>
import ReportsTable from '@/components/reports/Table'
import StatusSelect from '@/components/reports/selects/Status'
export default {
  name: 'ReportesProgramados',
  components:{ ReportsTable, StatusSelect },
  data () {
    return {
      pfilters: {}
    }
  },
  watch: { 
    pfilters (val) {
      if (val && this.$refs.Table) {
        this.$refs.Table.setPropertyFilters(val)
      }
    }
  }
}
</script>
