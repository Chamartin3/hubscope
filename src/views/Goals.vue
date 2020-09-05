<template lang='pug'>
.container.mb-5.fluid.fill-height
  .row
    .col
      GoalList
    .col-md-4.col-sm-12
</template>
<script>
import GoalList from '@/components/goals/List'
export default {
  name: '',
  components: { GoalList }
}
</script>
