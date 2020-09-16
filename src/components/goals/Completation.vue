<template lang='pug'>
v-tooltip(bottom)
  template(v-slot:activator="{ on, attrs }")
    div
      v-chip.mx-4(small @click="action" v-on="on" :color="color")
        .overline {{ text }}
      DeleteConfirmation(
        @success="$emit('completed')"
        model="goal"
        method="complete"
        ref="closeConf"
        customMessage="¿Desea cerrar esta meta? se cerraran todos los reportes")
      DeleteConfirmation(
        @success="$emit('reopened')"
        model="goal"
        method="reopen"
        ref="openConf"
        customMessage="¿Desea reabrir esta meta? se reabriran todos los reportes")
  span {{ message }}

</template>
<script>
export default {

  name: 'GoalCompletation',
  props: ['id', 'completation'],
  data () {
    return {
      dialog: false,
      loading: false
    }
  },
  computed: {
    text () {
      if (this.completation) return 'Completado'
      return 'abierto'
    },
    color () {
      if (this.completation) return 'gray'
      return 'green'
    },
    message () {
      if (this.completation) return 'El periodo esta cerrado, no puede recibir modificaciones'
      return 'El periodo esta abierto, para enviar reportes y modificaciones'
    },
    // action () {
    //   if (this.completation) return 'Abrir'
    //   return 'Cerrar'
    // },
    confirmation () {
      if (this.completation) return 'Al abrir este periodo se podran modificar los reportes, y se hará visible en lapagina principal'
      return 'Al cerrar este periodo, no se podra modificar los reportes asociados, y dejara de ser visible en la pagina principal'
    }
  },
  methods: {
    action () {
      if (!this.completation) this.$refs.closeConf.open(this.id)
      else this.$refs.openConf.open(this.id)
    },
    async send () {
      this.loading = true
      let res = await this.$django.models.goal.toggleStatus(this.id)
      this.loading = false
      this.dialog = false
      this.$emit('changed')
      this.$alert('success', 'success', res.message)
    }
  }
}
</script>
