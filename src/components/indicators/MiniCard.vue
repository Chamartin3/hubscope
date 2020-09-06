<template lang="pug">
LightCard(:title="indicator.name")
</template>
<script>
export default {
  name: 'IndicatorCard',
  props: ['indicator']
}
</script>
