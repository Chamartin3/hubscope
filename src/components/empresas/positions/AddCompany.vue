<template lang="pug">
extends ../../../layouts/templates/Modal/ModalForm
append content
  v-container(color="primary")
    .row.white--text
        .col
            CompanySelect(ref="SelectCompany" :preset="companies" v-model="form.companies")
</template>
<script>
import CompanySelect from '@/components/empresas/Select.vue'
import { formModal } from '@/mixins/Modal'
export default {
  mixins: [ formModal ],
  components: { CompanySelect },
  props:['user', 'companies', 'group'],
  methods: {

  },
  data () {
    return {
      company:null,
      activator: false,
      model_name: 'Position',
      modalColor:'primary',
      modalDark:true,
      createAction: 'manyCompaniesPersonel',
      customFormTitle: "Agregar a empresa",
      model: this.$django.models.company,
      form: {
        companies: this.companies,
        user: this.user.id,
        group: this.user.groups[0].name
      }
    }
  }
}
</script>
