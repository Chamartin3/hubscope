<template lang="pug">
LightCard(:title="empresa.name")
    .row.justify-space-around.py-3
      GoalStatus(
          v-for="g in empresa.open_goals"
          :status="g.status"
          :indicatorname="g.indicatorname"
          )
      .text-center(v-if="empresa.open_goals.length===0")
        .overline La empresa no tiene metas abiertas
    .text-center
      v-btn(
        color="primary" text
        @click="$router.push({name:'empresa',params:{id:empresa.id}})" )
        | ver detalles

</template>
<script>
import GoalStatus from '@/components/goals/Status'
export default {
  name: 'EmpresaCard',
  components: { GoalStatus },
  props: ['empresa']

}
</script>
