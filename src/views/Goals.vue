<template lang='pug'>
.container.mb-5.fluid.fill-height
  .row
    .col
      GoalList
    //- .col-md-4
    //-   LightCard(title="Filtros")
    //-     .container
    //-       CompanySelect(
    //-         ref="CompanySelect"
    //-         @input="filterByCompany"
          )

</template>
<script>
import GoalList from '@/components/goals/List'
import CompanySelect from '@/components/empresas/Select.vue'

export default {
  name: '',
  components: {
    GoalList,
    CompanySelect
  }
}
</script>
