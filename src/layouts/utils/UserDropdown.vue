<template lang="pug">
v-menu.mr-5.pr-2(offset-y transition='slide-y-transition')
  template(v-slot:activator='{ attrs, on }')
    v-btn.text-lg-center.no-text-transform.justify-space-around(text v-bind='attrs' v-on='on')
      //- span(style="white-space: normal;")
      v-container.mx-2(fluid, ma-0, pa-0, fill-height)
        v-layout(row)
          v-flex(xs4) {{user.first_name}} {{user.last_name}}
      v-avatar.mb-3.mr-5.ml-2(size='35')
        v-img(:src='avatar')
      v-spacer

      //- v-badge(color='error' overlap)
      //-   template(slot='badge' v-if="notifications.length>0")
      //-     | {{ notifications.length }}
  v-card
    v-list
      v-list-item(two-line :to="{name:'dashboard'}")
        v-icon.mr-3(color='tertiary')
            | fa-user-circle
        v-list-item-title.title Perfil
      v-list-item(two-line @click="$django.auth.logout()")
        v-icon.mr-3(color='tertiary')
            | fa-sign-out-alt
        v-list-item-title.title Salir
</template>
<script>
export default {
  name: 'ProfileDropdown',
  props: [ 'user' ],
  computed: {
    avatar () {
      let user = this.user
      if (user && user.profile && user.profile.picture) {
        return this.user.profile.picture
      }
      return require("@/assets/avatar.png")
    }
  }
}
</script>
