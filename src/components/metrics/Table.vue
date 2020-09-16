<template lang="pug">
v-card.blue-grey.lighten-5
  header.text-center.primary.py-2
    h4.ma-2.white--text
      v-icon(color="white") fas fa-ruler
      |
      | Metricas
  DeleteConfirmation(
    ref="confirmDelete"
    @success="listObjects"
    model='metric'
    customMessage='¿Desea eliminar esta métrica?'
  )
  metricForm(
    @edited="listObjects"
    @created="listObjects"
    ref="metricForm")
  .container
    v-text-field(
      v-model="params.search",
      append-icon="fa-search",
      label="Buscar metrica",
      placeholder="Buscar metrica"
      single-line,
      hide-details)
    v-btn( color="secondary" text x-small block @click="$refs.metricForm.open()" )
      | crear
    .justify-center.text-center.my-4(v-if="pagination && pagination.total>pagination.per_page")
      .caption Mostrando desde {{ pagination.from }} hasta  {{ pagination.to }} de
      .caption {{ pagination.total }} metricas en total
      .row.text-center.justify-center
        v-btn(
          v-if="pagination.current_page>1"
          color="secondary" text
          x-small @click="params.page=params.page-1" )
          | <<
        v-btn(
          v-if="pagination.current_page<pagination.last_page"
          color="secondary" text
          x-small @click="params.page=params.page+1" )
          | >>
    metricCard(v-for="metric in items"
      @delete="$refs.confirmDelete.open($event)"
      @edit="$refs.metricForm.edit(metric.id, metric)"
      :metric="metric")

</template>
<script>
import iteratorList from '@/layouts/templates/Lists/iteratorList.js'
import metricForm from './Form'
import metricCard from './Card'
export default {
  name: 'FullmetricList',
  components: { metricForm, metricCard },

  mixins: [ iteratorList ],
  data () {
    return {
      searchField: false,
      title: 'name',
      subtitle: 'desc',
      itemIcon: 'fas fa-ruler',
      itemName: 'metric',
      itemPluralName: 'Metricas',
      modelName: 'metric',
      params: {
        search: ''
      }
    }
  }
}
</script>
