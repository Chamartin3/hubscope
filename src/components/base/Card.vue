
<template lang='pug'>
v-card.primary.darken-1(dark)
  v-toolbar.text-center.primary(flat dark)
    .row.justify-center
      slot(name='title')
  .container(fluid)
    slot
</template>
