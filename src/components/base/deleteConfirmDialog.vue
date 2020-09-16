<template lang="pug">
  v-dialog(v-model="dialog", max-width="350")
    v-card.text-center.pa-5(color="primary" dark)
      .text-center
        v-icon.my-5(size="50") fa-exclamation-triangle
      |
      v-card-text.text-center
        p.headlin(v-if="customMessage" ) {{ customMessage }}
        p.headline(v-else) Desea eliminar este {{type!='' ? type: 'elemento'}}
      |
      v-card-actions.justify-space-around
        v-btn(
          color="error",
          @click.native="close()") Cancelar
        |
        v-btn(
          color="success",
          :loading="loading"
          @click.native="send") Confirmar
</template>
<script>
export default {
  props: {
    model: {
      type: String,
      required: true
    },
    method: {
      type: String,
      default: 'destroy',
      required: false
    },
    customMessage: {
      type: String,
      default: null,
      required: false
    }
  },
  data () {
    return {
      loading: false,
      dialog: false,
      type: '',
      service: null,
      id: null
    }
  },
  computed: {
    deleteMethod () {
      return this.$django.models[this.model][this.method]
    }
  },
  methods: {
    open (id, type = '') {
      this.dialog = true
      this.type = type
      this.id = id
    },
    close () {
      this.service = null
      this.id = null
      this.type = ''
      this.dialog = false
    },
    async send () {
      this.loading = true
      let res = await this.deleteMethod(this.id)
      this.$emit('success', this.id)
      this.close()
      this.loading = false
    }
  }
}
</script>
<style>
.circle-icon {
  font-size: 300px;

}
</style>
