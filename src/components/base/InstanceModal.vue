<template lang="pug">
v-dialog(v-model="dialog", max-width="500px")
  template(v-slot:activator="{ on }")
    v-btn.mb-2(color="primary", dark, v-on="on") {{buttomText}}
  |
  v-card
    v-card-title
      span.headline {{ formTitle }}
    |
    v-card-text
      v-container
    |
    v-card-actions
      v-spacer
      |
      v-btn(color="red darken-1", text, @click="close") Cancel
      |
      v-btn(color="green darken-1", text, @click="save") Save
</template>
<script>
export default {
  name: "InstanceModal",
  props:['service', 'boton'],
  data(){return {
    instance:{},
    editedIndex:-1,
    dialog:false,
    newItem:null,
  }},
  methods:{
   close () {
     this.dialog = false
     setTimeout(() => {
       this.editedItem = Object.assign({}, {})
       this.editedIndex = -1
     }, 300)
   },
   edit(instance, index=-1){
     this.instance=instance
     this.editedIndex = index,
     this.dialog=true
   },
   save () {
     let newItem=this.instance
     if (this.editedIndex > -1) {
       this.$emit('cambio',{
         index:this.editedIndex,
         item:this.instance
       })
     } else {
       this.$emit('nuevo', this,item)
     }
     this.close()
   },
  },
  computed:{
    formTitle () {
      return this.editedIndex === -1 ? 'Nuevo' : 'Editar'
    },
    buttomText(){let text=this.boton ? this.boton :'Nuevo'; return text},
  }
}
</script>
