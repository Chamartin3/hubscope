<template lang="pug">
v-card.blue-grey.lighten-5
  header.text-center.blue-grey.lighten-4.py-2
    strong Metas Evaluadas

  .container
    .text-center(v-if="empresas.lenght===0")
      .overline No hay empresas asignadas
    v-simple-table(v-else height="500")
      tbody(v-for='empresa in empresas' :key='empresa.name')
        tr.primary.white--text
          td(colspan="2")
            .row.justify-space-around
              strong
                h4 {{ empresa.name }}
              v-btn(
                x-small
                text color="white"
                @click="$router.push({name:'empresa',params:{id:empresa.id}})" )
                | ver

        tr(v-if="empresa.open_goals.length==0")
          td(colspan="2")
            | Sin metas evaluadas
        tr(v-for="goal in empresa.open_goals")
          td {{ goal.indicatorname }}
          td
            GoalStatus.ma-3(
            :status="goal.status"
            :indicatorname="goal.indicatorname"
            )

</template>
<script>
import GoalStatus from '@/components/goals/Status'
export default {
  name: 'Sumary',
  components: { GoalStatus },
  props: ['empresas']

}
</script>
