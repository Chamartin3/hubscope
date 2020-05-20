const baseSearch = {
  data () {
    return {
      params:{search:''}
    }
  },
  methods:{
    prepareSearch(params, oldParams){
      let search = params.search
      if (oldParams) {
        let isNewSearch = search != oldParams.search
        if (isNewSearch) params.page=1
      }
      return params
    },
  },
  mounted(){
    this.paramFilters.push(this.prepareSearch)
  }
}

const CSSearch={
  mixins:[baseSearch],
  data () {
    return {
      searchFields:[],
      seachedResults:false,
      caseSensitiveSearch:false
    }
  },
  methods:{
    makeSearch(results){
      const self=this
      const seachTerm =  String(this.params.search)
        this.seachedResults=false
      if (seachTerm === '' || seachTerm == null) return results
        this.seachedResults=true
      if (this.searchFields.length==0) {
        console.error('No searchFields setted')
      }
      return results.filter(elem=>{
        for (var i = 0; i < this.searchFields.length; i++) {
          let elemField =  String(elem[this.searchFields[i]])
          let found
          if (this.caseSensitiveSearch) {
            found = elemField.includes(seachTerm)
          }else{
            found = elemField.toLowerCase().includes(seachTerm.toLowerCase())
          }
          if (found) return true
        }
        return false
      })
    }
  },
  mounted(){
    this.resultActions.push(this.makeSearch)
  }
}


export {
  baseSearch,
  CSSearch
}
