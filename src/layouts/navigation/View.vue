<template lang="pug">
v-content()
    Alert(ref="Alert")
    Loading.mt-5(v-if="is_loading", :msg="msg")
    v-container.px-0(fluid fill-height v-show="!is_loading")
      v-fade-transition(mode="out-in")
        router-view(
          class="align-start"
          @loading="setLoading($event)",
          @loaded="is_loading=false")
</template>
<script>
export default {
  components: {
    Alert: () => import('@/layouts/utils/Alert'),
    Loading: () => import('@/layouts/utils/Loading')
  },
  data () {
    return {
      is_loading: false,
      msg: null
    }
  },
  methods: {
    setLoading (msg) {
      this.msg = msg
      this.is_loading = true
    }
  },
  computed: {
    alert () { return this.$store.state.alert },
    featuredSection () { return this.$route.params.scroll }
  },
  watch: {
    alert (val) {
      this.$refs.Alert.alert(val.type, val.tit, val.msg)
    }
  },
  created () {
    this.is_loading = false
  }
}
</script>
<style lang="sass">
$material-light: ('background': #DC1F1F)
</style>
