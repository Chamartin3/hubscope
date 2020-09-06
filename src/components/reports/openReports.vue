<template lang="pug">
LightCard(title="Reportes enviados")
  reportForm(ref="reportForm")
  v-data-table.elevation-1(
    :server-items-length="totalItems"
    :loading="loading"
    :headers="headers"
    :items="items"
    :multi-sort="true"
    item-key="id"
    :items-per-page="params.per_page"
    @update:options="changeParams($event)"
    :no-data-text="`No hay reportes abiertos`"
    color="blue-grey lighten-2"
    )

    template(v-slot:item.metric__name="{ item }") {{ item.metric.name }}
    template(v-slot:item.edit="{ item }")
      v-btn.primary.dark(
      :disabled="item.status === 'esperando'"
      small @click="$emit('editReport', item)" ) Modificar

    template(v-slot:item.begin="{ item }")
      | {{ item.begin | simpleperiod }}

</template>
<script>
import reportForm from './Form'
import reportStatus from './Status'
import { base, serverSide } from '#/Lists'
import { Filters } from './utils'
import addHeaders from '@/layouts/templates/Tables/tableHeaders'
import TableTemplate from '@/layouts/templates/Tables/djangoTable'

export default {
  name: 'OpenReports',
  components: { reportStatus, reportForm },
  mixins: [ Filters, TableTemplate ],
  data () {
    return {
      modelName: 'report',
      listMethod: 'allOpen',
      sumary: {},
      pagination: {},
      table_headers: [
        { text: 'Metrica', value: 'metric__name' },
        { text: 'Periodo', value: 'begin' },
        { text: 'editar', value: 'edit' }
      ],
      params: {
        per_page: 5
      }
    }
  },
  computed: {
    headers () {
      return addHeaders(this.table_headers, false)
    }
  }

}
</script>
