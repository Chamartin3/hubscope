<template lang='pug'>
v-expansion-panel.primary(active)
    v-expansion-panel-header.v-expansion-panel--active.primary.darken-1.white--text(v-slot="{ open }")
      v-row(no-gutters)
        v-col
          .headline {{ indicator.name}}
    v-expansion-panel-content.dark.white--text.my-5
      .row.justify-space-around
        .overline.darken-4
          h4 {{ indicator.desc }}
        .overline
          h4
            strong Unidad:
            | 
            | {{ indicator.unidad }}
      .row
        .col
          v-list.primary
            .container(v-for="goal in indicator.recent_periods")
              .row 
                .overline.white--text 
                  | {{ goal.period }}
              .row
                .col  
                  v-progress-linear(
                    :value='(goal.calculated_results/goal.goal)*100' 
                    color='secondary' 
                    height='20')
                    template(v-slot='{ value }')
                      strong {{ Math.ceil(value) }}%
                  
                v-chip.mt-2(small v-if="goal.completed" color="gray")
                  | Completado
                v-chip.mt-2(small v-else color="green")
                  | Abierto
</template>
<script>
export default {
  name: 'indicatorCard',
  props:['indicator']
}
</script>