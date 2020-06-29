export default{
  data(){
    return{
    successAlertMessage:'',
    failAlertMessage:'Error en Formulario',
  }
  },
  methods:{
    _alertResult(done){
      let msg = this.successAlertMessage || 'Los datos de han enviado correctamente'
      if(done && done.message) this.$alert('success','Exito',done.message)
      else this.$alert('success','Exito',msg)
    },
    _alertFail(fail){
      fail = fail.response ? fail.response : fail
      let type = fail.status ? fail.status : ''
      fail = fail.data ? fail.data : fail
      let message


      if (fail.non_field_errors)  {
        message = fail.non_field_errors.toString()
      }
      
      if (typeof fail === 'object' && type == 400 && !message) {
        message = 'Error en Formulario'
      }

      if( fail.message && !message) {
        message = fail.message
        delete fail.message
      }

      if (!message) message = this.failAlertMessage || fail
      

      if(fail && (type===401||type==400 )&& message){
        this.$alert('danger','Error', message)


      } else if(fail && fail.detail) {
        this.$alert('danger',`Error ${type}`,fail.detail)

      } else {
        if (fail && message){
          this.$alert('danger','Error', message)
        } else {
          this.$alert('danger','Error', message.message)
        }
      }
    }
  },
  mounted() {
    this.actionsOnSuccess.push(this._alertResult)
    this.actionsOnFail.push(this._alertFail)
  }
}
