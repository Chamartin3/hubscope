<template lang="pug">
//- extends ../../mixins/templates/Lists/doubleLineList.pug
//- /* :custom-sort="orderResults", */
.container(fluid)
  DeleteConfirmation(
    ref="DeleteConfirmation"
    @confirmDelete="deleteMeeting($event)"
    :model="model"
  )
  v-data-iterator(
  :items="items",
  :items-per-page="pagination.per_page",
  :page="params.page",
  :loading="loading"
  :server-items-length="pagination.total"
  hide-default-footer
   )
    template(v-slot:footer)
      v-toolbar.mb-1(dark, color="secondary darken-1")
        v-row.mt-2(align="center", justify="center")
          v-spacer
          span.white--text Empresas Por Pagina
          v-menu(offset-y)
            template(v-slot:activator="{ on }")
              v-btn.ml-2(color="white", text v-on="on")
                | {{ params.page_size }}
                v-icon fa-caret-down
            v-list
              v-list-item(v-for="number in [5,10,15,20]", :key="number", @click="params.page_size=number")
                v-list-item-title {{ number }}

    template(v-slot:header)
      v-toolbar.mb-1.px-5( v-if="!loading" dark, dense color="secondary darken-1")
        v-row.mt-2(align="center", justify="center")

          span.white--text
            .overline
              h3 Mostrando {{pagination.from}} hasta {{pagination.to}}
            .overline
              h3 of {{pagination.total}} dinamicas
          v-spacer
          span.mr-4.white--text
            | Pagina {{ pagination.current_page }} de {{ totalPages ? totalPages : 1  }}
          |
          v-btn.mr-1(dark, small color="primary darken-3",
          :disabled="pagination.current_page==1"
           @click="params.page=params.page-1")
            v-icon fa-angle-left
          |
          v-btn.ml-1(dark, small color="primary darken-3",
          :disabled="pagination.current_page>=totalPages || !totalPages"
          @click="params.page=params.page+1")
            v-icon fa-angle-right

    template(v-slot:loading)
      LoadingComponent

    template(v-slot:no-data)
      .text-center
        strong No hay empresas registradas 
    template(v-slot:default="{ items, isExpanded, expand }")
      .row
        v-col(v-for="item in items", :key="item.name", cols="12", sm="12", md="6", lg="4")
            v-card
        //-   Card(@deleteItem="$refs.DeleteConfirmation.open(item.api_id, 'meeting')"
        //-   :dinamica="item")
</template>
<script>
// import moment from 'moment'
import iteratorList from '@/layouts/templates/Lists/iteratorList.js'
import {SSList} from '#/Lists'
import AlertResults from '#/Forms/formAlertMixin'
// import ZoomSSpagination from '@/mixins/Pagination/ZoomSSpagination'

// import Card from './Card'
import moment from 'moment'
export default {
  name: 'RecentMeetingsList',
//   components:{Card},
  mixins: [iteratorList, SSList, AlertResults],
  data () {
    return {
      searchField: false,
      title: '',
      subtitle: '',
      itemIcon: '',
      actionIcon: '',
      modelName:'company',
      itemName: 'Empresas',
      itemPluralName: 'Empresas Gestionadas',
      actionsOnSuccess:[],
      actionsOnFail:[],
    //   model: this.$django.models.,
      invitation:false,
      // params:{profile_id:this.look_id},
      params:{
        page_size:5,
        // userId:'amykaufmans@gmail.com'
      },
    }
  },
  filters: {
    dateReadable(date){
      return moment(date).format('DD,MMMM-YYYY')
    },
  },
  computed:{
    totalPages(){
      let totalitems= this.pagination.total
      let perpage= this.params.page_size
      return Math.ceil(totalitems/perpage)
    }
  },
  methods: {
    // deleteMeeting(meetingID){
    //   const self= this
    //   let Model = this.$django.models.meeting
    //   let res = Model.zoomDelete(meetingID).then(
    //     done => {
    //       this.$refs.DeleteConfirmation.successDelete()
    //       // self._alertResult(done)
    //       self.removeItem(meetingID)
    //       self.setPagination(this.bufered_data)
    //       // self.pagination.total_items=self.pagination.total_items-1
    //       // let records=self.pagination.total_items
    //       // let page_size=self.params.page_size
    //       // if (self.items.length<2 && records>page_size ) {
    //       //       self.listObjects(self.params)
    //       // }
    //
    //     },
    //     fail =>{
    //       self._alertFail(fail.response)
    //       this.$refs.DeleteConfirmation.loading=false
    //     }
    //   )
    // },

    handleError(e){
      this.$alert('danger','Error',e.data.message)
    },
    addItem(item){
      item=this.preprocessElements(item)
      this.$set(this, 'items', [item, ...this.items])
      this.setPagination(this.items)
    },
    // removeItem (id) {
    //   // console.log(this.bufered_data)
    //   let item = this.bufered_data.filter(x => x.api_id === id)[0]
    //   const index = this.bufered_data.indexOf(item)
    //   this.bufered_data.splice(index, 1)
    // },
    // orderResults(list){
    //   return list.sort((a,b)=>{
    //     let adate= moment(a.created_at)
    //     let bdate= moment(b.created_at)
    //     return -adate.diff(bdate)
    //   })
    // },
    // preprocessElements(el){
    //   el['id']=el.api_id
    //   return el
    // },
    // processResults(response) {
    //   if(Array.isArray(response)) return response
    //   let list=response[this.recordsAttr]
    //   this.bufered_data=this.orderResults(list)
    //   this.buffered_results=true
    //   return list
    // },
    alertCoppied(msg, event){
      this.$alert('success','' ,'Link copied to clipboard!')
    },
    goTo(loc) {  window.open(loc, "_blank") }
  },
  mounted () {
    console.log(this.model)
  }
}
</script>
