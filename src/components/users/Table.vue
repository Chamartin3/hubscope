<template lang="pug">
extends ../../layouts/templates/Tables/baseFullCrud.pug
block header
  v-toolbar(flat color="white")
    DeleteConfirmation(
      model="accounts"
      ref="DeleteConfirmation"
      @success="removeItem($event)")
    userDetail(
      @successChange="changeItem($event)"
      ref="userDetail")

    v-text-field(
      v-model="params.search",
      append-icon="fa-search",
      label="Buscar Socios",
      placeholder="Buscar Usuario"
      single-line,
      hide-details)
    |
    v-divider.mx-4(inset, vertical)
    |
    v-spacer
    |
    Form(@created="addItem")

block options
  template(v-slot:item.detail="{ item }")
    v-icon.mr-2(small, @click="$refs.userDetail.view(item.id, item)")
      | fa-external-link-alt

  template(v-slot:item.delete="{ item }")
    v-icon.mr-2(small, @click="$refs.DeleteConfirmation.open(item.id, 'Usuario')")
      | fa-trash-alt

</template>
<script>
import userDetail from './Detail'
import Form from './Form'
import { dateFilter, moneyFilter, periodFilter } from './utils'
import addHeaders from '@/layouts/templates/Tables/tableHeaders'
import TableTemplate from '@/layouts/templates/Tables/djangoTable'
import operationsMixin from '#/Lists/operations/clientSideCrud'

export default {
  name: "",
  components:{
    userDetail,
    Form
  },
  mixins:[
    operationsMixin,
    TableTemplate
  ],
  computed:{
    headers(){
      return addHeaders(this.table_headers, false)
    }
  },
  data () {
    return {
      selected_period:"",
      modelName: 'accounts',
      modelNamePlural: 'Usuarios',
      downloading:false,
      filterFields: "Buscar documento",
      // dt_endpoint_name: 'list',
      // filtering: true,
      searchField:true,
      table_headers:[
        {text: 'Nombre de Usuario',value: 'username'},
        {text: 'Nombre',  value: 'first_name'},
        {text: 'Apellidos',value: 'last_name' },
        {text: 'Detalle', sortable: false, value:'detail'},
        {text: 'Eliminar', sortable: false, value:'delete'}
      ]
      //
      // service: this.$django.models.,
      }
  }
}
</script>
<style>
  /* .v-data-table-header{
    background-color: rgb(87, 0, 0);
  }
  thead.text-start {
  }
  th {
    color:white !important;
    font-size: 17px !important;
  } */
</style>
