<template lang='pug'>
extends ../../layouts/templates/Lists/doubleLineList.pug
append before_list
  .row.text-center.justify-space-around.mt-1
     v-btn(small v-if="!company"
    @click='addMetric'
    color='secondary') Crear
block no_items
  .row.text-center
    .col
      .overline
        h2 {{noneData}}
block item_action

</template>
<script>
// ~/Code/Django/hubscope/src/components/metrics/List.vue
import { SSDobleLine } from '@/layouts/templates/Lists'
export default {
	props:['company'],  // Filtered
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
//		listMethod: 'list',
			params:{
        company:this.company
        }, 
    }
  },
  computed:{
    noneData(){
      if (this.company) return 'No hay metricas asignadas a esta empresa'
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