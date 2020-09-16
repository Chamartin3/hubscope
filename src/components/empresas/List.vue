<template lang="pug">
.container
  CompanyForm(
    @created="listObjects"
    ref="CompanyForm")
  .row.justify-space-around
    GeneralPagination(
      color="secondary"
      v-model="params.page",
      :names="{singular:'unidad', plural:'unidades'}"
      :pagination="pagination")
      v-btn(c-dajngo-groups="'Admin'" color="secondary" text x-small
        @click="$refs.CompanyForm.open()" ) crear
    //- v-pagination(
    //-   v-model="params.page"
    //-   v-if="pagination.total > pagination.per_page"
    //-   color="secondary"
    //-   class="my-4",
    //-   :length="pagination.last_page")
    //- .col.text-center( v-if="!loading")
    //-   .overline(v-if="pagination.total > pagination.per_page")  mostrando de {{ pagination.from }} hasta {{ pagination.to }}
    //-   .overline {{ pagination.total }} unidades en total

  .row(v-if="!loading")
    .col
      .row
        v-col(v-for="item in items", :key="item.name", cols="12", sm="12", md="6", lg="4")
          Card(v-if="item", :empresa="item")
  .row(v-else)
    LoadingComponent

</template>
<script>
// import moment from 'moment'
import iteratorList from '@/layouts/templates/Lists/iteratorList.js'
import Card from './Card'
import CompanyForm from './Form'
import moment from 'moment'
export default {
  name: 'EmpresasList',
  components: { Card, CompanyForm },
  //   components:{Card},
  mixins: [iteratorList],
  data () {
    return {
      modelName: 'company',
      itemName: 'Empresas',
      itemPluralName: 'Empresas',
      nodata: 'No hay empresas registradas',
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
