export default {
  data () {
    return {
      loading:false,
      params:{},
      items:[],
      resultActions:[],
      paramFilters:[],
    }
  },
  computed:{
    model(){
      // modelName Requires prop or data
      if (this.modelName) return this.$django.models[this.modelName]
    }
  },
  watch:{
    params:{
      deep:true,
      immediate:true,
      handler(newParams, oldParams){
        let params = this._preProcessParams(newParams, oldParams)
        this.listObjects(params)
      }
    }
  },
  methods:{
    async getItems(params={}){
      this.loading = true
      return items
    },
    async listObjects(params={}){
      let list = await this.getItems(params)
      let processedList = this._processResults(list)
      this.items = processedList.map(x=>this.preprocessElements(x))
      this.loading = false
    },
    _processResults(results) {
      for (var i = 0; i < this.resultActions.length; i++) {
        results=this.resultActions[i](results)
      }
      return results
    },
    _preProcessParams(params, oldp) {
      for (var i = 0; i < this.paramFilters.length; i++) {
        params=this.paramFilters[i](params,oldp)
      }
      return params
    },
    processResults(results){return results},
    preprocessElements(elem) {return elem},
  },
  mounted(){
    this.resultActions.push(this.processResults)
  }


}
