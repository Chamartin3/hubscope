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
// #app {
//   font-family: 'Avenir', Helvetica, Arial, sans-serif;
//   -webkit-font-smoothing: antialiased;
//   -moz-osx-font-smoothing: grayscale;
//   text-align: center;
//   color: #2c3e50;
// }
.link {
  cursor: pointer;
}

#app .v-content__wrap, .v-sheet{
  background-color:var(--v-primary-darken2);
}
.v-card, tbody, .v-data-table-header, .v-data-footer {
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

.sline{
  border-color: var(--v-secondary-base);
  border-width: 2px;
}

.v-card__actions, .v-card__title {
  background-color: var(--v-primary-base);
}

// .v-data-table, .v-card, .theme--dark {
//   background-color:var(--v-primary-lighten1);
// }
// .v-data-table, .v-card, .theme--light {
//   background-color:var(--v-primary-lighten1);
// }
</style>
