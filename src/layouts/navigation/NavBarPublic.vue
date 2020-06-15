<template lang="pug">
v-app-bar#core-app-bar(
  color='primary'
  app absolute
  dark
  flat
  height="60")
  v-toolbar-items.white--text
    v-btn(dark v-for="link in links" text :to="{ name: link.name, params: {} }")  {{link.show_name}}
</template>
<script>
import UserDropdown from '@/layouts/utils/UserDropdown'
export default {
  components: { UserDropdown },
  data () {
    return {
      links: []
    }
  },
  methods: {
    goTo (section) {
      if (this.$route.name === 'index') {
        this.scrollTo(section)
      } else {
        this.$router.push(
          {
            name: 'index',
            params: { scroll: section }
          }
        )
      }
    },
    scrollTo (section) {
      this.$vuetify.goTo(`#${section}`, { duration: 800 })
    }
  },
  mounted () {
    console.log(this.$django)
  }
}
</script>
