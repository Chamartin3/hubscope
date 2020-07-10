<template lang="pug">
.container.mb-5.fluid.fill-height.primary.darken-2
  .row
    .col-12.col-md-8
      ReportsFilters(
        ref="filterManager"
        @filters_changed="$refs.Table.setDatableFilters($event)"
        :companyName="instance.name")
      ReportsTable(
        ref="Table"
        :company="instance.id")
    .col-12.col-md-4
      PersonelList(
        @person="filterByPerson($event)"
        :companyid="instance.id", 
        :company_name="instance.name"
        )
      DateRangeSelect(
        @inputend="filterByRangeEnd"
        @inputbegin="filterByRangeBegin"
      )
      MetricSelect(
        :company="instance.id"
        @input="filterByMetric")

</template>
<script>
import PersonelList from '@/components/empresas/positions/List'
import ReportsFilters from '@/components/reports/Filters.vue'
import ReportsTable from '@/components/reports/Table'
import DateRangeSelect from '@/components/reports/selects/Dates'
import MetricSelect from '@/components/reports/selects/Metrics'
export default {
  name: 'ReportesRealizados',
  props:['instance'],
  components:{
    PersonelList,
    ReportsTable,
    ReportsFilters,
    DateRangeSelect,
    MetricSelect
  },
  methods: {
    filterByRangeBegin(begin){
      
      this.$refs.filterManager.setFilter(
        'Reportes desde',
        'begin__gte',
        begin
      )
    },      
    filterByRangeEnd(end){
      this.$refs.filterManager.setFilter(
        'Reportes hasta',
        'end__lte',
        end
      )
    },
    filterByPerson(person){
      this.$refs.filterManager.setFilter(
        'Reportes realizados por:',
        'registered_by__username',
        person.username
      )
    },    
    filterByMetric(metric){
      this.$refs.filterManager.setFilter(
        'Metrica:',
        'metric__name',
        metric
      )
    },
  }
}
</script>
