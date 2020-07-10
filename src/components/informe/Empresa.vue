<template lang="pug">
v-card.pointer(dark color="primary lighten-1")
  .container
    .row.text-center(@click="$router.push({name:'resumen_empresa',params:{id:empresa.id}})")
      .col
        .display-1 {{ empresa.name }}
    hr
    .row
      .col(v-if="empresa.open_goals.length > 0")
        GoalStatus.ma-3(
          v-for="g in empresa.open_goals"
          :status="g.status"
          :indicatorname="g.indicatorname"
          )
      .col(v-else)
        .overline La empresa no tiene metas abiertas
</template>
<script>
import GoalStatus from '@/components/indicators/Goals/Status'
export default {
  name:"EmpresaCard",
  props: ['empresa'],
  components: {GoalStatus}
  
}
</script>