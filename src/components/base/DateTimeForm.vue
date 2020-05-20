<template lang="pug">
v-row.justify-center
  v-col(sm="6")
    v-menu(
      ref="menu_day"
      v-model='menu_day'
      :close-on-content-click='false'
      transition='scale-transition'
      offset-y=''
      min-width='290px')
      template(v-slot:activator='{ on }')
        v-text-field(
          v-model='sel_day'
          label='Dia'
          :error-messages="errors"
          prepend-icon='fas fa-calendar-alt'
          readonly
          v-on='on')
      v-date-picker(v-model='sel_day' color="primary" :min="today"  no-title scrollable)
        .flex-grow-1
        v-btn(text='' color='primary' @click='menu_day = false; sel_day=""') Cancelar
        v-btn(text='' color='primary' @click='menu_day = false') OK

  v-col(sm="6")
    v-menu(
      ref="menu_hour"
      v-model='menu_hour'
      :close-on-content-click='false'
      transition='scale-transition'
      offset-y=''
      min-width='290px')
      template(v-slot:activator='{ on }')
        v-text-field(
          v-model='sel_hour'
          label='Hora'
          :error-messages="errors"
          prepend-icon='fas fa-clock'
          readonly
          v-on='on')
      v-time-picker(v-model='sel_hour' color="primary" )
        .flex-grow-1
        v-btn(text='' color='primary' @click='menu_hour = false; sel_hour=""') Cancelar
        v-btn(text='' color='primary' @click='menu_hour = false') OK
</template>

<script>
import moment from 'moment'

export default {
  props:['errors'],
  data () {
    return {
      sel_day:"",
      menu_day:false,
      sel_hour:"",
      menu_hour:false,
      today: moment().format('YYYY-MM-DD'),
    }
  },
  computed: {
    selectedDatetime () {
      let raw_dt = this.sel_day +" "+this.sel_hour
      let selected_dt = moment(raw_dt).format('YYYY-MM-DD HH:mm:ss')
      return selected_dt
    }
  },
  watch: {
    selectedDatetime(val) {
      this.$emit('input',val)
    }
  }
}
</script>

</style>
