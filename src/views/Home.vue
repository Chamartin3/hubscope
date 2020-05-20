<template>
  <div>
    <h1>Home</h1>
    <img alt="Vue logo" src="@/assets/vue.png">
    <img alt="Django logo" width="500" src="@/assets/django.png">
    <HelloWorld msg="VueJS and Django the best combination"/>
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'app',
  components: {
    HelloWorld
  }
}
</script>
