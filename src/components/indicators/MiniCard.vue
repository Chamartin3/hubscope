<template lang="pug">
LightCard.ma-2(width="250" :title="indicator.name" :sub="indicator.company_name")
  .container
    .caption
      .text-center.overline {{ indicator.desc }}
    hr
    .overline.mt-2
      strong tipo:
      |
      |
      | {{ typeName(indicator.tipo )  }}
    .overline.mt-2
      strong Metricas utilizadas:
      |
      |
      v-chip(v-for="metric in indicator.components"
        small label
        :key="metric.metric_name")
        | {{ metric.metric_name }}
    .overline.mt-2
      strong Metas activas:
      |
      |
      | {{ indicator.total_active_goals }}
    .justify-center
      v-btn.mt-3(
        text x-small color="secondary"
        block @click="$router.push({name:'single_indicator', params:{id:indicator.id} })") Ver detalle

</template>
<script>
export default {
  name: 'IndicatorCard',
  props: {
    indicator: { type: Object, required: true }
  },
  data () {
    return {
      tipos: [
        {
          value: 'S',
          name: 'Simple',
          desc: ''
        },
        {
          value: 'A',
          name: 'Acumulado',
          desc: ''
        },
        {
          value: 'C',
          name: 'Cociente',
          desc: ''
        },
        {
          value: 'E',
          name: 'Estado',
          desc: ''
        },
        {
          value: 'P',
          name: 'Porcentaje',
          desc: ''
        },
        {
          value: 'SA',
          name: 'Producto',
          desc: ''
        }
      ]
    }
  },
  methods: {
    typeName (val) {
      return this.tipos.filter(tipo => tipo.value === val)[0].name
    }
  }
}
</script>
