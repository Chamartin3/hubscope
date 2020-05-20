<template lang="pug">
extends ../../mixins/Modal/ModalForm
append content
  v-container
    v-row
      v-col
        v-text-field(label="New password",
        type="password"
        v-model="form.password", :error-messages="errors.password", :rules="[valrules.required]")
    v-row
      v-col
        v-text-field(label="Confirm password",
        type="password", v-model="form.passwordconf", :error-messages="errors.passwordconf", :rules="[valrules.required]")
</template>
<script>
import modalFormMixin from '@/mixins/Modal/modalFormMixin'
export default {
  mixins: [ modalFormMixin ],
  data () {
    return {
      activator: false,
      model_name: 'Password',
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
