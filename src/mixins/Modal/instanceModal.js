
export default {
  data(){
    return {
      model_name: '',
      instance:null,
      loading:false,
      id:null,
      retrieve_method:'retrieve',
    }
  },
  methods:{
    async setInstance(instance=null){
      if(instance){
        this.instance = instance
      }else{
        let model = this.$django.models[this.model_name]
        this.instance = await model[this.retrieve_method](this.id)
      }
    },
    async view(id, instance=null){
      this.id=id
      this.loading=true
      await this.setInstance(instance)
      this.dialog = true
      this.loading=false
    },
    close () {
      this.dialog = false
      this.instance = null
    },
  }
}
