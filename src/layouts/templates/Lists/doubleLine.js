export default {
  data(){
    return {
      title:null,
      subtitle:null,
      itemName:"",
      itemActionIcon:"fas fa-external-link-alt",
      itemPluralName:"Telefonos",
    }
  },
  methods:{
    callRegistration(){console.log('registration')},
    callDetail(){console.log('detail')},
    getItemTitle(item){
      if (!item) return ''
      if (this.title) return item[this.title]
      return item
    },
    getItemSubTitle(item){
      if (!item || !this) return ''
      if (this.subtitle) return item[this.subtitle]
      return item
    }
  }
}
