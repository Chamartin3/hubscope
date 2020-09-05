<template lang='pug'>
v-tooltip(bottom)
  template(v-slot:activator="{ on, attrs }")
    div
      v-chip.mx-4(small @click="dialog=true" v-on="on" :color="color")
        .overline {{ text }}
      v-dialog(v-model="dialog", max-width="350")
        v-card.text-center.pa-5(color="primary" dark)
          .text-center
            v-icon.my-5(size="50") fa-exclamation-triangle
          v-card-text.text-center
            p.headline ¿Desea {{action}} este periodo?
            p {{confirmation}}
          v-card-actions.justify-space-around
            v-btn(
              color="error",
              @click.native="dialog=false") Cancelar
            v-btn(
              color="success",
              :loading="loading"
              @click.native="send") Confirmar
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
    action () {
      if (this.completation) return 'Abrir'
      return 'Cerrar'
    },
    confirmation () {
      if (this.completation) return 'Al abrir este periodo se podran modificar los reportes, y se hará visible en lapagina principal'
      return 'Al cerrar este periodo, no se podra modificar los reportes asociados, y dejara de ser visible en la pagina principal'
    }
  },
  methods: {
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
