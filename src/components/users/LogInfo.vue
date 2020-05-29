<template lang="pug">
v-card
  .container
    GroupForm(ref="GroupForm" @edited="$emit('successChange',user)")
    .row.text-center
      .col(v-editable @edit="$refs.GroupForm.edit(user.id, {id:user.id})")
        .overline.mb-4 Permisos
        v-chip(v-for="group in user.groups") {{ group.name }}
      .col
        .overline.mb-4 Ultimo Ingreso
        p {{ user.last_login | fulltime}}


</template>
<script>
import moment from 'moment'
import GroupForm from './GroupForm'
export default {
  name: "",
  props:['user'],
  components: { GroupForm },
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
  data(){
    return {

    }
  }
}
</script>
