<template lang="pug">
extends ../../../layouts/templates/Lists/doubleLineList.pug

append before_list
  .row.text-center.justify-space-around.mt-1
    v-btn(
        small 
        @click="addPersonel" 
        color="secondary") Crear
    v-btn(
        small 
        @click="addPersonel" 
        color="secondary") Agregar

block no_items
  .row.text-center
    .col
      .overline
        h2 No hay personas registradas


</template>
<script>
import { SSDobleLine } from '@/layouts/templates/Lists'
export default {
  props:['id'],
  name: 'PhonesList',
  mixins: [ SSDobleLine ],
  data () {
    return {
      searchField: false,
      title: 'number',
      subtitle: 'reference',
      itemIcon: 'fas fa-users',
      actionIcon: 'fa-edit',
      itemName: 'Usuario',
      itemPluralName: 'Personal',
      listMethod: 'personel',
      modelName: 'company',
      params:{id:this.id},
    }
  },
  methods: {
    addPersonel(){

    },
    async getItems(params={}){
      if (this.loading){
        this.pendingRequest = true
        return []
      }
      this.loading = true
      console.log(this.id);      
      let results = await this.model[this.listMethod](this.id)
      let mres={
        pagination:{},
        results:results
      }
      if (params && params.search!='') params.page = 1
      return mres
    },
    callRegistration () { console.log('registration' + this.itemName) },
    callDetail () { console.log('detail' + this.itemName) }
  },
  mounted () {
    console.log(this.model)
    console.log(this.id)
  }
}
</script>
