<template lang="pug">
.container
  .justify-space-around
    v-card(v-for="a in items") {{ a.name }}

  .col-md-4

</template>
<script>
import iteratorList from '@/layouts/templates/Lists/iteratorList.js'
export default {
  name: 'Indicadores',
  components: {

  },
  mixins: [iteratorList],
  data () {
    return {
      modelName: 'asignment'
    }
  }
}
</script>
