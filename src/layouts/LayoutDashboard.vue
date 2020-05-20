<template lang="pug">
  v-app(light)
    AppBar
    CoreView
    CoreFooter
    CoreDrawer
</template>
<script>
export default {
  name: 'Dashboard',
  components: {
    CoreDrawer: () => import('@/layouts/navigation/Drawer'),
    CoreFooter: () => import('@/layouts/navigation/Footer'),
    AppBar: () => import('@/layouts/navigation/NavBarPrivate'),
    CoreView: () => import('@/layouts/navigation/View')
  }
}
</script>
