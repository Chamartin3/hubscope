import { baseMainForm, errorsMixin } from '#/Forms'
import formAlertMixin from '#/Forms/formAlertMixin'
export default {
  mixins: [baseMainForm, formAlertMixin, errorsMixin ],
  data () {
    return {
      customFormTitle: '',
      instance: null
    }
  },
  methods: {
    onClose () {

    },
    beforeSend () {
      this._validateForm()
      this.loading = true
    },
    stopLoading () {
      this.loading = false
    },
    open () {
      this.clearAll()
      this.dialog = true
      this.inErrors = {}
    },
    success (item) {
      if (this.mode == 'creation') {
        this.$emit('created', item)
      } else {
        this.$emit('edited', item)
      }
      this.close()
      this.onClose()
    },
    close () {
      this.onClose()
      this.clearAll()
      this._resetValidation()
      this.dialog = false
      this.instance = null
      this.mode = 'creation'
    },
    edit (id, instance = null) {
      this.mode = 'edition'
      if (instance) {
        this.instance = instance
        this._setFields(instance)
      } else this._fetchInst(id)
      this.dialog = true
    }
  },
  computed: {
    formTitle () {
      if (this.customFormTitle) return this.customFormTitle
      if (this.mode === 'creation') return 'Crear'
      return 'Editar'
    }
  },
  mounted () {
    this.actionsOnSuccess.push(this.success)
    this.actionsOnSuccess.push(this.stopLoading)
    this.actionsOnFail.push(this.stopLoading)
  }
}
