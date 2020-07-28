<template lang="pug">
.container.mb-5.fluid.fill-height
  v-toolbar.text-left.secondary
    .row.justify-space-between.px-4
      .headline Asignaciones
      v-btn(
      color="primary" 
      @click="$refs.Form.open()") Nueva Asignación
  hr.sline
  .row
    .col
      AsignmentsList(:company="instance.id")
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
