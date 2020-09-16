<template lang="pug">
.container
  LoadingComponent(v-if="loading" )
  div(v-else-if="indicator")
    DeleteConfirmation(
      model="indicator"
      ref="DeleteConf"
      customMessage="¿Desea eliminar este indicador?"
      @success="$router.go(-1)")
    ModalEdit(
      ref="ModalEdit",
      @successChange="getInstance"
      :editInstance="indicator"
      :action="$django.models.indicator.partial_update",
      :service="$django.models.indicator.partial_update",
      )
    v-card.primary.darken-1.white--text
      .text-center
        div(v-editable @edit="$refs.ModalEdit.openDialog('name','text','nombre de indicador')")
          h1 {{ indicator.name}}
      .container
        .row.justify-space-around()
          .overline.darken-4.mx-3
            div(v-editable @edit="$refs.ModalEdit.openDialog('desc','text','descripción de indicador')")
              h4 {{ indicator.desc }}
          .overline.mx-3
            div(v-editable @edit="$refs.ModalEdit.openDialog('unidad','text','unidad de medida')")
              h4
                strong Unidad:
                |
                | {{ indicator.unidad }}
    OpenGoals(:indicator="indicator")
    Inform(
      @period="setTable($event)"
      :metrics="indicator.metrics"
      :indicatorname="indicator.unidad"
      :indicator="indicator.id")
  .row.justify-space-between#ReportTable
    .container(v-show="report_table")
      header.blue-grey.lighten-4.pa-2
        .overline Reportes asociados
      ReportsTable(ref="Table")

  .row.justify-center.text-center
    v-btn( v-django-groups="'Admin'" large color="red" text @click="$refs.DeleteConf.open(indicator.id)" )
      | Eliminar Indicador

  BackButton(mensaje="Volver")
          //- GoalList(:indicator="indicator")

</template>
<script>
import AsignmentsList from '@/components/asignments/List'
import AsignmentsForm from '@/components/asignments/Form'
import MetricasList from '@/components/metrics/List'
import Inform from '@/components/indicators/Informe.vue'
import { Goal, List as GoalList } from '@/components/goals'
import ReportsTable from '@/components/reports/Table'
import OpenGoals from '@/components/goals/Slider.vue'

export default {
  name: 'SingleIndicator',
  components: { Inform, Goal, ReportsTable, OpenGoals },
  data () {
    return {
      model: 'indicator',
      indicator: null,
      loading: false,
      report_table: false
    }
  },
  computed: {
    id () {
      return this.$route.params.id
    }

  },
  mounted () {
    this.getInstance()
  },
  methods: {
    async getInstance () {
      this.loading = true
      let model = this.$django.models[this.model]
      this.indicator = await model['detail'](this.id)
      this.loading = false
    },

    setTable (params) {
      let names = this.indicator.components.map(m => m.metric_name)
      let filters = {
        'end__gte': params.begin,
        'begin__lte': params.end,
        'metric__name__in': names
      }
      console.log(filters)
      this.$refs.Table.setDatableFilters(filters)
      this.report_table = true
      this.$vuetify.goTo('#ReportTable')
    }
  }

}
</script>
