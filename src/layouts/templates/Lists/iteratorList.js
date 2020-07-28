// import baseList from '#/Lists/baseList'
// import serverSide from '#/Lists/severSide'

import {SSList} from '#/Lists'

export default {
  mixins:[ SSList ],
  data(){
    return {
      title:'',
      subtitle:'',
      itemName:"",
      itemIcon:"",
      itemPluralName:"",
      nodata:"nodata",
      pageLengthOptions:[5,10,15,20],
      itemKey:'id',
    }
  },
  methods: {
    callRegistration () { console.log('registration') },
    callDetail () { console.log('detail') },
    addElem(elem){
      let newElem=preprocessList(elem)
      this.list.push(newElem)
    }
  },
  computed:{
    totalPages(){
      let totalitems= this.pagination.total
      let perpage= this.pagination.per_page
      return Math.ceil(totalitems/perpage)
    },
    pagesText(){
      return  `Mostrando ${this.pagination.from} hasta ${this.pagination.to}`
    },    
    totalsText(){
      return  `Total ${this.pagination.total} ${ this.itemPluralName }`.toLowerCase()
    },
    currentText(){
      return  `Pagina ${ this.pagination.current_page } de ${ this.totalPages ? this.totalPages : 1  }`
    },
    perPageText(){
      return  `por pagina`
    }
  },
  filters: {
    TitleFilter (val, title) { return val[title] },
    SubtitleFilter (val, subtitle) { return val[subtitle] }
  },
  mounted () {
    if (!this.model) console.error('model required')
    this.listObjects()
  }
}
