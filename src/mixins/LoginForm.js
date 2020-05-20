
export default {
  data(){
    return {
      form:{
        username: '',
        password: ''
      },
    }
  },
  methods:{
    authenticate(){
      let lg = this.$django.auth.login(this.form).then(
        this.SuccessLogin,
        fail=>{
          console.log(fail)
          this.$alert('danger','Error', fail.msj)
        }
      )
    },
    SuccessLogin(done){
      console.log(done)
      if(done.type=='error'){
        this.$alert('danger','Error', done.msj)
      }else{
        this.$alert('success','Exito', done.msj)
        let host = window.location.protocol + '//'+window.location.host
        console.log(host)
        window.location = host+'/'+this.$django.autentication.on_login

      }

    }

  },
  mounted(){
    console.log(this.$django)
  }
}
