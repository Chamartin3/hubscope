<template lang='pug'>
v-tooltip(bottom)
        template(v-slot:activator="{ on, attrs }")
          v-chip(v-on="on" :color="color")
            | {{ name }}
        span {{ desc }}
</template>
<script>
export default {
  props: ['status'],
  computed:{
    desc(){ 
      return this[this.status].desc
    },
    name(){ 
      return this[this.status].name 
    },
    color(){ 
      return this[this.status].color 
    },
  },
  data() {
    return {
      cerrada:{
        'color':'gray',
        'name':'Cerrado',
        'desc':'El reporte no puede ser modificado'
      },
      entregada:{
        'color':'green',
        'name':'Entegado',
        'desc':'El reporte ya fué entregado'
      },
      esperando:{
        'color':'secondary lighten-1',
        'name':'Evaluando',
        'desc':'El reporte aun esta dentro de los tiempos estipulados'
      },
      abierta:{
        'color':'yellow',
        'name':'En Espera',
        'desc':'Esperando porl a entrega del reporte'
      },
      atrasada:{
        'color':'red',
        'name':'Atrasado',
        'desc':'El reporte no se ha entregado a tiempo'
      }
    }
  }
}
</script>