import DatatableProcesing from '@/layouts/templates/Tables/datatableFilters'
export default {
  mixins:[ DatatableProcesing ],
  data () {
    return {
      filters:[]
    }
  },
  watch: { 
    filters: {
      deep: true,
      handler: 'refreshFilters'
    }
  },
  methods: {
    refreshFilters (val, oldVal) {
      const newFiltersName = val.map(x => x.db_name)
      const removedFilters = oldVal.filter(v => !newFiltersName.includes(v.db_name))

      for (let i = 0; i < removedFilters.length; i++) {
        let remfil = removedFilters[i]
        this.remove_datatable_filter(remfil.db_name, remfil.value)
      }
      for (let j = 0; j < val.length; j++) {
        let fil = val[j]
        this.add_datatable_filter(fil.db_name, fil.value)
      }
    },
    setFilter (name, dbname, value) {
      this.filters.push({
        name: name,
        db_name: dbname,
        value: value
      })
    },
    removeAllFilters () {
      this.$set(this, 'filters', [])
    }
  }
}
