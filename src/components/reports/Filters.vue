<template lang='pug'>
.container.mt-n5.fluid.primary.darken-2
  .row.justify-space-around 
    v-col(cols=10)
      v-card.py-5.px-3(dark color="secondary")
        .headline {{ title }} 
    .col

  .row.justify-space-between(v-if="filters.length > 0")
    .ml-2.overline
      .row
       h2.ml-3 Filtrado
       v-tooltip(bottom)
          template(v-slot:activator='{ on, attrs }')
            v-icon.pointer.ml-4(
            v-on="on"
            @click="removeAllFilters" 
            color="red" size='medium') fas fa-times
          span Quitar filtros

  .row(v-for="fil in filters")
    .row(v-if="Array.isArray(fil.value)")
      .col
        strong {{fil.name}}
      .col
      v-chip(v-for="v in fil.value") v
    .row(v-else)
      .col.ml-3
        strong.mr-3 {{fil.name}}
        | {{fil.value}}
</template>
<script>

import filtersManager from '@/layouts/templates/Tables/filtersManager'
export default {
  name: 'CompanyReportFilters',
  mixins:[ filtersManager ],
  props:['companyName'],
  data() {
    return {
    }
  },
  computed: {
    title() {
      return `Reportes recientes de ${this.companyName}`
    }
  }
}
</script>