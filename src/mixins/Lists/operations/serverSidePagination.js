export default {
  data(){
    return {
      loading:false,
      totalItems:0,
      items:[],
      pagination:{},
      params:{
        page:1,
        page_size:5,
        ordering:'',
        search:'',
        datatable_filters:{},
      }
    }
  },
  watch:{
    params:{
      deep:true,
      immediate:true,
      handler:'listObjects'
    }
  },
  methods:{
    async listObjects(params={}){
      if (params && params.search!='') {
        params.page = 1
      }
      this.loading=true
      let data= await this.service.list('console', null, {
        ...params,
      })
      this.items = data.results
      this.totalItems = data.pagination.total
      this.pagination= data.pagination
      this.loading=false
    },
    changeParams(options){
      this.$set(this.params, 'page', options.page)
      let size= options.itemsPerPage > 0 ? options.itemsPerPage: this.totalItems
      this.$set(this.params, 'page_size', size)
      let orders=''
      for (var i = 0; i < options.sortBy.length; i++) {
        if (i>0) orders+=','
        orders+= options.sortDesc[i]?'-':''
        let field= options.sortBy[i].includes('.') ? options.sortBy[i].replace(".", "__") : options.sortBy[i]
        orders+= field
      }
      this.$set(this.params, 'ordering', orders)
    },
  }
}
