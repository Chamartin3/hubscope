<template lang="pug">
.container.mb-5.fluid.fill-height
  .row.justify-center
    .col
      CompaniesList

</template>
<script>
import CompaniesList from '@/components/empresas/List.vue'
export default {
  name: "Empresas",
  components:{ CompaniesList },
}
</script>
