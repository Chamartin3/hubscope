<template lang="pug">
.container.mb-5.fluid.fill-height.primary.darken-2
  .row
    .col
      ReportsFilters(
        ref="filterManager"
        @filters_changed="$refs.Table.setDatableFilters($event)"
        :companyName="instance.name")
      ReportsTable(
        ref="Table"
        :company="instance.id")
    .col-md-4.col-sm-12
      PersonelList(
        @person="filterByPerson($event)"
        :companyid="instance.id", 
        :company_name="instance.name"
        )

</template>
<script>
import PersonelList from '@/components/empresas/positions/List'
import ReportsFilters from '@/components/reports/Filters.vue'
import ReportsTable from '@/components/reports/Table'
export default {
  name: 'ReportesRealizados',
  props:['instance'],
  components:{
    PersonelList,
    ReportsTable,
    ReportsFilters
  },
  methods: {
    filterByPerson(person){
      this.$refs.filterManager.setFilter(
        'Reportes realizados por:',
        'registered_by__username',
        person.username
      )
    }
  }
}
</script>
