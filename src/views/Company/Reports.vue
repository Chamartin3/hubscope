<template lang="pug">
.container.mb-5.fluid.fill-height
  .row
    .col-12.col-md-8
      ReportsFilters(
        ref="filterManager"
        @filters_changed="$refs.Table.setDatableFilters($event)"
        @filter_removed="handleFilterChange"
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

      card
        template(slot="title")
          .headline Status
        StatusSelect(
          @input="$refs.Table.setPropertyFilters({status:$event})"
          ref="StatusSelect")

      card
        template(slot="title")
          v-icon.white--text.mx-2 far fa-calendar-alt
          .headline Rango de Fechas
        DateRangeSelect(
          ref="DateRangeSelect"
          @inputend="filterByRangeEnd"
          @inputbegin="filterByRangeBegin"
        )
      card
        template(slot="title")
          v-icon.white--text.mx-2 fas fa-ruler
          .headline Metricas
        MetricSelect(
          ref="MetricSelect"
          :company="instance.id"
          @input="filterByMetric")
      

</template>
<script>
import PersonelList from '@/components/empresas/positions/List'
import ReportsFilters from '@/components/reports/Filters.vue'
import ReportsTable from '@/components/reports/Table'

import StatusSelect from '@/components/reports/selects/Status'
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
    MetricSelect,
    StatusSelect
  },
  methods: {
    handleFilterChange(filter_name){
      if (filter_name.includes('Metrica')) this.$refs.MetricSelect.reset()       
      if (filter_name.includes('Reportes desde')) this.$refs.DateRangeSelect.resetBegin()       
      if (filter_name.includes('Reportes hasta')) this.$refs.DateRangeSelect.resetEnd()       
    },
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
