<template lang='pug'>
v-tooltip(bottom)
        template(v-slot:activator="{ on, attrs }")
          v-chip(v-on="on" :color="color")
            | {{ name }}
        span {{ desc }}
</template>
<script>
import { Statuses } from './utils'
export default {
  props: ['status'],
  data () {
    return {
      ...Statuses
    }
  },
  computed: {
    desc () {
      return this[this.status].desc
    },
    name () {
      return this[this.status].name
    },
    color () {
      return this[this.status].color
    }
  }
}
</script>
