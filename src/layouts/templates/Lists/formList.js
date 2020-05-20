export default {
  name: "",
  props:['errors'],
  data(){
    return{
      name: "Items",
      items:[],
      subtitle:true,
      errorMessage:''
    }
  },
  methods:{
    removeItem(idx){
      this.items.splice(idx, 1)
    },
    addItem(person){
      this.items.push(person)
    },
    openForm(){
      this.$refs.instanceForm.open()
    },
  },
  watch:{
    errors(val){
      this.errorMessage = val
    },
    items:{
      deep:true,
      handler:function(val){
        this.$emit('change',val)
        this.$emit('input',val)
      }
    }
  },
  filters:{
    title(val){
      return val
    },
    subtitle(val){
      return val
    },
  },
}
