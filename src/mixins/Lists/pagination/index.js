const basePagination = {
  data () {
    return {
      pagination:{},
      paginated:true,
      params:{
        page:1,
        per_page:10
      },
    }
  },
  methods:{
    setPagination(results){
      this.pagination = {
        total_items: results.length,
        current_page:1,
        total_pages:1,
      }
      return results
    },
  },
  mounted(){
    this.resultActions.push(this.setPagination)
  }
}

const serverSide = {
  data () {
    return {
      clientPagination:true,
    }
  },
  methods:{
    setPagination(results){
      if (results && results.pagination) {
        this.pagination = results.pagination
        return results.results
      }
      return results
    },
  },
}


const clientSide = {
  data () {
    return {
      clientPagination:true,
    }
  },
  methods:{
    setPagination(results){
      // vClient Side Paginatiuon
      let per_page = this.params.per_page
      let total = results.length
      let total_pages = Math.ceil(total / per_page)
      let current_page = this.params.page
      let current_begin = (current_page-1) * per_page
      let current_end = current_begin + per_page
      current_end = current_end < total ? current_end : total
      let items  = results.slice(current_begin, current_end)
      this.pagination = {
        total_items: total,
        current_page:current_page,
        total_pages:total_pages,
        current_begin:current_begin+1,
        current_end:current_end,
        per_page:per_page
      }
      return items
    },
  },
}

const CSPagination = {
  mixins:[ basePagination, clientSide ]
}


const SSPagination={
  mixins:[basePagination, serverSide]
}


export {
  CSPagination,
  SSPagination,
}
