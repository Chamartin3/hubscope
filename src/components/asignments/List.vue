<template lang='pug'>
.container.mb-5.fluid.fill-height
  DeleteConfirmation(
      model="asignment"
      ref="DeleteConf"
      customMessage="¿Desea cerrar esta asignación? no se eliminaran los reportes pero se dejaran de crear automaticamente"
      @success="listObjects();$emit('changed')")
  .row.justify-space-around
    GeneralPagination(
      color="secondary"
      v-model="params.page",
      :names="{singular:'asignación', plural:'asignaciones'}"
      :pagination="pagination")
  .row(v-if="items.length<1").justify-center
    .overline
      h2 No hay asignaciones registradas
  .row(v-else)
    v-col(
          v-for='item in items',
          :key='item.name',
          cols='12', sm='12', md='6', lg='4')
           AsignmentCard(
             @borrar="$refs.DeleteConf.open($event,'Asignación')"
             v-if='item', :asignment='item')
block footer
</template>
<script>

// ~/Code/Django/hubscope/src/components/asignments/List.vue
import iteratorList from '@/layouts/templates/Lists/iteratorList.js'
import AsignmentCard from './Card'
export default {
  name: 'AsignmentList',
  components: { AsignmentCard },
  mixins: [ iteratorList ],
  props: [ 'company' ],
  data () {
    return {
      modelName: 'asignment',
      nodata: 'No hay asignaciones registradas',
      params: {
        company: this.company
      }
    }
  },
  methods: {
  }
}
</script>
