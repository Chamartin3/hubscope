<template lang='pug'>
extends ../../layouts/templates/Lists/iteratorList.pug
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
        GoalForm(ref="GoalForm")
    .row.justify-space-between
      v-col(cols=8)
        v-card.py-5.px-3(dark color="secondary")
          .headline Metas activas
      .col.text-right
        v-btn(color="secondary"
        @click="$refs.GoalForm.open()"
        ) Agregar Meta
block footer

</template>
<script>
import iteratorList from '@/layouts/templates/Lists/iteratorList.js'
import GoalForm from './Form'
import Goal from './Goal'
export default {
  name: 'GoalList',
  components: { Goal, GoalForm },
  mixins: [ iteratorList ],
  props: ['indicator'],
  data () {
    return {
      active: [],
      itemKey: 'id',
      itemName: 'Meta',
      modelName: 'goal',
      // listMethod: 'openGoals',
      itemPluralName: 'Metas',
      nodata: 'No hay metas activas',
      params: {
        page: 1,
        page_size: 5,
        ordering: '',
        search: ''
      }
    }
  },
  watch: {
    'pagination.per_page': function (val) {
      for (let i = 0; i < val + 1; i++) {
        this.active.push(i)
      }
    }
  },
  methods: {
    async getItems (params = {}) {
      if (this.loading) {
        this.pendingRequest = true
        return []
      }
      this.loading = true
      let results = await this.model[this.listMethod](this.params)
      return results
    }
  }
}
</script>
