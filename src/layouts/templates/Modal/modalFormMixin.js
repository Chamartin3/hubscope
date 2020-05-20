import { baseMainFrom  } from '#/Forms'
import formAlertMixin from '#/formAlertMixin'
export default {
  mixins:[baseMainFrom formAlertMixin],
  name: "",
  data(){
    return {
      customFormTitle:null,
      modalColor:null,
      modalDark:false,
      maxWidth:null,
      dialog: false,
      activator: true,
      model_name: '',
      valid:true,
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
    beforeSend() {
      this._validateForm()
      this.loading=true
    },
    stopLoading(){this.loading=false},
    open () {
      this.clearAll()
      this.dialog = true
      this.inErrors = {}
    },
    exito(){
      this.cerrar()
      this.$emit('successChange')
    },
    cerrar () {
      this.clearAll()
      this._resetValidation()
      this.dialog = false
      this.instance = null
      this.mode="creation"
    },
    edit(id, instance=null){
      this.mode="edition"
      if (instance){
        this.instance = instance
        this._setFields(instance)
      }
      else this._fetchInst(id)

      this.dialog = true
    }
  },
  mounted () {
    this.actionsOnSuccess.push(this.exito)
    this.actionsOnSuccess.push(this.stopLoading)
    this.actionsOnFail.push(this.stopLoading)
  }

}
