<template lang="pug">
extends ../../layouts/templates/Modal/FullsreenModal.pug

append content
  div.white.black--text(v-if="instance")
    Info(
      @cambio="$emit('successChange', $event)",
      :userInstance="instance"
      )
    LogInfo(
      :user="instance"
      @cambio="$emit('successChange', $event)",
      )
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
      contentColor:'secondary',
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
