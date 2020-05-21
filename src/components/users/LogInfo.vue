<template lang="pug">
v-card
  v-container
    .row.text-center
      .col
        .overline.mb-4 Permisos
        v-chip(v-for="group in user.groups") {{ group.name }}
      .col
        .overline.mb-4 Ultimo Ingreso
        p {{ user.last_login | fulltime}}


</template>
<script>
import moment from 'moment'
export default {
  name: "",
  props:['user'],
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
