<template lang="pug">
v-app-bar#core-app-bar(
color="primary"
dark
app
absolute
flat height='92')
  v-btn(v-if="responsive" icon @click.stop='onClick')
    //- v-icon menu
    v-icon fa-bars
  v-toolbar-title.tertiary--text.font-weight-light.align-self-center
    | {{ title }}
  v-spacer
  v-toolbar-items
    v-row.mx-0(align='center')
    UserDropdown(v-if="$django && $django.user", :user="$django.user")
</template>
<script>
import UserDropdown from '@/layouts/utils/UserDropdown'
import { mapMutations } from 'vuex'

export default {
  components: { UserDropdown },
  data () {
    return {
      notifications: [],
      title: 'Tablero de control',
      responsive: false
    }
  },
  computed: {
    user () {
      return this.$django.user
    },
    avatar () {
      let user = this.$django ? this.$django.user : null
      if (user && user.profile && user.profile.picture) {
        return this.user.profile.picture
      }
      return '@/assets/default_avatar.png'
    }
  },
  watch: {
    '$route' (val) {
      this.title = val.meta.show_name ? val.meta.show_name : val.name
    }
  },
  mounted () {
    this.onResponsiveInverted()
    window.addEventListener('resize', this.onResponsiveInverted)
  },
  beforeDestroy () {
    window.removeEventListener('resize', this.onResponsiveInverted)
  },
  methods: {
    ...mapMutations('app', ['setDrawer', 'toggleDrawer']),
    getOut () { this.$django.auth.logout() },
    onClick () {
      this.setDrawer(!this.$store.state.app.drawer)
    },
    onResponsiveInverted () {
      if (window.innerWidth < 991) {
        this.responsive = true
      } else {
        this.responsive = false
      }
    }
  }
}
</script>

<style>
  /* Fix coming in v2.0.8 */
  #core-app-bar {
    width: auto;
  }

  #core-app-bar a {
    text-decoration: none;
  }
</style>
