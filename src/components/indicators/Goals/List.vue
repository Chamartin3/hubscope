<template lang='pug'>
extends ../../../layouts/templates/Lists/iteratorList.pug
block content
  .row(v-for='(goal, idx) in items' :key='idx')
    .col
      Goal(:goal="goal")
      
//- block instance
//- block nodata
   strong {{nodata}}
block header
  .container(v-if="items")
    .row.justify-space-between
        GoalForm(ref="GoalForm", :indicator="indicator")
    .row.justify-space-between
      v-col(cols=8)
        v-card.py-5.px-3(dark color="secondary")
          .headline Metas activas
      .col.text-right
        v-btn(color="secondary"
        @click="$refs.GoalForm.open()"
        ) Agregar Meta
  //-         Goal(:goal="goal")
  //- v-toolbar.mb-1.px-5(v-if="!loading && pagination.last_page!=1" dark, dense color="secondary darken-1")
  //-   v-row.mt-2(align="center", justify="center")
  //-     span.white--text
  //-       .overline
  //-         h3 {{ pagesText }}
  //-       .overline
  //-         h3 {{ totalsText }}
  //-     v-spacer
  //-     span.mr-4.white--text
  //-       | {{ currentText }}
  //-     |
  //-     v-btn.mr-1(dark, small color="primary darken-3",
  //-     :disabled="pagination.current_page==1"
  //-     @click="params.page=params.page-1")
  //-       v-icon fa-angle-left
  //-     |
  //-     v-btn.ml-1(dark, small color="primary darken-3",
  //-     :disabled="pagination.current_page>=totalPages || !totalPages"
  //-     @click="params.page=params.page+1")
  //-       v-icon fa-angle-right
block footer

</template>
<script>
import iteratorList from '@/layouts/templates/Lists/iteratorList.js'
import  GoalForm   from './Form'
import  Goal   from './Goal'
export default {
  name: 'GoalList',
  components: { Goal, GoalForm},
  mixins: [ iteratorList ],
  props:['indicator'],
  data () {
    return {
      active:[],
      itemKey:'id',
      modelName:'indicator',
      itemName: 'Meta',
      listMethod:'openGoals',
      itemPluralName: 'Metas',
      nodata:'No hay metas activas',
      params:{
         page:1,
         page_size:5,
         ordering:'',
         search:'',
       }
    }
  },
  methods:{
     async getItems(params={}){
      if (this.loading){
        this.pendingRequest = true
        return []
      }
      this.loading = true
      let results = await this.model[this.listMethod](this.indicator.id,this.params)
      return results
     }
  },
  watch:{
    "pagination.per_page":function(val){
      for (let i = 0; i < val+1; i++) {
        this.active.push(i)
      }
    }
  }
}
</script>