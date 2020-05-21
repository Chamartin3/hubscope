<template lang="pug">
.container.mb-5.fluid.fill-height
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
