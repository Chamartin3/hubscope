<template lang="pug">
.container.mb-5.fluid.fill-height
  .row.justify-center
    .col

  .row.justify-center
    .col-md-8
      LightCard(title="Reportes a la fecha")
        ReportsFilters(
            ref="filterManager"
            @filters_changed="$refs.Table.setDatableFilters($event)"
            @filter_removed="handleFilterChange")
        ReportsTable(ref="Table")
    .col-md-4
      LightCard(title="Filtros")
        .container
          CompanySelect(
            ref="CompanySelect"
            @input="filterByCompany"
          )
          MetricSelect(
            ref="MetricSelect"
            @input="filterByMetric")

          StatusSelect(
            @input="$refs.Table.setPropertyFilters({status:$event})"
            ref="StatusSelect")
          .col
            DateRangeSelect(
            ref="DateRangeSelect"
            @inputend="filterByRangeEnd"
            @inputbegin="filterByRangeBegin"
            )

</template>
<script>
import ReportsTable from '@/components/reports/Table'
// import StatusSelect from '@/components/reports/selects/Status'
import ReportsFilters from '@/components/reports/Filters.vue'
import CompanySelect from '@/components/empresas/Select.vue'

import {
  Status as StatusSelect,
  Metrics as MetricSelect,
  Dates as DateRangeSelect
} from '@/components/reports/selects'

export default {
  name: 'ReportesProgramados',
  components: {
    ReportsTable,
    ReportsFilters,
    StatusSelect,
    MetricSelect,
    DateRangeSelect,
    CompanySelect
  },
  data () {
    return {
      pfilters: {}
    }
  },
  watch: {
    pfilters (val) {
      if (val && this.$refs.Table) {
        this.$refs.Table.setPropertyFilters(val)
      }
    }
  },
  methods: {
    handleFilterChange (filter_name) {
      if (filter_name.includes('Metrica')) this.$refs.MetricSelect.reset()
      if (filter_name.includes('Reportes desde')) this.$refs.DateRangeSelect.resetBegin()
      if (filter_name.includes('Reportes hasta')) this.$refs.DateRangeSelect.resetEnd()
    },
    filterByRangeBegin (begin) {
      this.$refs.filterManager.setFilter(
        'Reportes desde',
        'begin__gte',
        begin
      )
    },
    filterByRangeEnd (end) {
      this.$refs.filterManager.setFilter(
        'Reportes hasta',
        'end__lte',
        end
      )
    },
    filterByPerson (person) {
      this.$refs.filterManager.setFilter(
        'Reportes realizados por:',
        'registered_by__username',
        person.username
      )
    },
    filterByMetric (metric) {
      this.$refs.filterManager.setFilter(
        'Metrica:',
        'metric__name',
        metric
      )
    },
    filterByCompany (company) {
      this.$refs.filterManager.setFilter(
        'Empresa:',
        'company__name',
        company
      )
    }
  }
}
</script>
