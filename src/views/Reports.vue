<template lang="pug">
.container.mb-5.fluid.fill-height
  .row.justify-center
    .col
      ReportsTable

</template>
<script>
import ReportsTable from '@/components/reports/Table'
export default {
  name: 'Reportes Programados',
  components:{ ReportsTable },
}
</script>
