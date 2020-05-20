

export default {
  data() {
    return {
      subForm: true,
      serviceProp:{
        type:Object,
        required:false,
        default:null
      },
    }
  },
  methods: {
    _preProcessForm() {
      let proxy = { ...this.form }
      return proxy
    },
    preProcessForm(form) { return form },
    _setInstance() {
      if (this.$attrs.value) {
        this.instance = this.preProcessInstance(this.$attrs.value)
      } else {
        this.instance = null
      }
      this._setFields(this.instance)
    }
  },
  watch: {
    form: {
      deep: true,
      handler: function(val, oldVal) {
        let form = this.preProcessForm(this._preProcessForm())
        if (form) this.$emit('input', form)
      }
    },
  }

}
