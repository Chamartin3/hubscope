<template lang="pug">
.container.mt-5(fluid fill-height)
  v-spacer.text-center
  .row.align-center.justify-center
    v-col(sm="auto" min-width="50%")
      //- v-img.super(:src="logoh" width="250")
      v-card.elevation-12.pa-5( dark color="primary")
        v-card-header
          h3 {{projectName}}
        v-card-text
          v-form
            v-text-field( v-model="form.username" label="Login"
              name="login" prepend-icon="fa-user" type="text")
            v-text-field(v-model="form.password" id="password"
              label="Password" name="password" prepend-icon="fa-key" type="password")
        v-card-actions.justify-center
          v-btn(@click="authenticate" color="secondary") Login
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
