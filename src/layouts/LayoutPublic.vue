<template lang="pug">
  v-app(light)
    AppBar
    CoreView
    AppFooter
</template>
<script>
export default {
  name: 'Web',
  components: {
    AppBar: () => import('@/layouts/navigation/NavBarPublic'),
    AppFooter: () => import('@/layouts/navigation/Footer'),
    CoreView: () => import('@/layouts/navigation/View')
  }
}
</script>
