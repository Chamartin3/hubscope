<template lang="pug">
.container.mb-5.fluid.fill-height.primary.darken-2
  .row.justify-center
    .col
      AsignmentsList(:company="instance.id" @new="$refs.Form.open()")
    .col-md-4.col-sm-12
      MetricasList(:company="instance.id")
      AsignmentsForm(ref="Form" :company="instance.id")

</template>
<script>
import AsignmentsList from '@/components/asignments/List'
import AsignmentsForm from '@/components/asignments/Form'
import MetricasList from '@/components/metrics/List'
export default {
  name: 'ReportesProgramados',
  props: ['instance'],
  components:{ 
    AsignmentsList,
    AsignmentsForm,
    MetricasList
    },
}
</script>
