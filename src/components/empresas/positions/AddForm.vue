<template lang="pug">
extends ../../../layouts/templates/Modal/ModalForm
append content
  v-container(color="primary")
    .row.white--text
        .col
            UserAutocomplete(v-model="user" :rules="false")
    .row(v-if="notAvariable")
      .col.text-center.red.lighten-4.red--text
        | Este usuario tiene el rol de {{notAvariable}} por lo tanto no puede ser asignado a ninguna empresa

    .row.white--text(v-else)
      .col
          GroupSelect(ref="GroupSelect" v-model="form.group", :filtered="true")

block actions
  v-btn(
    color="red darken-1",
    @click="close") Cancelar
  v-btn(
    color="green darken-1", 
    :disabled="!invalid", @click="sendForm") Guardar
</template>
<script>
import UserAutocomplete from '@/components/users/Autocomplete'
import GroupSelect from '@/components/users/GroupSelect'
import { formModal } from '@/mixins/Modal'
export default {
  mixins: [ formModal ],
  components: { 
    UserAutocomplete,
    GroupSelect
  },
  computed: {
    invalid () {
      return this.form.user && this.form.group
    }
  },
  watch: {
    user (val) {
      if (val) {
        let groups = val.groups.map(g => g.name)
        
        if (groups.length < 1) {
          this.form.user = val.id
          this.notAvariable = null

        } else if (groups.includes('Admin') || groups.includes('Ejecutivo')) {
          this.notAvariable = groups[0]
          this.form.user = null
          this.$refs.GroupSelect.value = null

        } else {
          this.notAvariable = null
          this.form.user = val.id
          this.$refs.GroupSelect.value = val.groups[0]

        }
      }
    }
  },
  data () {
    return {
      user: null,
      notAvariable: null,
      activator: false,
      customFormTitle: "Agregar empleado",
      model_name: 'Rol',
      modalColor:'primary',
      modalDark:true,
      editAction: 'addPersonel',
      mode:'edition',
      model: this.$django.models.company,
      form: {
        user: null,
        group:null
      }
    }
  }
}
</script>
