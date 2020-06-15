<template lang="pug">
v-data-table.elevation-1(
  :server-items-length="totalItems"
  :loading="loading"
  :headers="headers"
  :items="items"
  
  :expanded.sync="expanded"
  show-expand
  :single-expand="true"
  :multi-sort="true"
  item-key="id"
  :items-per-page="params.per_page"
  @update:options="changeParams($event)"
  :no-data-text="`No se ha encontrado ${modelNamePlural}`"
  dark
  color="primary lighten-2"
  )

  template(v-slot:item.metric__name="{ item }") {{ item.metric.name }}
  template(v-slot:item.metric__unidad="{ item }") {{ item.metric.unidad }}
  template(v-slot:item.num_value="{ item }") {{ item.value }}

  template(v-slot:item.delete="{ item }")
    v-icon.mr-2(small, @click="$refs.DeleteConfirmation.open(item.id, 'Usuario')")
      | fa-trash-alt
  
  template(v-slot:expanded-item='{ headers, item }')
    td(:colspan='headers.length')
      .container
        .row
          .col Periodo  {{ item | period }}        
        .row
          .col Registrado el {{item.created_at | datetime}}
        .row
          .col Registrado Por {{item.registered_by}}

</template>
<script>
import addHeaders from '@/layouts/templates/Tables/tableHeaders'
import TableTemplate from '@/layouts/templates/Tables/djangoTable'
import operationsMixin from '#/Lists/operations/clientSideCrud'
import moment from 'moment'
export default {
  name: "",
  props:['company'],
  mixins:[
    operationsMixin,
    TableTemplate
  ],
  computed:{
    headers(){
      return addHeaders(this.table_headers, false)
    },
  },
  filters:{
    period(item){
      let begin=moment(item.begin).format('DD MMM-YYYY')
      let end=moment(item.end).format('DD MMM-YYYY')
      return `${begin} - ${end}`
    },
    datetime(time){
      return moment(time).format('dddd, DD MMMM YYYY hh:mm ')

    }
  },
  data () {
    return {
      selected_period:"",
      modelName: 'report',
      modelNamePlural: 'Reportes',
      downloading:false,
      filterFields: "Buscar documento",
      expanded:[],
      // dt_endpoint_name: 'list',
      // filtering: true,
      searchField:true,
      table_headers:[
        { text: 'Detalle', sortable: false, value: 'data-table-expand' },
        {text: 'Metrica',value: 'metric__name'},
        {text: 'Valor',  value: 'num_value'},
        {text: 'Unidad',  value: 'metric__unidad'},
      ],
      params:{
        search:this.company
      }
      //
      // service: this.$django.models.,
      }
  }
}
</script>