<template lang="pug">
extends ../../layouts/templates/Lists/iteratorList.pug

append content
  .row
    .col
      .row
        v-col(v-for="item in items", :key="item.name", cols="12", sm="12", md="6", lg="4")
          Card(v-if="item", :empresa="item")

block header
  .row.justify-space-around

    v-btn.ml-5(dark, color="secondary darken-2",
        fab
        :disabled="pagination.current_page==1"
        @click="params.page=params.page-1")
        v-icon fa-angle-left
    .col.text-center
      span.white--text
        | {{ currentText }}
      .row.justify-center.mt-n3
        .col.text-center
          span.white--text
            | {{ totalsText }}
    v-btn.mr-5(dark, color="secondary darken-2",
        fab
        :disabled="pagination.current_page>=totalPages || !totalPages"
        @click="params.page=params.page+1")
        v-icon fa-angle-right
  hr.sline
block footer
  

</template>
<script>
// import moment from 'moment'
import iteratorList from '@/layouts/templates/Lists/iteratorList.js'
import Card from './Card'
import moment from 'moment'
export default {
  name: 'EmpresasList',
  //   components:{Card},
  mixins: [iteratorList],
  components: { Card },
  data () {
    return {
      modelName:'company',
      itemName: 'Empresas',
      itemPluralName: 'Empresas',
      nodata:'No hay empresas registradas',
      params:{
        page_size:3,
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
