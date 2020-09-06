<template lang="pug">
.container
  .row(v-if="loading")
    LoadingComponent
  .row(v-else)
    reportForm(ref="reportForm")
    .col-md-8
      pendingReports(@editReport="editReport($event)")
      OpenReports(@editReport="editReport($event)")
    .col-md-4
      Sumary(:empresas="items")

</template>
<script>
import EmpresaCard from '@/components/informe/Empresa.vue'
import Sumary from '@/components/empresas/Sumary.vue'
import OpenReports from '@/components/reports/openReports'
import pendingReports from '@/components/reports/pendingReports'
import reportForm from '@/components/reports/Form'
// import moment from 'moment'
import iteratorList from '@/layouts/templates/Lists/iteratorList.js'

import moment from 'moment'
export default {
  name: 'Dashboard',
  components: {
    Sumary,
    pendingReports,
    OpenReports,
    reportForm
  },
  //   components:{Card},
  mixins: [iteratorList],
  data () {
    return {
      modelName: 'company',
      itemName: 'Empresas',
      itemPluralName: 'Empresas',
      nodata: 'No hay empresas registradas',
      listMethod: 'all',
      params: {
        per_page: 3
      }
    }
  },
  mounted () {
    console.log(this.model)
  },
  methods: {
    editReport (report) {
      console.log('Evento')
      console.log(report)
      console.log(this.$refs)
      console.log(this.$refs.reportForm)
      this.$refs.reportForm.edit(report.id, report)
    },
    addItem (item) {
      item = this.preprocessElements(item)
      this.$set(this, 'items', [item, ...this.items])
      this.setPagination(this.items)
    }
  }
}
</script>
