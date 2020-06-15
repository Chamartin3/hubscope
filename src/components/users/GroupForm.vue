<template lang="pug">
extends ../../layouts/templates/Modal/ModalForm
append content
  v-container(color="primary")
    .row.white--text
        .col
            GroupSelect(v-model="form.groupname")
</template>
<script>
import GroupSelect from './GroupSelect'
import { formModal } from '@/mixins/Modal'
export default {
  mixins: [ formModal ],
  components: { GroupSelect },
  data () {
    return {
      activator: false,
      model_name: 'Rol',
      modalColor:'primary',
      modalDark:true,
      editAction: 'patch_change_group',
      model: this.$django.models.accounts,
      form: {
        groupname: ''
      }
    }
  }
}
</script>
