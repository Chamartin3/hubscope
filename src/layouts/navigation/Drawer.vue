<template lang="pug">
v-navigation-drawer#app-drawer(
  app
  dark
  floating
  persistent

  color="primary",
  mobile-break-point="991",
  v-model="inputValue",
  width="210")
  template(v-slot:img="attrs")
    v-img(v-bind="attrs", :gradient="'to top, rgba(0, 0, 0, .8),'+ $vuetify.theme.themes.light.primary")

  .row.mb-1
    .col.display-2.text-center.secondary--text
      //- strong HubScope
      img(
        src='@/assets/img/logo.png',
        height="100",
        contain)
    //- router-link(:to="{ name: 'login', params: {} }")
  v-divider.mx-1.mb-1
  v-list(nav)
    div
      v-list-item(v-for="(link, i) in links", :key="i", :to="{name:link.to}", active-class="primary secondary--text")
        v-list-item-action
          v-icon {{ link.icon }}
          |
        v-list-item-title(v-text="link.text") item
    |
</template>
<script>
import paths from '@/router/paths'
import { accessFilters } from '@/router/guards'
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
    col () { return this.$vuetify },
    inputValue: {
      get () {
        return this.$store.state.app.drawer
      },
      set (val) {
        this.setDrawer(val)
      }
    },
    links () {
      return paths.filter(x => x.parent === 'dashboard')
        .filter(x => !x.hide)
        .filter(accessFilters)
        .map(path => route(path))
    }
  },
  methods: { ...mapMutations('app', ['setDrawer', 'toggleDrawer']) }
}
</script>
