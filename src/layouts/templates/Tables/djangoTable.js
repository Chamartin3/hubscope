// import SSPagination from '@/mixins/serverSidePagination.js'
// import clientSideCrud from '@/mixins/clientSideCrud.js'
// import detailDialog from './DetailDialog'

import {SSList} from '#/Lists'
export default {
  mixins:[SSList],
  data () {
    return {
      filterFields: "look out fields",
      filtering: true,
      searchField:true,
      pagination:{},
      params:{
        datatable_filters:{}
      }
    }
  },
  computed:{
    totalItems(){
      if (this.pagination.total) return this.pagination.total
      else return 0
    }
  },
  methods:{
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
  },
}
