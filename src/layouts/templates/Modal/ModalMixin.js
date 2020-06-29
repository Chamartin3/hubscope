// mport {baseFormMixin, errorsMixin } from '@/mixins/VueAjaxFormMixin'
// import mainFormMixin from '@/mixins/VueAjaxFormMixin/modelMainForm'
// import formAlertMixin from '@/mixins/formAlertMixin'
export default {
  name: "",
  data(){
    return {
      customFormTitle:null,
      buttomText:null,
      modalColor:null,
      modalDark:false,
      dialog: false,
      activator: true,
      model_name: '',
      valid:true,
      service:null,
      loading:false,
      instance:null
    }
  },
  computed:{
    formTitle(){
      if(this.customFormTitle) return this.customFormTitle
      if(this.mode==='creation') return 'Crear'
      return 'Editar'
    }
  },
  methods:{
    open () {
      this.dialog = true
      this.inErrors = {}
    },
    exito(){
      this.cerrar()
    },
    cerrar () {
      this.dialog = false
      this.instance = null
    },
    async edit(id, instance=null){
      if (instance){
        this.instance = instance
      } else if(this.service) {
        this.instance = await this.service.retrieve(id)
      } else {
        console.log("No instance")
      }
      this.dialog = true
    }
  },
  mounted () {

  }

}
