<template lang="pug">
div
  reportForm(ref="reportForm" @edited="listObjects")
  DeleteConfirmation(
    customMessage="¿Desea eliminar este reporte?"
    @success="listObjects"
    ref="deleteConfirm",
    model="report")
  DeleteConfirmation(
    ref="closeCofirm"
    model="report",
    method="close",
    @success="listObjects"
    customMessage="¿Desea cerrar este reporte? no se le podran hacer modificiones a los valores" )
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
    template(v-slot:item.begin="{ item }")
      div(v-if="item.status==='activa'")
        | Desde {{ item.begin | minidate }} hasta hoy
        | ({{ item | days }})

      div(v-else)
        | {{ item | simpleperiod }}
        | ({{ item | days }})

    template(v-slot:item.status="{ item }")
      reportStatus(:status="item.status")

    template(v-slot:item.delete="{ item }")
      v-icon.mr-2(small, @click="$refs.DeleteConfirmation.open(item.id, 'Usuario')")
        | fa-trash-alt

    template(v-slot:expanded-item='{ headers, item }')
      td(:colspan='headers.length')
        reportCard(
          @user=""
          @editReport="editReport($event)"
          @deleteReport="$refs.deleteConfirm.open(item.id)"
          @closeReport="$refs.closeCofirm.open(item.id)"
          :report="item")

</template>
<script>
import addHeaders from '@/layouts/templates/Tables/tableHeaders'
import TableTemplate from '@/layouts/templates/Tables/djangoTable'
import operationsMixin from '#/Lists/operations/clientSideCrud'
import reportCard from './Card'
import reportStatus from './Status'
import reportForm from '@/components/reports/Form'
import { Filters } from './utils'
import moment from 'moment'
export default {
  name: '',
  components: { reportCard, reportStatus, reportForm },
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
    Filters,
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
        { text: 'Metrica', sortable: false, value: 'metric__name' },
        { text: 'Status', sortable: false, value: 'status' },
        { text: 'Periodo', value: 'begin' }
        // { text: 'final', value: 'end' }
      ],
      params: {
        search: this.company,
        ordering: '-updated_at'
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
    editReport (report) {
      this.$refs.reportForm.edit(report.id, report)
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
