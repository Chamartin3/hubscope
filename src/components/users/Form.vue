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
    .row
      .col
        v-text-field(label="Email",
          :rules="[valrules.required]",
          prepend-icon='fa-at', v-model="form.email", :error-messages="errors.email")

    .row
      .col
        GroupSelect(v-model="form.group", :filtered="company")
      .col(v-if="companySelector && !company")
        CompanySelect(v-model="form.company")
      .col.text-center(v-if="company")
        v-chip(v-for="c in form.company") {{ c }} 
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
      .text-center.headline-1.white--text
        h2
          strong Nuevo Usuario

</template>
<script>
import { formModal } from '@/mixins/Modal'
import GroupSelect from './GroupSelect'
import CompanySelect from '@/components/empresas/Select'
export default {
  props: {
    fullmode: { default: false },
    company: { default: null },
    button: { default: false }
  },
  components: { GroupSelect, CompanySelect },
  mixins: [ formModal ],
  computed: {
    formTitle () {
      return 'Add new'
    }
  },
  watch: {
    'form.group': function (newVal) {
      if ( newVal === 'Gerente' || newVal === 'Registrador' ) {
        this.companySelector = true
      } else {
        this.companySelector = false
      }
    },
  },
  // mounted() {
  //   if (this.company) this.form.company.append(this.company)
  // },
  data () {
    return {
      activator:this.button,
      text:false,
      companySelector: false,
      maxWidth: null,
      modalTitle: 'Nuevo Usuario',
      modalColor: 'primary',
      modalDark: true,
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
        group: '',
        company:[this.company]
      }
    }
  }
}
</script>
