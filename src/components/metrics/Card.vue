<template lang="pug">
v-card.my-1
  .container
    h3.text-center(
      v-editable
      @edit="$emit('edit')")
      | {{ metric.name }}

    .overline {{ metric.desc }}
    .overline
      strong Tipo:  {{ metric.tipo | tipos }}
    .overline
      strong Unidad: {{ metric.unidad  }}
      v-btn(
        v-if="metric.has_indicators===0 && metric.tipo!='COMP'"
        text
        color="grey lighten-2"
        x-small @click="$emit('delete', metric.id)" )
        v-icon(x-small) fas fa-trash
    .overline(v-if="metric.constant_value")
      strong Valor: {{ metric.constant_value  }}

</template>
<script>

export default {
  name: 'MetricCard',
  filters: {
    tipos: val => {
      const tipos = {
        'A': 'Simple',
        'C': 'Constante',
        'E': 'Estado',
        'COMP': 'Computada'
      }
      return tipos[val]
    }
  },
  props: {
    metric: {
      type: Object,
      required: true
    }
  }
}
</script>
