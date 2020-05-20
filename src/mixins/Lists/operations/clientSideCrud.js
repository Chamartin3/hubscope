export default {
  methods:{
    removeItem (id) {
      let item=this.items.filter(x=>x.id===id)[0]
      const index = this.items.indexOf(item)
      this.items.splice(index, 1)
    },
    getIndex(item) {
      return this.items.map(i=>i.id).indexOf(item.id)
    },
    changeItem (newitem) {
      let idx = this.getIndex(newitem)
      Object.assign(this.items[idx], newitem)
    },
    addItem(newItem) {
      this.items.push(newItem)
    }
  },
}
