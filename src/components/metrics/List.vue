<template lang='pug'>
extends ../../layouts/templates/Lists/doubleLineList.pug
append before_list
  .row.text-center.justify-space-around.mt-1
     v-btn(small
    @click='addMetric'
    color='secondary') Crear
block no_items
  .row
    .col
      .overline
        h2 No hay Metricas registradas

</template>
<script>
// ~/Code/Django/hubscope/src/components/metrics/List.vue
import { SSDobleLine } from '@/layouts/templates/Lists'
export default {
// 	props:['id']  // Filtered
  name: 'metricList',
  mixins: [ SSDobleLine ],
  data () {
    return {
      searchField: false,
      title: 'name',
      subtitle:'desc',
      itemIcon: 'fas fa-ruler',
      itemName: 'metric',
      itemPluralName: 'Metricas',
      modelName: 'metric',
//			listMethod: 'list',
// 			params:{id:this.id},  Filtered
    }
  },
  methods:{
    addMetric(){console.log('registration')},
    callRegistration(){console.log('registration')},
    callDetail(){console.log('detail')},
    getItemTitle(item){
      return `${item.name} (${item.unidad})`
    }

  }
}
</script>