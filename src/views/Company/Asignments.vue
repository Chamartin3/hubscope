<template lang="pug">
.container.mb-5.fluid.fill-height.primary.darken-2
  .row.justify-center
    .col
      AsignmentsList
    .col-md-4.col-sm-12
      MetricasList

</template>
<script>
import AsignmentsList from '@/components/asignments/List'
import MetricasList from '@/components/metrics/List'
export default {
  name: 'ReportesProgramados',
  components:{ 
    AsignmentsList,
    MetricasList
    },
}
</script>
