<template>
  <div id="app">
   <router-view/>
  </div>
</template>
<script>
export default {
  mounted () {
    console.log(this.$django.models)
  }
}
</script>
<style lang="scss">

.link {
  cursor: pointer;
}

// #app .v-content__wrap, .v-sheet{
//   background-color:var(--v-primary-darken2);
// }
.v-card, tbody, .v-data-table-header, .v-picker__body, .v-picker__body, .v-data-footer {
  background-color: var(--v-primary-lighten1);
}

tr.v-data-table {
  background-color: var(--v-primary-base);
}
thead>tr {
  background-color: var(--v-primary-base);
}
tbody>tr:hover {
  background-color: var(--v-primary-base) !important;
}

.theme--dark.v-picker__body {
  background: var(--v-primary-darken1);
}
.sline{
  border-color: var(--v-secondary-base);
  border-width: 2px;
}



// .v-card__actions, .v-card__title, .v-menu {
//   background-color: var(--v-primary-base);
// }

// .v-data-table, .v-card, .theme--dark {
//   background-color:var(--v-primary-lighten1);
// }
// .v-data-table, .v-card, .theme--light {
//   background-color:var(--v-primary-lighten1);
// }
</style>
