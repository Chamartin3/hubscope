<template lang='pug'>
extends ../../layouts/templates/Lists/iteratorList.pug
append header
append content
  .row
     .col
      .row
         v-col(v-for='item in items', :key='item.name', cols='12', sm='12', md='6', lg='4')
           Card(v-if='item', :asignment='item')
block header
  .row.justify-space-around(v-if="!loading")

    v-btn.ml-5(dark, color="secondary",
        fab
        :disabled="pagination.current_page==1"
        @click="params.page=params.page-1")
        v-icon fa-angle-left
    .col.text-center
      span.white--text
        | {{ currentText }}
      .row.justify-center.mt-n3
        .col.text-center
          span.white--text
            | {{ totalsText }}
    v-btn.mr-5(dark, color="secondary",
        fab
        :disabled="pagination.current_page>=totalPages || !totalPages"
        @click="params.page=params.page+1")
        v-icon fa-angle-right
  hr.sline
  .row.text-center
    .col
      v-btn(color="secondary" @click="$emit('new')") Nueva Asignación
block footer
</template>
<script>
// ~/Code/Django/hubscope/src/components/asignments/List.vue
import iteratorList from '@/layouts/templates/Lists/iteratorList.js'
import Card from './Card'
export default {
  name: 'asignmentList',
   components: { Card },
  mixins: [ iteratorList ],
  data () {
    return {
       modelName:'asignment',
       itemName: 'asignment',
       itemPluralName: 'asignaciones',
       nodata:'No hay asignaciones registradas',
       //params:{
         // page:1,
         // page_size:5,
         // ordering:'',
         // search:'',
         // datatable_filters:{},
       // }
     }
  },
  methods:{
  },
}
</script>