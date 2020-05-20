<template lang="pug">
v-snackbar(
  v-model="snackbar",
  :color="style.color",
  top,
  :timeout="30000",
  :dark="style.textColor!='black'")
  v-icon.mr-3(:color="style.textColor")
    | {{style.icon}}
  |
  div
    .headline {{tit}}
    |  {{msg}}
  |
  v-btn(icon
    :color="style.textColor",
   @click="snackbar = false")
    v-icon fa-times
</template>
<script>
export default {
  name: 'Alert',
  data () {
    return {
      snackbar: false,
      tit: '',
      msg: '',
      style: {
        color: '',
        icon: '',
        textColor: ''
      }
    }
  },
  methods: {
    alert (type, tit, msg = '') {
      let style = {}
      if (type === 'danger') {
        style.color = 'red'
        style.textColor = 'white'
        style.icon = 'fas fa-exclamation'
      }
      if (type === 'warning') {
        style.color = 'rgb(179, 161, 0)'
        style.textColor = 'white'
        style.icon = 'fas fa-exclamation-triangle'
      }
      if (type === 'success') {
        style.color = 'green'
        style.textColor = 'white'
        style.icon = 'fas fa-check-circle'
      }
      this.snackbar = true
      this.style = style
      this.tit = tit
      this.msg = msg
    }
  }
}
</script>
