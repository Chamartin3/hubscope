<template lang="pug">
v-card.pointer(dark color="primary lighten-1")
  .container
    .row.text-center(@click="$router.push({name:'empresa',params:{id:empresa.id}})")
      .col
        .display-1 {{ empresa.name }}
    hr
    .row
      .col
</template>
<script>
export default {
  name:"EmpresaCard",
  props: ['empresa']
  
}
</script>