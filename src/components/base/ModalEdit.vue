<template lang="pug">
v-dialog(v-model='dialog' persistent='' max-width='290')
  v-card
    v-card-title.headline.text-center Editar {{fieldName}}
    v-card-text
      DynamicField(
        ref="field"
        :val="maped_value"
        :outErrors="errors"
        :type="fieldType"
        :name="fieldName"
        :itemOptions="options"
        v-model="form")
    v-card-actions
      .flex-grow-1.text-center
        v-btn(color='red darken-1' text='' @click='cerrar') Cancelar
        v-btn(color='green darken-1' text='' @click='sendForm') Modificar
</template>
<script>
import {baseMainForm} from '#/Forms'
import formAlertMixin from '#/Forms/formAlertMixin'

import DynamicField from './DynamicField'
export default {
  mixins:[baseMainForm, formAlertMixin],
  components:{ DynamicField },
  props:{
    action:{},
    service:{required:false}
  },
  data(){
    return {
      dialog:false,
      form:{},
      fieldType:'text',
      fieldName:'',
      fieldModel:'',
      options:[]
    }
  },
  computed:{
    map(){
      return this.fieldModel ? this.fieldModel.split(".") : []
    },
    maped_value(){
      return this.get_mapped(this.instance)
    },
    maped_errors(){
      return this.get_mapped(this.errors)
    },
  },
  methods:{
    get_mapped(value){
      if(value && Object.keys(value.length>0)){
        let lvl
        for (var i = 0; i <this.map.length; i++) {
          lvl = this.map[i]
          value = value[lvl]
        }
        return value
      }
      return null
    },
    preProcessForm (form) {
      let list = this.map
      var pre = {}
      var final = {}
      for (var i = list.length-1; i >= 0; i--) {
        pre = {}
        if ( i == list.length-1 ) {
           pre[list[i]] = form.val
        } else {
          pre[list[i]] = final
        }
        final = pre
      }
      return final
     },
    openDialog (model, type=null, name=null, options=[]) {
      if(type) this.fieldType = type
      if(name) this.fieldName = name
      if(options) this.options = options
      if(type=='color') this.form.val=""
      if(type=='image') this.form.val=""
      this.fieldModel = model
      this.dialog = true
    },
    exito(done){
      this.cerrar()
      this.$emit('successChange',done)
    },
    cerrar () {
      this.fieldType = null
      this.$refs.field.form.val=null
      this.fieldName = null
      this.fieldModel = null
      this.dialog = false
    },
    sendForm() {
      let self = this
      let form = this.preProcessForm(this._preProcessForm())
      this._beforeSend()
      this.beforeSend()
      this.action(this.instance.id, form).then(
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
  },
  mounted () {
    // this.instanceID=this.id
    // this.instance.id = this.id
    this.actionsOnSuccess.push(this.exito)

  },

}
</script>
