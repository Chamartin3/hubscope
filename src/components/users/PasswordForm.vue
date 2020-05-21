<template lang="pug">
extends ../../layouts/templates/Modal/ModalForm
append content
  v-container
    v-row
      v-col
        v-text-field(label="Nueva contraseña",
        type="password"
        v-model="form.password", :error-messages="errors.password", :rules="[valrules.required]")
    v-row
      v-col
        v-text-field(label="Confirmar contraseña",
        type="password", v-model="form.passwordconf", :error-messages="errors.passwordconf", :rules="[valrules.required]")
</template>
<script>
import { formModal } from '@/mixins/Modal'
export default {
  mixins: [ formModal ],
  data () {
    return {
      activator: false,
      model_name: 'Contraseña',
      editAction: 'patch_change_password',
      model: this.$django.models.accounts,
      form: {
        password: '',
        passwordconf: ''
      }
    }
  }
}
</script>
