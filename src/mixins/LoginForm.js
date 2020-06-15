
export default {
  data(){
    return {
      loading: false,
      form:{
        username: '',
        password: ''
      },
    }
  },
  methods:{
    authenticate(){
      this.loading = true
      let lg = this.$django
      .auth.login(this.form)
      .then(this.SuccessLogin,this.FailLogin)
    },
    FailLogin(){
        
      console.log(fail)
        this.loading = false
        this.$alert('danger','Error', fail.msj)
      },
      SuccessLogin(done){
        this.loading = false
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

  }
}
