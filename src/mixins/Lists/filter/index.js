const _ = require('lodash')

const baseFilters = {
  data () {
    return {
      params:{filters:{}}
    }
  },
  methods:{
    prepareFilters(params, oldParams){
      let search = params.search
      if (oldParams) {
        let isNewSearch = !_.isEqual(params.filters, oldParams.filters)
        if (isNewSearch) params.page = 1
      }
      return params
    },
  },
  mounted(){
    this.paramFilters.push(this.prepareFilters)
  }
}

const CSFilters={
  mixins:[baseFilters],
  data () {
    return {
      caseSensitiveFilters:false
    }
  },
  methods:{
    filterResults(results){
      const self = this
      const filters =  this.params.filters
      this.seachedResults=false

      let validFilters =  Object.values(filters)
                                .filter(el=>el!=''&&el!=null).length
      if(validFilters<1) return results

      return results.filter(elem=>{
        for (var i = 0; i < Object.keys(filters); i++) {
          let k = Object.keys(filters)[i]
          if(!elem.hasOwnProperty(k)){
            console.error('Property '+k+' Does not exist in this elem')
          }else{
            let elemField =  elem[i]
            let found
            if (this.caseSensitiveFilters) {
              found = elemField.includes(seachTerm)
            }else{
              found = elemField.toLowerCase().includes(seachTerm.toLowerCase())
            }
            if (found) return true
          }
        }
        return false
      })
    }
  },
  mounted(){
    this.resultActions.push(this.filterResults)
  }
}


export {
  baseFilters,
  CSFilters
}
