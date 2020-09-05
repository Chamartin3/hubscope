<template lang="pug">
div
  div(class="pcontainer" style="height: 30px;")

    v-tooltip(bottom)
      template(v-slot:activator="{ on, attrs }")
        .bar(v-on="on" class="red", :style="'width:'+barraFallida*100+'%'" )
      span(v-if="intermedio") Si la meta esta por debajo de {{ medium | number }} se considera mal (rojo)
      span(v-else) Si la meta esta por debajo de {{ logro | number }} se considera mal (rojo)

    v-tooltip(bottom v-if="intermedio")
      template(v-slot:activator="{ on, attrs }")
        .bar(v-on="on" class="yellow", :style="'width:'+barraIntermedia*100+'%'" )
      span Si la meta esta entre {{ logro | number }} y  {{ medium | number }} se considera intermedio (amarillo)

    v-tooltip(bottom)
      template(v-slot:activator="{ on, attrs }")
        .bar(v-on="on" class="green" :style="'width:'+winSize*100+'%'" )
      span Si la meta esta por encima de {{ logro | number }} se considera bien (verde)

  div(class="pcontainer" style="height: 30px;")
    span.overline.red--text(
      v-if="intermedio"
      :style="'margin-left:'+(barraFallida*100)+'%'") {{  intermedio | number  }}
    span.overline.yellow--text(
      :style="'margin-left:'+(barraIntermedia*100-5)+'%'") {{  logro | number  }}
</template>
<script>
export default {
  name: 'Semaforo',
  filters: {
    number: val => Intl.NumberFormat('es-VE').format(val)
  },
  props: ['logro', 'intermedio'],
  data () {
    return {
      failSize: 0.75
    }
  },
  computed: {
    medium () {
      if (this.intermedio) return parseInt(this.intermedio)
      return null
    },
    winSize () { return 1 - this.failSize },
    totalBar () { return this.logro * (1 + this.winSize) },
    barreraLogro () { return this.totalBar * this.failSize },
    barraIntermedia () {
      return this.failSize - this.barraFallida
    },
    barraFallida () {
      if (!this.intermedio) return this.failSize
      let perc = this.intermedio / this.totalBar
      if (perc > this.failSize) return this.failSize
      else return perc
    }
  }
}
</script>
<style>
.pcontainer {
  border-radius: 16px;
  overflow: hidden;
  width: 100%;
}
.bar {
  display: inline-block;
  right: 100%;
  height: inherit;
  transition: inherit;
}

</style>
