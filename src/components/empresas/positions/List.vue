<template lang="pug">
extends ../../../layouts/templates/Lists/doubleLineList.pug

append before_list
  .row.text-center.justify-space-around.py-2
    UserForm(
      ref="UserForm"
      @created="listObjects()"
      :company="company_name")
    PositionForm(
      :instanceID="companyid"
      :editInstance="{id:companyid}"
      :company_name="company_name"
      ref="PositionForm"
      @edited="listObjects"
    )
    userDetail(
        @successChange="listObjects"
        ref="userDetail")
    v-overlay(absolute :value='loadingInfo')
      LoadingComponent

    v-btn(
        small 
        @click="$refs.UserForm.open()" 
        color="secondary") Crear
    v-btn(
        small 
        @click="$refs.PositionForm.open()" 
        color="secondary") Agregar

block no_items
  .row.text-center
    .col
      .overline
        h2.white--text No hay personas registradas

block item_content
    v-list-item-content
      v-list-item-title(v-if="title") 
        | {{ getItemTitle(item) }}
      v-list-item-subtitle(v-if="subtitle") 
        .overline {{ getItemSubTitle(item) }}
    v-list-item-action
      .row
        v-btn(icon @click="$emit('person',item.user)")
          v-icon(color="grey lighten-1")
            | fas fa-filter

        v-btn(icon @click="callDetail($event,item.user)")
          v-icon(color="grey lighten-1")
            | {{ itemActionIcon}}

</template>
<script>
import { SSDobleLine } from '@/layouts/templates/Lists'
import operationsMixin from '#/Lists/operations/clientSideCrud'
import UserForm from '@/components/users/Form'
import PositionForm from '@/components/empresas/positions/AddForm.vue'
import userDetail from '@/components/users/Detail'
export default {
  props:['companyid','company_name'],
  name: 'PersonelList',
  components: { 
    UserForm, 
    PositionForm, 
    userDetail 
  },
  mixins: [ SSDobleLine ],
  data () {
    return {
      checkedUser:null,
      loadingInfo:false,
      searchField: false,
      title:'function',
      subtitle: 'name',
      itemIcon: 'fas fa-users',
      actionIcon: 'fa-edit',
      itemName: 'Usuario',
      itemPluralName: 'Personal',
      listMethod: 'personel',
      modelName: 'company',
      params:{ id:this.id },
    }
  },
  methods: {
    getItemTitle(item){
      return item.user.fullname
    },
    addItem(newItem) {
      let user = newItem
      user['fullname']=`${newItem.first_name} ${newItem.last_name}`
      let position = {
        user:user,
        name:user.groups[0].name,
        ultimo_login:null
      }
      this.items.push(position)
    },
    itemAction(item){console.log(item)},
    async getItems(params={}){
      if (this.loading){
        this.pendingRequest = true
        return []
      }
      this.loading = true
      console.log(this.id);      
      let results = await this.model[this.listMethod](this.companyid)
      let mres={
        pagination:{},
        results:results
      }
      if (params && params.search!='') params.page = 1
      return mres
    },
    callRegistration () { console.log('registration' + this.itemName) },
    async callDetail (event,item) { 
        this.loadingInfo = true
        let checkedUser = await this.$django.models.accounts.get_information(item.id)
        this.$refs.userDetail.view(checkedUser.id, checkedUser)
        this.loadingInfo = false
    
      }
  },
}
</script>
