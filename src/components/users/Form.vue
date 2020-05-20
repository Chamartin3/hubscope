<template lang="pug">
extends ../../layouts/templates/Modal/ModalForm
append content
  v-container.pa-5
    v-row
      v-col
        v-text-field(label="First name", v-model="form.first_name", :error-messages="errors.first_name", :rules="[valrules.required]")
      v-col
        v-text-field(label="Last name", v-model="form.last_name", :error-messages="errors.last_name", :rules="[valrules.required]")
    v-row
      v-col
        v-text-field(label="Username", v-model="form.username", :rules="[valrules.required]", :error-messages="errors.username")

    v-row
      v-col
        v-text-field(label="Email", :rules="[valrules.required]", prepend-icon='fa-at', v-model="form.email", :error-messages="errors.email")
    v-row
      v-col
        v-text-field(label="New password",
        type="password"
        v-model="form.password", :error-messages="errors.password", :rules="[valrules.required]")
      v-col
        v-text-field(label="Confirm password",
        type="password", v-model="form.passwordconf", :error-messages="errors.passwordconf", :rules="[valrules.required]")

    v-row(v-if="fullmode")
      v-col
        v-text-field(label="Telefono", prepend-icon='phone', :rules="[valrules.required]", v-model="form.phone", :error-messages="errors.phone")
      v-col
</template>
<script>
import { formModal } from '@/mixins/Modal'
export default {
  props: {
    fullmode: { default: false }
  },
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
    formTitle () { return 'Add new' }
  },
  data () {
    return {
      activator: true,
      maxWidth:null,
      model_name: 'user account',
      buttomText: 'Nuevo Usuario',
      createAction: 'registration',
      model: this.$django.models.accounts,
      form: {
        first_name: '',
        last_name: '',
        username: '',
        email: '',
        password: '',
        passwordconf: ''
      }
    }
  }
}
</script>
