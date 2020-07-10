export default {
  data(){
    return {
      datatable_filters:{}
    }
  },
  methods: {
    add_datatable_filter(name, value){
      let filtername = this.process_filtername(name, value) 
      this.$set(this.datatable_filters, filtername, value)
      this.datatable_filters_changed()
    },    
    remove_datatable_filter(name, value){
      let filtername = this.process_filtername(name, value) 
      delete this.datatable_filters[filtername]
      this.datatable_filters_changed()
    },
    process_filtername(name, value) { 
      let isarray = Array.isArray(value)
      if (isarray) return  name + '__in'
      // TODO: Hay que hacer que este filtro detecte fechas
      let isdate = name.includes('__gte') || name.includes('__lte')
      if (isdate) return  name 
      return name + '__contains'
    },
    datatable_filters_changed(){
      this.$emit('filters_changed', this.datatable_filters)
    }
  }
}