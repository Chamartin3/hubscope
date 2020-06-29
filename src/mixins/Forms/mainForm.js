export default {
  data() {
    return {
      mode: 'creation',
      model:null,
      createAction:'create',
      editAction:'partial_update',
      instanceAction:'retrieve',
      actionsOnFail: [],
      actionsOnSuccess: [],
      editMode:true,
      valid:true,
      formRef:'_formWrapper',
      valrules:{
        required: v => !!v || 'Campo Requerido.',
        min: v => v.length >= 4 || 'Minimo 4 caracteres',
        max: v => v.length <= 4 || 'Maximo 4  caracteres',
      },
      extraValidations:[],
    }
  },
  watch:{
    editInstance(val){
      if (Object.keys(this.editInstance).length === 0 && this.editInstance.constructor === Object ) {}else{
        this._setInstance()
      }

    }
  },
  methods: {
    async _fetchInst(id) {
      this.instance = await this.model[this.instanceAction](id)
    },
    async _setInstance() {
      // Look for the id in the props
      // if(this.editInstance && this.fetchInstance){
        //   console.error('You should not fetch an object if you are giving one to edit')
        // }
      if (this.editMode){

        if (this.editInstance) {
          if (Object.keys(this.editInstance).length != 0) {
            this.instance = {...this.editInstance}
          }
        }else{
          let id = this.instanceID ? this.instanceID :
          null
          if (id) await this._fetchInst(id)
        }

        this._setFields(this.instance)
      }
    },
    beforeSend() { },
    _beforeSend() { this._validateForm()},
    _resetValidation(){
      if(this.$refs[this.formRef]){
        this.$refs[this.formRef].resetValidation()
      }
    },
    _validateForm(){
      for (var i = 0; i < this.extraValidations.length; i++) {
        if(!this.extraValidations[i]()) return false
      }

      if(this.$refs[this.formRef]){
        return this.$refs[this.formRef].validate()
      }else{
        return true
      }
    },
    sendForm() {
      let self = this
      let form = this.preProcessForm(this._preProcessForm())
      this._beforeSend()
      this.beforeSend()
      if (this._validateForm()) {
        if (this.mode === 'creation') this._sendCreate(form)
        else this._sendEdit(form)
      } else {
        self.failedSend({message:'Errores en formulario'})
      }
    },
    preProcessForm(form) { return form },
    _preProcessForm() { return this.form },
    successSend(success) { },
    _successSend(data) {
      this.successSend(data)
      for (var i = 0; i < this.actionsOnSuccess.length; i++) {
        this.actionsOnSuccess[i](data)
      }
    },
    failedSend(fail) {},
    _failedSend(fail) {
      this.failedSend(fail)
      for (var i = 0; i < this.actionsOnFail.length; i++) {
        this.actionsOnFail[i](fail)
      }
    },
    clearAll(done) {
      if (this.mode === 'creation') {
        this._clearForm()
        for (var i = this.$children.length - 1; i >= 0; i--) {
          if (this.$children[i].subForm) this.$children[i]._clearForm()
        }
        // instance
        // this._setFields(this.proxyForm)
      } else {
        if (this.edit_form_var) {
          this.edit_form_var = false
        }
      }
    },
    _sendCreate(form){
      const self=this
      this.model[this.createAction](form).then(
        done=>self._successSend(done),
        fail=>self._failedSend(fail.response))
    },
    _sendEdit(form){
      let id=this.instance.id
      this.model[this.editAction](id,form).then(this._successSend, this._failedSend )
    },
    processSubForm(value, name=null){
      if (name) this.form[name] = value
      else Object.assign(this.form, value)
    },
  },
  mounted() {
    this._setInstance()
    this.actionsOnSuccess.push(this.clearAll)
  }
}


const Legacy = {
  props:{
    service:{
      type:Object,
      required:true
    },
  },
  data() {
    return {
      mode: 'creation',
      actionsOnFail: [],
      actionsOnSuccess: [],
      editMode:true,
      valid:true,
    }
  },
  watch:{
    editInstance(val){
      if (Object.keys(this.editInstance).length === 0 && this.editInstance.constructor === Object ) {}else{
        this._setInstance()
      }

    }
  },
  methods: {
    async _fetchInst(id) {
      this.instance = await this.service.retrieve(id)
    },
    async _setInstance() {
      if (this.serviceProp) {
        this.service = this.serviceProp
      }
      // Look for the id in the props
      // if(this.editInstance && this.fetchInstance){
        //   console.error('You should not fetch an object if you are giving one to edit')
        // }
      if (this.editMode){


        if (this.editInstance) {
          if (Object.keys(this.editInstance).length != 0) {
            this.instance = {...this.editInstance}
          }
        }else{
          let id = this.instanceID ? this.instanceID :
          this.$route.params.id ? this.$route.params.id :
          null
          if (id) await this._fetchInst(id)
        }

        this._setFields(this.instance)
      }
    },
    beforeSend() { },
    _beforeSend() { },
    preProcessForm(form) { return form },
    _preProcessForm() { return this.form },
    successSend(success) { },
    _successSend(data) {
      for (var i = 0; i < this.actionsOnSuccess.length; i++) {
        console.log('action number'+i)
        this.actionsOnSuccess[i](data)
      }
    },
    failedSend(fail) { },
    _failedSend(fail) {
      for (var i = 0; i < this.actionsOnFail.length; i++) {
        this.actionsOnFail[i](fail)
      }
    },
    clearAll(done) {
      if (this.mode === 'creation') {
        this._clearForm()
        for (var i = this.$children.length - 1; i >= 0; i--) {
          if (this.$children[i].subForm) this.$children[i]._clearForm()
        }
        // instance
        // this._setFields(this.proxyForm)
      } else {
        if (this.edit_form_var) {
          this.edit_form_var = false
        }
      }
    },
    sendForm() {
      let self = this
      let form = this.preProcessForm(this._preProcessForm())
      this._beforeSend()
      this.beforeSend()
      if (this.mode === 'creation') {
        this.service.create(form).then(
          done => {
            self._successSend(done)
            self.successSend(done)
          },
          fail => {
            self._failedSend(fail)
            self.failedSend(fail)
          })
      } else {
        this.service.partial_update(this.instance.id, form).then(
          done => {
            self._successSend(done)
            self.successSend(done)
          },
          fail => {
            self._failedSend(fail)
            self.failedSend(fail)
          }
        )
      }
    }
  },
  mounted() {
    this._setInstance()
    this.actionsOnSuccess.push(this.clearAll)
  }
}
