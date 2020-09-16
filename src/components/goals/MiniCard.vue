<template lang="pug">
v-card.ma-4( width='250')
  .container.text-center(@click="$emit('detail', goal)")
    .headline {{ goal.name || goal.indicatorname }}
    .overline
      | {{ goal.name ?  goal.indicatorname : '' }}
      | {{ goal.company_name }}
    Status.mx-3(
      :indicatorname="goal.indicatorname"
      :status="goal.status")
    .overline.mt-2 {{ goal.acomplishment*100 }} % de cumplimiento
    v-progress-linear(
      v-model='goal.acomplishment*100'
      color='secondary')
</template>
<script>
import Status from './Status'
export default {
  name: 'GoalMiniCard',
  components: { Status },
  props: {
    goal: {
      type: Object,
      required: true
    }
  }
}
</script>
