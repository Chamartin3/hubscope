<template lang='pug'>
v-card.pointer(dark color='primary lighten-1')
  .container
    .row.text-center
      .col
        .display-1 {{ name }}
    hr
    .row.text-center.mx-2
      .col
        .overline Proximo vencimiento
    .row.text-center.mx-2
      .col
        .overline    
        strong {{ asignment.deadline_date }}  
    .row.text-center.mx-2
      .col
        .overline Frecuencia
    .row.text-center.mx-2
      .col
        .overline
        strong {{ frecuencyText }}
</template>
<script>
export default {
  name: 'asignmentCard',
  props:['asignment'],
  data() {
    return {
      weekdays: [
        'Lunes',
        'Martes', 
        'Miercoles',
        'Jueves',
        'Viernes',
        'Sabbados',
        'Domingos'
      ],
    }
  },
  computed:{
    name(){
      return this.asignment.metric_info.name
    },
    selectedText(){

      if(this.asignment.frecuency==='DAY') return this.asignment.metafreq
      let days =  this.asignment.metafreq.split(',')
      let last = days.pop()
      const self = this
      if(this.asignment.frecuency==='MONT') {
        if(days.length<1) return last
        return days.join(',')+' y '+last
      }
      if(this.asignment.frecuency==='WEEK') {
        if(days.length<1) return self.weekdays[last]
        return days.map(d => self.weekdays[d]).join(',')+' y '+ self.weekdays[last]
      }
    },
    frecuencyText(){
      if(!this.selectedText) return null
      if(this.asignment.frecuency === 'MONT') {
        return `Los ${this.selectedText} de cada mes`
      }
      if(this.asignment.frecuency === 'WEEK') {
        return `Semanalmente los ${this.selectedText}`
      }
      if(this.asignment.frecuency === 'DAY') {
        return `Cada ${this.selectedText} dias`
        
      }     
      return 'solo una vez'
    }
  }
}
</script>