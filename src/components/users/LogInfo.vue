<template lang="pug">
v-card.white.black--text
  .container.white.black--text
    GroupForm(ref="GroupForm" @edited="$emit('successChange',user)")
    CompanyForm(
      ref="CompanyForm" 
      :user="user"
      @created="refresh($event)"
      :group="user.groups[0].name" 
      :companies="user.roles.map(r => r.company)")
    .row.text-center
      .col(v-editable @edit="$refs.GroupForm.edit(user.id, {id:user.id})")
            .overline.mb-4 Permisos
            v-chip.pa-5(label small )
              .headline  {{  mainRole }}
      .col(
        v-if="!['Admin', 'Ejecutivo'].includes(mainRole)"
        v-editable @edit="$refs.CompanyForm.open()")
            .overline.mb-4 Empresa
            v-chip.pa-5(small pill v-for="pos in user.roles")
              .overline  {{  pos.company }}

      .col
        .overline.mb-4 Ultimo Ingreso
        p {{ user.last_login | fulltime}}


</template>
<script>
import moment from 'moment'
import GroupForm from './GroupForm'
import CompanyForm  from '@/components/empresas/positions/AddCompany.vue'
export default {
  name: "",
  props:['user'],
  components: { GroupForm, CompanyForm},
  filters:{
    fulltime(val){
      let time =  moment(val).format('hh:mm a')
      let date =  moment(val).format('DD-MMMM')
      if (moment(val).isValid()){
        return `${date} a las ${time}`
      }else {
        return 'No hay registros de ingreso'
      }
    }
  },
  computed: { 
    mainRole(){
      return this.user.groups[0].name
    }
  },
  methods: {
    refresh(data) {
      this.$emit('cambio')
      this.user.roles=data
    }
  },
  data(){
    return {
      empresas:null,
    }
  }
}
</script>
