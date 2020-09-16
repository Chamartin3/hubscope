<template lang="pug">
div
  .text-center(v-if="loading")
    LoadingComponent
  v-slide-group.pa-4(v-else active-class='success' show-arrows)
    v-slide-item(v-slot:default='{ active, toggle }')
    v-slide-item(v-for="goal in items" :key='goal.id' v-slot:default='{ active, toggle }')
      GoalCard(:goal="goal" @detail="$refs.GoalDetail.view($event.id)")
      //- v-card.ma-4( width='250')
        .container.text-center
          .headline {{ goal.name || goal.indicatorname }}
          .overline
            | {{ goal.name ?  goal.indicatorname : '' }}
            | {{ indicator.company_name }}
          Status.mx-3(
            :indicatorname="goal.indicatorname"
            :status="goal.status")
          .overline.mt-2 {{ goal.acomplishment*100 }} % de cumplimiento
          v-progress-linear(
            v-model='goal.acomplishment*100'
            color='secondary')
    v-slide-item(v-slot:default='{ active, toggle }')
      v-card.ma-4( width='100')
        GoalDetail(ref="GoalDetail" @deletedGoal="listObjects")

        GoalForm(
          @created="listObjects"
          ref="GoalForm"
          :indicator="indicator")
        .text-center.align-center.grey--text
          v-btn.mt-5(x-large @click="$refs.GoalForm.open()" color="grey" text )
            v-icon(x-large) fas fa-plus-circle
          .overline nueva
          .overline meta

</template>
<script>
import GoalForm from './Form'
import GoalDetail from './Detail'
import Status from './Status'
import GoalCard from './MiniCard'
import iteratorList from '@/layouts/templates/Lists/iteratorList.js'

export default {
  name: 'GoalSlider',
  components: { GoalForm, Status, GoalCard, GoalDetail },
  mixins: [iteratorList],
  props: {
    indicator: {
      type: Object,
      required: true
    }
  },
  data () {
    return {
      modelName: 'indicator',
      listMethod: 'openGoals'
    }
  },
  methods: {
    async getItems (params = {}) {
      this.loading = true
      let results = await this.model[this.listMethod](this.indicator.id)
      return results
    }
  }

}
</script>
