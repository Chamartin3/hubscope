<template lang="pug">
v-card
  v-container
    v-row
      v-col
        .overline Permisos
        v-chip(v-for="group in user.groups_info") {{ group.name }}
    v-row
      v-col
        .overline Ultimo Ingreso
        .headline {{ user.last_login | fulltime}}


</template>
<script>
import moment from 'moment'
export default {
  name: "",
  props:['user'],
  filters:{
    fulltime(val){
      let time =  moment(val).format('hh:mm a')
      let date =  moment(val).format('DDDD DD-MMMM')
      if (moment(val).isValid()){
        return `Ultimo ingreso el ${date} a las ${time}`
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
