<template lang='pug'>
      v-card
        .row.text-left.justify-space-around.py-3(v-if="filters.length>0")
          .overline.mt-2
            h2 {{ filters.length }} filtros Aplicados
          v-tooltip(bottom)
            template(v-slot:activator='{ on, attrs }')
              v-btn(text @click="removeAllFilters" v-on="on" ) Quitar
                v-icon.pointer.ml-4(size='large') fas fa-times
            span Quitar filtros
        .row(v-for="fil in filters").justify-space-around
          p(v-if="Array.isArray(fil.value)")
            strong {{fil.name}}
            v-chip(v-for="v in fil.value") {{v}}
          p(v-else)
            strong.mr-3 {{fil.name}}
            | {{fil.value}}
          v-tooltip(bottom)
            template(v-slot:activator='{ on, attrs }')
              v-btn(text @click="removeFilter(fil.name)" v-on="on" )
                v-icon.pointer.ml-4(size='large') fas fa-times
            span Quitar filtro de {{ fil.name }}
</template>
<script>

import filtersManager from '@/layouts/templates/Tables/filtersManager'
export default {
  name: 'CompanyReportFilters',
  mixins: [ filtersManager ],
  props: ['companyName'],
  data () {
    return {
    }
  },
  computed: {
    title () {
      return `Reportes recientes de ${this.companyName}`
    }
  }
}
</script>
