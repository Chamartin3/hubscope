export default{
  data(){
    return{
    successAlertMessage:'',
    failAlertMessage:'',
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

      if (fail.non_field_errors)  {
        fail.message = fail.non_field_errors.toString()
      }

      let msg = this.failAlertMessage || fail

      if(fail && fail.type && fail.type===401 && fail.message){

        this.$alert('danger','Error',fail.message)

      }else if(fail && fail.detail){

        this.$alert('danger',`Error ${type}`,fail.detail)
      }else {
        if(fail && fail.message)
        this.$alert('danger','Error', fail.message)
        else this.$alert('danger','Error',msg.message)
      }
    }
  },
  mounted() {
    this.actionsOnSuccess.push(this._alertResult)
    this.actionsOnFail.push(this._alertFail)
  }
}
