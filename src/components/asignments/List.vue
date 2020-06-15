<template lang='pug'>
extends ../../layouts/templates/Lists/iteratorList.pug
append content
  .row
     .col
      .row
         v-col(v-for='item in items', :key='item.name', cols='12', sm='12', md='6', lg='4')
           Card(v-if='item', :asignment='item')
  // block header
  // block footer
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