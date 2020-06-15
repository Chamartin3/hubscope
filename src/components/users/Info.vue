<template lang="pug">
v-card
  ModalEdit(
    ref="ModalEdit",
    @successChange="setUser($event)"
    :editInstance="user"
    :action="action",
    :service="action",
  )
  PasswordForm(ref="PasswordForm")
  v-container.white(v-if="user")
    v-row.mt-n5.mb-5.justify-center.primary.white--text
      v-col.text-center(md="3" v-editable @edit="EditField('username')")
          p.headline.font-weight-bold
            | {{ user.username }}
    v-row.justify-center.white.black--text
      v-col.text-center(v-editable @edit="EditField('first_name', 'nombre')")
        h4.overline Nombres
          p.headline
            | {{user.first_name | nonempty }}
      v-col.text-center(v-editable @edit="EditField('last_name','apellido')")
        h4.overline Apellidos
          p.headline
            | {{user.last_name | nonempty }}
            //- EditableElement(")
    v-row.white.black--text
      v-col.text-center( v-editable @edit="EditField('email','email','email')")
          h4
            v-icon.mx-2 fa-at
            | {{user.email | nonempty }}
      v-col.text-center
        v-btn.primary(
          color="secondary"
          @click="$refs.PasswordForm.edit(user.id, {id:user.id})") Cambiar Contraseña
</template>
<script>
import ModalEdit from '@/components/base/ModalEdit'
import PasswordForm from './PasswordForm'
export default {
  name:"UserCard",
  props:{
    userInstance:{
      default:null
    }
  },
  components:{
    ModalEdit,
    PasswordForm
  },
  methods:{
    EditField(fieldname, name=null, type="text"){
      if (!name) name=fieldname
      this.$refs.ModalEdit.openDialog(fieldname, type, name)
    },
    setUser(user){
      if(this.id === user.id){
        this.$store.dispatch('accounts/getUserInfo', user.id)
      }

      this.$emit('cambio', user)
    },
  },
  computed: {
    user () {
      // console.log(this.$store.state)
      if(!this.userInstance) return this.$store.state.accounts.user
      else return this.userInstance

    },
    id () {
      return this.$store.state.accounts.user.id
    },
    action () {
      return this.$django.models.accounts.patch_information
    }
  },
  filters:{
    nonempty(val){
      if(val==='') return 'not defined'
      return val
    }
  }
}
</script>
