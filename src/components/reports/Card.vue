<template lang='pug'>
.container
  .row.text-center
    .col(v-if="report.value")
      .display-1
        | {{ report.value | number }}
      .overline(v-if="report.value")
        .headline {{ report.metric.unidad }}
      .overline
        | {{ report | period }}
      .overline
        | ({{ report | days }} )
      
    .col(v-else)
      .display-1
        | Pendiente
      .overline
        | Fecha esperada de reporte
      .overline
        | Despues del {{ report.end | date }}
      .overline
        | Antes del {{ report.deadline | date }}
      .overline(:class="{'red--text':report.delayed}")
        h3.font-weight-bold ({{ report.end | days_until }})
    .col(v-if="report.value")
      .text-center
        .overline Registrado por
        .subtitle-1.pointer(@click="$emit('user', report.registered_by )")
          | {{ report.registered_by | nulluser}}
      .text-center.mt-3(v-if="")
        .overline Modificado:
        .overline {{ report.updated_at | date  }}
        .subtitle-1.pointer(@click="$emit('user',report.modified_by )")
          |{{ report.modified_by | nulluser}}

    .col.align-center
      .text-center
        v-btn.ma-1.gray(color="secondary lighten-1"
          @click="$emit('editReport',report.id)" small)
          v-icon.mr-2(x-small) far fa-edit
          | Modificar
      .text-center
        v-btn.ma-1(
          color="secondary darken-2" 
          @click="$emit('deleteReport',report.id)" small)
          v-icon.mr-2(x-small) far fa-trash-alt
          | Eliminar
          
  //- td(:colspan='headers.length')
  //-     .container
  //-       .row
  //-         .col Periodo  {{ item | period }}        
  //-       .row
  //-         .col Registrado el {{item.created_at | datetime}}
  //-       .row
          //- .col Registrado Por {{item.registered_by}}      

</template>
<script>
import moment from 'moment'
import reportStatus from './Status'
export default {
  name: 'reportCard',
  props:['report'],
  components: { reportStatus },
  filters:{
    nulluser(user){
      if (user) return user.fullname
      return 'Sistema Automatizado'

    },
    period(item){
      let begin = moment(item.begin).format('DD MMM-YYYY')
      let end = moment(item.end).format('DD MMM-YYYY')
      return `${begin} - ${end}`
    },    
    days(item){
      if(item.days===1) return `${1} dia` 
      return `${item.dias} dias`
    },
    date(time){
      return moment(time).format('dddd, DD MMMM YYYY')
    },    
    days_until(time){
      let dias = moment(time).diff(moment(),'days')
      if(dias===0) return `Hoy` 
      let text
      if(dias<0){
        dias = -dias
        text = `Hace ${dias} `
      }else{
        text = `Dentro de ${dias} `
      }
      if (dias==1) return text+'dia'
      return text+'dias'
    },
    number(num){
      return parseInt(num).toLocaleString()
    }
  }
}
</script>