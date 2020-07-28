<template lang="pug">
v-container.mb-5.fluid.fill-height(dark color="primary")
  .row.justify-center
    .col
      UserTable(ref="UserTable" 
        @new="$refs.UserForm.open()")
      UserForm(ref="UserForm", 
        @created="$refs.UserTable.addItem($event)")
      
</template>
<script>
import {
  Detail as UserDetail,
  Form as UserForm,
  Info as UserInfo,
  Table as UserTable,
  LogInfo as UserLogInfo,
} from '@/components/users'

export default {
  name: "Users",
  components:{
    UserDetail,
    UserForm,
    UserInfo,
    UserTable,
    UserLogInfo,
  }
}
</script>
