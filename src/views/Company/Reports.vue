<template lang="pug">
.container.mb-5.fluid.fill-height.primary.darken-2
  .row
    .col
      ReportsTable(:company="instance.id")
    .col-md-4.col-sm-12
      PersonelList(:id="instance.id")

</template>
<script>
import PersonelList from '@/components/empresas/positions/List'
import ReportsTable from '@/components/reports/Table'
export default {
  name: 'ReportesRealizados',
  props:['instance'],
  components:{
    PersonelList,
    ReportsTable
  },
}
</script>
