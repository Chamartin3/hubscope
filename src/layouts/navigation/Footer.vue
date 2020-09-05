<template lang="pug">
  v-footer#core-footer(app color='primary' fixed)
    v-layout(row wrap align-center)
      v-flex(xs12='')
        .white--text.ml-4
          | 2020
          v-icon.white--text.mx-2 fa-copyright
          | {{description}}
</template>
<script>
import { mapMutations, mapState } from 'vuex'
export default {
  computed: { ...mapState('app', ['name', 'description']) }
}
</script>

<style>
#core-footer {
  z-index: 0;
}
</style>
