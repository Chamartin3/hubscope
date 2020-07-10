<template lang='pug'>
extends ../../layouts/templates/Lists/iteratorList.pug
block content
  .row
     .col
      .row
      v-expansion-panels(v-model="active" accordion multiple flat hover)
        Card(v-if="active" v-for='(item, idx) in items' :key='idx' :indicator='item')
      
//- block instance
//- block nodata
   strong {{nodata}}
block header
  v-toolbar.mb-1.px-5(v-if="!loading && pagination.last_page!=1" dark, dense color="secondary darken-1")
    v-row.mt-2(align="center", justify="center")
      span.white--text
        .overline
          h3 {{ pagesText }}
        .overline
          h3 {{ totalsText }}
      v-spacer
      span.mr-4.white--text
        | {{ currentText }}
      |
      v-btn.mr-1(dark, small color="primary darken-3",
      :disabled="pagination.current_page==1"
      @click="params.page=params.page-1")
        v-icon fa-angle-left
      |
      v-btn.ml-1(dark, small color="primary darken-3",
      :disabled="pagination.current_page>=totalPages || !totalPages"
      @click="params.page=params.page+1")
        v-icon fa-angle-right
block footer

</template>
<script>
// ~/Code/Django/hubscope/src/components/indicators/List.vue
import iteratorList from '@/layouts/templates/Lists/iteratorList.js'
import Card from './Card'
export default {
  name: 'indicatorList',
   components: { Card },
  mixins: [ iteratorList ],
  props:['company'],
  data () {
    return {
      active:[],
      itemKey:'id',
      modelName:'indicator',
      itemName: 'Indicador',
      itemPluralName: 'Indicadores',
      nodata:'No hay indicators registradas',
      params:{
         page:1,
         page_size:5,
         ordering:'',
         search:'',
         datatable_filters:{
           company__id:this.company.id
         },
       }
    }
  },
  methods:{
  },
  watch:{
    "pagination.per_page":function(val){
      for (let i = 0; i < val+1; i++) {
        this.active.push(i)
      }
    }
  }
}
</script>