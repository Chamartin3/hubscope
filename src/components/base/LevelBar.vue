<template lang="pug">
div
  div(class="pcontainer" style="height: 30px;")
    v-tooltip(bottom)
      template(v-slot:activator="{ on, attrs }")
        .bar(v-on="on" class="red" style="width:80%" )
      span Si la meta esta por debajo de {{ logro }} se considera mal (rojo)
    .bar(class="yellow" style="width:10%" )
    v-tooltip(bottom)
      template(v-slot:activator="{ on, attrs }")
        .bar(v-on="on" class="green" style="width:10%")
      span Si la meta esta por encima de {{ logro }} se considera bien (verde)

  div(class="pcontainer" style="height: 30px;")
</template>
<script>
export default {
  name: 'semaforo',
  props: ['logro', 'intermedio'],
  computed: {
    logrototal () { return this.logro * 1.1 },
    inter () { return this.logrototal * 0.9 },
    resto () {
      return this.logrototal * 0.9
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
