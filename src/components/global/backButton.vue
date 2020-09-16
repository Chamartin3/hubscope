<template lang="pug">
v-tooltip(left)
  template(v-slot:activator="{ on, attrs }")
    v-btn.mb-7(color='secondary'
    v-on="on"
    @click="goTo"
    dark large fixed  bottom right fab)
      v-icon fas fa-arrow-left
  span {{ mensaje }}
</template>
<script>
export default {
  name: 'BackButton',
  props: {
    to: {
      type: String,
      default: null
    },
    mensaje: {
      type: String,
      default: 'volver'
    }
  },
  methods: {
    goTo () {
      if (this.to) this.$router.push({ name: this.to })
      else this.$router.go(-1)
    }
  }

}
</script>
