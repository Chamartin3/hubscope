<template lang="pug">
extends ../../layouts/templates/Modal/ModalForm
append content
  .container.pa-5.theme--dark
    .row
      .col
        v-text-field(label="Nombres",
          v-model="form.first_name",
          :error-messages="errors.first_name", :rules="[valrules.required]")
      .col
        v-text-field(label="Apellidos",
          v-model="form.last_name",
          :error-messages="errors.last_name", :rules="[valrules.required]")
    .row
      .col
        v-text-field(label="Nombre de Usuario",
          v-model="form.username",
          :rules="[valrules.required]", :error-messages="errors.username")
      .col
        GroupSelect(v-model="form.group")

    .row
      .col
        v-text-field(label="Email",
          :rules="[valrules.required]",
          prepend-icon='fa-at', v-model="form.email", :error-messages="errors.email")
    .row
      .col
        v-text-field(label="Nueva contraseña",
          type="password"
          v-model="form.password", :error-messages="errors.password"
          :rules="[valrules.required]")
      .col
        v-text-field(label="Confirmar contraseña",
          type="password", v-model="form.passwordconf"
          :error-messages="errors.passwordconf", :rules="[valrules.required]")


block title
  v-card-title(color="primary")
    .col.primary
      .text-center.display-1.white--text
        strong Nuevo Usuario

</template>
<script>
import { formModal } from '@/mixins/Modal'
import  GroupSelect from './GroupSelect'
export default {
  props: {
    fullmode: { default: false }
  },
  components: { GroupSelect },
  mixins: [ formModal ],
  methods: {
    // sendForm() {
    // if (this._validateForm()) {
    //     this.$emit('added',this.form)
    //     this.exito()
    //   }
    // },
  },
  computed: {
    formTitle () {
      return 'Add new'
    }
  },
  data () {
    return {
      activator: true,
      maxWidth: null,
      modalTitle: 'Nuevo Usuario',
      modalColor:'primary',
      modalDark:true,
      model_name: 'Usuario',
      buttomText: 'Nuevo Usuario',
      createAction: 'registration',
      model: this.$django.models.accounts,
      form: {
        first_name: '',
        last_name: '',
        username: '',
        email: '',
        password: '',
        passwordconf: '',
        group: ''
      }
    }
  }
}
</script>
