<template lang="pug">
.container.mb-5.fluid.fill-height.primary.lighten-2
  .row.justify-center(v-if="!loading")
    .col
      v-expansion-panels(v-model="active" accordion multiple flat hover)
        Card(v-if="active" v-for='(item, idx) in items' :key='idx' :indicator='item')
      //- v-card(style="overflow-x: scroll").primary
      //-   v-tabs(v-model="tab" vertical dark background-color="primary" color="secondary")
      //-     v-tab(v-for="ind in items") {{ ind.name }}
      //-     v-tabs-slider(color='secondary')
      //-   v-tabs-items(v-model="model")
      //-     v-tab-item.primary.darken-1(v-for="ind in items" :key="ind.id" :value="ind.id" )
      //-       v-toolbar.darken-2( dark color="primary" ) {{ ind.name }}
      //-       Card(:indicator="ind") 
  .row(v-else)
    LoadingComponent

</template>
<script>
import List from '@/components/indicators/List.vue'
import Card from '@/components/indicators/Card.vue'
import iteratorList from '@/layouts/templates/Lists/iteratorList.js'
export default {
  props: ['instance'],
  name: 'Indicadores',
  components: { List, Card },
  mixins: [ iteratorList ],
  data () {
    return {
      active:[],
      tab:1,
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
           company__id:this.instance.id
         },
       }
    }
  }
}
</script>
