


const formResponses = {
  methods: {
    show_alert(response = null) {
      if (response) {
        let tipo = response.type === 200 ? 'success'
          : response.type ? 'danger' : 'success'
        this.alert.show = true
        this.alert.type = tipo
        this.alert.message = response.message ? response.message : "Exito"
        let self = this
        if (response.message) {
          setTimeout(function() { self.alert.show = false }, 5000)
        }
      }
    }
  },
  data() {
    return {
      alert: { show: false, type: 'success', message: '' },
      response: {},
      actionsOnFail: [],
      actionsOnSuccess: []
    }
  },
  created() {
    this.actionsOnSuccess.push(this.show_alert)
    this.actionsOnFail.push(this.show_alert)
  }
}


export {
  baseFormMixin,
  mainFormMixin,
  subFormMixin,
  formResponses,
  viewModeMixin
}
