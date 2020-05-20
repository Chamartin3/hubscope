
export default {
  props: {
    instanceID: {
      default: null
    },
    editInstance: {
      type: Object,
      default:null
    },
  },
  data() {
    return {
      mode: 'creation',
      form: {},
      proxyForm: {},
      instance: null
    }
  },
  methods: {
    beforeSet(instance) {  },
    afterSet(instance) {  },
    onClear(){},
    preProcessInstance(instance) { return instance },
    _setProxy() {
      this.proxyForm = { ...this.form }
    },
    _clearForm(done) {
      this.onClear()
      this.form = { ...this.proxyForm }
    },
    async _setFields(instance) {
      let inst = this.preProcessInstance(instance)
      let form = { ...this.proxyForm }
      if (inst) {
        for (var key in form) {
          form[key] = inst[key]
        }
        this.form = form
        this.mode = 'edition'
      } else {
        this.mode = 'creation'
      }
      this.afterSet(inst)
    },
  },
  mounted() {
    this._setProxy()
  }
}
