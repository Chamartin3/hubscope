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
  color="blue-grey"
  )

  template(v-slot:item.metric__name="{ item }") {{ item.metric.name }}
  template(v-slot:item.end="{ item }")
    | {{ item.end | date }}
  template(v-slot:item.begin="{ item }")
    | {{ item.begin | date }}

  template(v-slot:item.status="{ item }")
    reportStatus(:status="item.status")

  template(v-slot:item.delete="{ item }")
    v-icon.mr-2(small, @click="$refs.DeleteConfirmation.open(item.id, 'Usuario')")
      | fa-trash-alt

  template(v-slot:expanded-item='{ headers, item }')
    td(:colspan='headers.length')
      reportCard(
        @user=""
        @editReport=""
        @deleteReport=""
        :report="item")

</template>
<script>
import addHeaders from '@/layouts/templates/Tables/tableHeaders'
import TableTemplate from '@/layouts/templates/Tables/djangoTable'
import operationsMixin from '#/Lists/operations/clientSideCrud'
import reportCard from './Card'
import reportStatus from './Status'
import moment from 'moment'
export default {
  name: '',
  components: { reportCard, reportStatus },
  filters: {
    period (item) {
      let begin = moment(item.begin).format('DD MMM-YYYY')
      let end = moment(item.end).format('DD MMM-YYYY')
      return `${begin} - ${end}`
    },
    datetime (time) {
      return moment(time).format('dddd, DD MMMM YYYY hh:mm ')
    },
    date (time) {
      return moment(time).format('dddd, DD MMMM YY')
    }

  },
  mixins: [
    operationsMixin,
    TableTemplate
  ],
  props: ['company'],
  data () {
    return {
      selected_period: '',
      modelName: 'report',
      modelNamePlural: 'Reportes',
      downloading: false,
      filterFields: 'Buscar documento',
      expanded: [],
      // dt_endpoint_name: 'list',
      // filtering: true,
      searchField: true,
      table_headers: [
        { text: 'Detalle', sortable: false, value: 'data-table-expand' },
        { text: 'Metrica', value: 'metric__name' },
        { text: 'Status', sortable: false, value: 'status' },
        { text: 'Inicio', value: 'begin' },
        { text: 'final', value: 'end' }
      ],
      params: {
        search: this.company
      }
      //
      // service: this.$django.models.,
    }
  },
  computed: {
    headers () {
      return addHeaders(this.table_headers, false)
    }
  },
  methods: {
    setDatableFilters (newfilters) {
      this.$set(this.params, 'datatable_filters', newfilters)
      if (Object.keys(newfilters).length === 0) this.listObjects(this.params)
    },
    setPropertyFilters (properties) {
      console.log('property filters')
      console.log(properties)
      this.$set(this.params, 'property_filters', properties)
      if (Object.keys(properties).length === 0) this.listObjects(this.params)
    }
  }
}
</script>
