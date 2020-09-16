<template lang='pug'>
.container
  GoalDetail(ref="GoalDetail")
  GoalForm(
    @created="listObjects"
    @edited="listObjects"
    ref="GoalForm" )
  .row.justify-space-around
    GeneralPagination(
      color="secondary"
      v-model="params.page",
      :names="{singular:'meta', plural:'metas'}"
      :pagination="pagination")
      v-btn(c-dajngo-groups="'Admin'" color="secondary" text x-small
        @click="$refs.GoalForm.open()" ) crear

  .row.justify-space-around(v-if="!loading")
      GoalCard(v-for="goal in items"
      @detail="$refs.GoalDetail.view(goal.id)"
      :key="goal.id" :goal="goal")
  .row(v-else)
    LoadingComponent

</template>
<script>
import iteratorList from '@/layouts/templates/Lists/iteratorList.js'
import GoalForm from './Form'
import Goal from './Goal'
import GoalDetail from './Detail'
import Status from './Status'
import GoalCard from './MiniCard'
export default {
  name: 'GoalList',
  components: { GoalForm, GoalCard, GoalDetail },
  mixins: [ iteratorList ],
  // props: ['indicator'],
  data () {
    return {
      active: [],
      itemKey: 'id',
      itemName: 'Meta',
      modelName: 'goal'
      // listMethod: 'openGoals',
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
