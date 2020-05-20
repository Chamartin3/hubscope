<template lang="pug">
extends ../../layouts/templates/Modal/FullsreenModal.pug

append content
  div(v-if="instance")
    userCard(
      @cambio="$emit('successChange', $event)",
      :userInstance="instance"
      )
    userLogInfo(:user="instance")
</template>
<script>
import userCard from './userCard'
import userLogInfo from './userLogInfo'
import { instanceModal } from '@/mixins/Modal'
export default {
  name: "UserDetail",
  mixins:[instanceModal],
  components:{
    userCard,
    userLogInfo
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
