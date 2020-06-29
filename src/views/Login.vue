<template lang="pug">
.container(fluid fill-height)
  v-spacer.text-center
  .row.align-center.justify-center
    v-col(sm="auto" min-width="50%")
      v-img.mx-auto.my-n12.img-bright(
          style="z-index:2"
          src='@/assets/logo.png', 
          width="180", 
          contain)
      v-card.elevation-12.pa-5.mt-n5.pt-10( dark color="primary")
        v-card-header.text-center
        v-card-text
          v-form
            v-text-field( v-model="form.username" label="Login"
              name="login" prepend-icon="fa-user" type="text")
            v-text-field(v-model="form.password" id="password"
              label="Password" name="password" prepend-icon="fa-key" type="password")
        v-card-actions.justify-center
          v-btn(
            :loading="loading"
            @click="authenticate" color="secondary") Login
</template>
<script>
import LoginForm from '#/LoginForm'
import { mapMutations, mapState } from 'vuex'
export default {
  name:'LoginForm',
  mixins:[LoginForm],
  computed: {
    ...mapState('app', ['logoh']),
    projectName() {
      return this.$store.state.app.name
    }
  },
}
</script>
<style>
.img-bright { 
    -webkit-filter: drop-shadow(0 0 0.25rem  rgb(255, 255, 255));
    filter:         drop-shadow(0 0 0.25rem  rgb(255, 253, 253)); 
}
</style>