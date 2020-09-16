<template lang="pug">
extends ../../layouts/templates/Modal/ModalForm
block title
  v-card-title
    span.headline.white--text {{ formTitle }} {{ model_name }}
append content
  .row.text-center
    .col
      v-text-field(
        v-model="form.name",
        :errors="errors.name"
        placeholder="Nombre"
        label="Nombre"
      )
</template>
<script>
import { formModal } from '#/Modal'

export default {
  name: 'CompanyForm',
  mixins: [formModal ],
  data () {
    return {
      // activator:this.button,
      model_name: 'Organización (Empresa u Oficina)',

      model: this.$django.models.company,
      form: {
        name: ''
      }
    }
  }
}
</script>
