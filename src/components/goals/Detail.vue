<template lang="pug">
extends ../../layouts/templates/Modal/FullsreenModal.pug
block title
  v-toolbar-title(v-if="instance")
    .headline {{ instance.indicatorname }}
append content
  div.white.black--text(v-if="instance && !waiting")
    Goal(:xgoal="instance")
  div.white.black--text(v-else)
    LoadingComponent

</template>
<script>
import { instanceModal } from '@/mixins/Modal'
import Goal from './Goal'
export default {
  name: 'GoalDetail',
  components: {
    Goal
  },
  mixins: [instanceModal],
  data () {
    return {
      modalTitle: 'Meta',
      customFormTitle: 'Meta',
      modalColor: 'primary',
      contentColor: 'secondary',
      modalDark: true,
      model_name: 'goal',
      retrieve_method: 'detail',
      waiting: false
    }
  },
  watch: {
    dialog () {
      this.wait()
    },
    instance: {
      deep: true,
      handler (val) {
        if (val) {
          this.customFormTitle = `${val.indicatorname}`
        } else {
          this.customFormTitle = null
        }
      }
    }
  },
  methods: {
    wait () {
      const self = this
      self.waiting = true
      setTimeout(function () { self.waiting = false }, 2000)
    }
  }
}
</script>
