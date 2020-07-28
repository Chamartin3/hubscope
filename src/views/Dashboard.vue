<template lang="pug">
.container
    .row(v-if="loading")
        LoadingComponent
    .row(v-else  v-for="e in items" :key="e.name",) 
        .col.mx-7
            EmpresaCard(v-if="e", :empresa="e")

            
</template>
<script>
import EmpresaCard from '@/components/informe/Empresa.vue'
// import moment from 'moment'
import iteratorList from '@/layouts/templates/Lists/iteratorList.js'

import moment from 'moment'
export default {
  name: 'Dashboard',
  //   components:{Card},
  mixins: [iteratorList],
  components: { EmpresaCard },
  data () {
    return {
      modelName:'company',
      itemName: 'Empresas',
      itemPluralName: 'Empresas',
      nodata:'No hay empresas registradas',
      listMethod:'all',
      params:{
        per_page:3,
      }
    }
  },
  methods: {
    addItem(item){
      item=this.preprocessElements(item)
      this.$set(this, 'items', [item, ...this.items])
      this.setPagination(this.items)
    },
  },
  mounted () {
    console.log(this.model)
  }
}
</script>
