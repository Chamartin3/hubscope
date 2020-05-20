<template lang="pug">
v-navigation-drawer#app-drawer(
  app
  dark
  floating
  persistent
  :src="drawer_img"
  color="primary",
  mobile-break-point="991",
  v-model="inputValue",
  width="260")
  template(v-slot:img="attrs")
    v-img(v-bind="attrs", :gradient="'to top, rgba(0, 0, 0, .8),'+ $vuetify.theme.themes.light.primary")

  v-list-item(two-line="")
    router-link(:to="{ name: 'login', params: {} }")
      v-avatar.ma-5(size='180' color="primary darken-1")
        v-img(:src='logo', height="100", contain="")
  v-divider.mx-3.mb-3
  v-list(nav)
    div
      v-list-item(v-for="(link, i) in links", :key="i", :to="{name:link.to}", active-class="primary white--text")
        v-list-item-action
          v-icon {{ link.icon }}
          |
        v-list-item-title(v-text="link.text") item
    |
</template>
<script>
import paths from '@/router/paths'
import { mapMutations, mapState } from 'vuex'

function route (path) {
  return {
    to: path.name,
    text: path.show_name !== '' ? path.show_name : path.name,
    icon: path.show_icon
  }
}

export default {
  props: {
    opened: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    ...mapState('app', ['drawer', 'drawer_img', 'logo']),
    col(){
      return this.$vuetify
    },
    inputValue: {
      get () {
        return this.$store.state.app.drawer
      },
      set (val) {
        this.setDrawer(val)
      }
    },
    links () { return paths.filter(x => x.parent === 'dashboard').map(path => route(path)) }
  },
  methods: { ...mapMutations('app', ['setDrawer', 'toggleDrawer']) }
}
</script>
