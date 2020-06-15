<template lang="pug">
v-container.mb-5.fluid.fill-height(dark color="primary")
  .row.justify-center
    .col
      Table
      
</template>
<script>
import {
  Detail,
  Form,
  Info,
  Table,
  PasswordForm,
  LogInfo,
} from '@/components/users'

export default {
  name: "Users",
  components:{
    Detail,
    Form,
    Info,
    Table,
    PasswordForm,
    LogInfo,
  },
}
</script>
