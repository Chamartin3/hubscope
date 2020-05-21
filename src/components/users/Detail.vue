<template lang="pug">
extends ../../layouts/templates/Modal/FullsreenModal.pug

append content
  div(v-if="instance")
    Info(
      @cambio="$emit('successChange', $event)",
      :userInstance="instance"
      )
    LogInfo(:user="instance")
</template>
<script>
import Info from './Info'
import LogInfo from './LogInfo'
import { instanceModal } from '@/mixins/Modal'
export default {
  name: "UserDetail",
  mixins:[instanceModal],
  components:{
    Info,
    LogInfo
  },
  data(){
    return{
      customFormTitle:'',
      modalColor:'primary',
      modalDark:true,
      model_name: 'Usuario',
    }
  },
  watch:{
    instance:{
      deep:true,
      handler(val){
        if(val){
          this.customFormTitle = `${val.username}`
          this.customFormTitle = `${val.username}`
        }else{
          this.customFormTitle = null
        }
      }
    }
  }
}
</script>
