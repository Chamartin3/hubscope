import {baseFormMixin, mainFormMixin} from './formMixin'
import axios from 'axios'

function getCookie (name) {
  var cookieValue = null
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';')
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim()
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
        break
      }
    }
  }
  return cookieValue
}
const csrftoken = getCookie('csrftoken')

export default{
props:{
  service:{
    required:false,
    default:null
  }
},
mixins:[baseFormMixin, mainFormMixin],
data () {
  return {
      authdata: {
        email: '',
        password: ''
      },
      al: {
        mensaje: '',
        type: 'danger',
        icon: ['fas', 'exclamation-triangle'],
        visible: false
      }
  };
},
  methods: {
    successLogin(msg){},
    failLogin(msg){},
    send () {
      let config = {
        headers: {
          'X-CSRFToken': csrftoken,
          csrf: csrftoken
        }
      }
      const self = this
      var qs = require('qs')
      console.log(config)
      console.log('coockie:' + csrftoken)
      var req = axios.post('/ajaxlogin/login/', qs.stringify(this.authdata), config).then(
        done => {
          console.log(done)
          var mensaje = done.data.message
          // var alerta = {}

          if (mensaje == 'Exito') {
            this.successLogin(done.data)
            let host = window.location.protocol + '//' + window.location.host
            window.location = host + '/tablero/'
          } else {
            this.failLogin(done.data)
          }
        },
        fail => {
          console.log('fail')
          console.log(fail)
          // alerta.mensaje = 'Error desconocido'
          // alerta.type = 'danger'
          // alerta.icon = ['fas', 'exclamation-triangle']
          // self.$emit('alerta',  alerta )

        })
    }
  }
}
