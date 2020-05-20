<template lang="pug">
span
  v-badge.pointer(
  bottom
  overlap
  :value="hover"
  label=""
  icon="fa-pencil-alt"
  @click.native="press"
  transition="scale-transition")
    v-hover(v-model="hover", :close-delay="3000")
      div
        slot
</template>
<script>
export default {
  data () {
    return {
      hover: false,
      payload: ''
    }
  },
  methods: {
    press () {
      this.$emit('edit', this.payload)
      this.$root.$children[0].$root.$children[0].$emit('edit', this.payload)
    },
    hide () {
      const self = this
      setTimeout(function () {
        self.hover = false
      }, 3000)
    }
  },
  computed: {
    editable () {
      return this.$slots
    }

  }
}
</script>
<style media="screen">
.pointer{
  cursor: pointer;
}
</style>
