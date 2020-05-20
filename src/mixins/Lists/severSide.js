export default {
  data () {
    return {
      serverSide:true,
      listMethod:'list',
      paginated:true,
      pagination:{},
      pendingRequest: false
    }
  },
  watch: {
    loading (val) {
      if (!val && this.pendingRequest) {
        this.pendingRequest = false
        this.listObjects(this.params)
      }
    }
  },
  computed:{
    model(){
      // modelName Requires prop or data
      if (this.modelName) return this.$django.models[this.modelName]
    }
  },
  methods:{
    async getItems(params={}){
      if (this.loading){
        this.pendingRequest = true
        return []
      }

      this.loading = true
      let results
      if (this.params) {
        results = await this.model[this.listMethod](this.params)
      }else{
        results = await this.model[this.listMethod]()
        if (params && params.search!='') params.page = 1
      }
      return results
    }
  },
  mounted(){
    if(!this.modelName) console.error('model required')
  }
}
