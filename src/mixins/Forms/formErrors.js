try {
  const _ = require('lodash');
}

catch(error){

  console.log('There is an error importing lodash please enssure that you have that depdendencý')
  console.log(error)

}
const errorsMixin = {
  data () {
    return {
      inErrors: {},
      actionsOnFail: [],
      actionsOnSuccess: [],
      OERR:{}
    }
  },
  methods: {
    setInErrors (errors = {}) {
      if (typeof errors != 'object') errors = {}
      if (errors.data) errors = errors.data
      let e
      if( Object.keys(errors).length>0 ) e = errors
      else e = {}

      this.$set(this, 'inErrors', e)
    },
    cleanInErrors (){ this.setInErrors() },
    filterDatabaseError (error) {
      let transformed = error
      if (typeof error === 'object' && error[0]) { error = error[0] }
      if (error === 'Clave primaria "0" inválida - objeto no existe.') {
        transformed = 'Registro no existe en la base de datos'
      }
      return transformed
    },
  },
  props: {
    outErrors: {
      default: function () { return {} },
      type: [Object, String]
    }
  },
  watch: {
    _compForm:{
      deep:true,
      handler: function (val, oldVal){
        let changedFields = []
        const self = this
        
        Object.entries(oldVal).forEach(function([key, oldvalue]) {
          if (val[key]!=oldvalue) changedFields.push(key)
        })

        let proxyerrors = { ...self.inErrors }
        for (let k = 0; k < changedFields.length; k++) {
          delete proxyerrors[changedFields[k]]
        }       
        self.setInErrors(proxyerrors)
      },
    },
    outErrors:{
      deep: true,
      handler: function (val){
        let out = {}        
        if (typeof val  === 'string') {
          for (var inst in this.form) { out[inst] = val }
          this.OERR = out
        } else {
          this.OERR = Object.assign(out, val)
        }
      }     
    }
  },
  computed: {
    _compForm () {
      return Object.assign({}, this.form)
    },
    errors () {
      let merged = Object.assign(this.inErrors, this.OERR )  
      let mergedFiltered = {}
      Object.entries(merged).forEach(([key, value]) => {
        let newVal = this.filterDatabaseError(value)
        mergedFiltered[key] = Array.isArray(newVal) ? newVal.join(',') : newVal
      })
      return mergedFiltered
    }
  },
  created () {
    this.actionsOnFail.push(this.setInErrors)
    this.actionsOnSuccess.push(this.cleanInErrors)
  }
}

export default errorsMixin
