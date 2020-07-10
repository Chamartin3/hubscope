<template lang='pug'>
span
  v-tooltip(bottom)
    template(v-slot:activator="{ on, attrs }")
      v-icon.sbulb(v-on="on" :class="status+'color'" :color="color" ) fa-circle
    span {{ message }}

</template>
<script>
const goalStatuses = {
  'good':{
    color:"success"
  },
  'medium':{
    color:"warning"
  },
  'bad':{
    color:"red"
  },
}
export default {
  name: 'GoalStatus',
  props:['status', 'indicatorname'],
  computed:{
    color(){
      return goalStatuses[this.status].color
    },
    message(){
      let msj
      if(this.status == 'bad') msj = "esta lejos de cumplirse"
      if(this.status == 'medium')  msj = "requiere ajustes"
      if(this.status == 'good') msj = "va bien"
      return `El indicador ${this.indicatorname} ${msj} `
    }
  }
}
</script>
<style>
tbody tr:nth-of-type(odd) {
   background-color: rgba(0, 0, 0, .05);
 }
 .sbulb:hover:before {
  transform: scale(1.2);
  filter: blur(2px);
}

.mediumcolor {
  text-shadow: 0 0 6px #d19e04;
}

.badcolor {
  text-shadow: 0 0 6px red;
}

.goodcolor {
  text-shadow: 0 0 6px green;
}
</style>