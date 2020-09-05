<template lang='pug'>
.container
  LoadingComponent(v-if="loading || !instance")
  Goal(v-else :goal="instance")
</template>
<script>
import Goal from '@/components/goals/Goal.vue'
export default {
  name: 'Detail',
  props: ['id'],
  components: {
    Goal
  },
  data () {
    return {
      loading: false,
      instance: null
    }
  },
  methods: {
    async getDetail () {
      let loading = true
      this.instance = await this.$django.models.goal.detail(this.id)
      this.loading = false
    }
  },
  mounted () {
    this.getDetail()
  }
}
</script>
