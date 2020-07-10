<template lang='pug'>.
v-expansion-panel.primary(active)
    v-expansion-panel-header.v-expansion-panel--active.primary.white--text( hide-actions )

      template(v-slot="{ open }")
        .row.justify-space-between(@click="setPanel(open)")
          .headline {{ indicator.name}}
          v-icon(dark  color="secondary" :class="{'fa-flip-vertical':open}") fas fa-arrow-circle-down
    v-expansion-panel-content.primary.darken-1    
      .container.dark.white--text.my-5.primary.darken-1.white--text
        .row.justify-space-around()
          .overline.darken-4.mx-3
            h4 {{ indicator.desc }} 
          .overline.mx-3 
            h4
              strong Unidad:
              | 
              | {{ indicator.unidad }}
          Inform(
            :indicatorname="indicator.unidad"
            :indicator="indicator.id")
      .row.justify-space-between
        GoalList(:indicator="indicator")
           
</template>
<script>
import Inform from './Informe'
import { Goal, List as GoalList  } from './Goals'
export default {
  name: 'indicatorCard',
  components: { Inform, Goal, GoalList },
  props:['indicator'],
  data() {
    return {
      panel: true,
      disabled: false
    }
  },
  methods: {
    setPanel(val){
      this.$set(this, 'panel', !val)
    }
  }
}
</script>