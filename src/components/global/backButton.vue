<template lang="pug">
v-tooltip(left)
  template(v-slot:activator="{ on, attrs }")
    v-btn.mb-7(color='secondary'
    v-on="on"
    @click="$router.push({name:to})"
    dark large fixed  bottom right fab)
      v-icon fas fa-arrow-left
  span {{ mensaje }}
</template>
<script>
export default {
  name: 'BackButton',
  props: ['to', 'mensaje']

}
</script>
