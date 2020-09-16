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
      if (this.status === 'constant') return ''
      return this[this.status].desc
    },
    name () {
      if (this.status === 'constant') return ''
      return this[this.status].name
    },
    color () {
      if (this.status === 'constant') return ''
      return this[this.status].color
    }
  }
}
</script>
