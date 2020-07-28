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
    setFilter (name, db_name, value) {
      let obj = {
        name: name,
        db_name: db_name,
        value: value
      }  
      // Verifica si el filtro existe por nombre y lo remplaza
      let index = this.filters.indexOf(this.filters.find(f=>f.name==name))
      if ( index==-1 ) this.filters.push(obj) 
      else this.filters.splice(index, 1, obj)
    },
    removeFilter(name){
      let index = this.filters.indexOf(this.filters.find(f=>f.name==name))
      if ( index==-1 ) return
      let elobj = {...this.filters[index]}
      this.remove_datatable_filter(elobj.db_name, elobj.value)
      this.$emit('filter_removed',name)
      this.filters.splice(index, 1)
    },
    removeAllFilters () {
      this.$set(this, 'filters', [])
    }
  }
}
