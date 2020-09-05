<template lang="pug">
.container
  .row(v-if="loading")
    LoadingComponent

</template>
<script>
import EmpresaCard from '@/components/informe/Empresa.vue'
// import moment from 'moment'
import iteratorList from '@/layouts/templates/Lists/iteratorList.js'

import moment from 'moment'
export default {
  name: 'Dashboard',
  components: { EmpresaCard },
  //   components:{Card},
  mixins: [iteratorList],
  data () {
    return {
      modelName: 'company',
      itemName: 'Empresas',
      itemPluralName: 'Empresas',
      nodata: 'No hay empresas registradas',
      listMethod: 'all',
      params: {
        per_page: 3
      }
    }
  },
  mounted () {
    console.log(this.model)
  },
  methods: {
    addItem (item) {
      item = this.preprocessElements(item)
      this.$set(this, 'items', [item, ...this.items])
      this.setPagination(this.items)
    }
  }
}
</script>
