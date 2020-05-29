import baseList from '#/Lists/baseList'
import serverSide from '#/Lists/severSide'

export default {
  mixins:[ baseList, serverSide],
  data(){
    return {
      title:'',
      subtitle:'',
      itemName:"",
      itemIcon:"",
      itemPluralName:"Telefonos",
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
  filters: {
    TitleFilter (val, title) { return val[title] },
    SubtitleFilter (val, subtitle) { return val[subtitle] }
  },
  mounted () {
    if (!this.model) console.error('model required')
    this.listObjects()
  }
}
