<template lang="pug">
.container.fill-height(v-if="instance")
  .row.typing--text.align-start(style="max-height ")
    .col.text-center
      .display-2 {{ instance.name }}
      br
  .row.justify-space-around.mt-n6
    v-btn(
      text
      color="secondary"
      @click="$router.push({name:'reporte-empresa'})" ) reportes
    v-btn(
      text
      color="secondary"
       @click="$router.push({name:'tareas-empresa'})" ) asignaciones
    v-btn(
      text
      color="secondary"
       @click="$router.push({name:'indicators-empresa'})" ) indicadores
  .row.secondary
    hr.sline
  .row
    v-fade-transition(mode="out-in")
      router-view(
        :instance="instance"
        class="align-center")

      //- v-tabs(v-model="tab"
      //- slider-color="secondary"
      //- fixed-tabs)
      //-   v-tab.typing--text( v-for="t in tabs" )
      //-     | {{t.name}}

      //- v-tabs-items(v-model='tab')
      //-   v-tab-item(key='Reportes')
      //-     ReportsPage(:instance="instance")
      //-   v-tab-item(key='Asignments')
      //-     AsignmentPage(:instance="instance")
      //-   v-tab-item(key='Indicadores')
      //-     IndicatorsPage(:instance="instance")

  BackButton(to="companies" mensaje="Volver a lista de empresas")
</template>
<script>
import ReportsPage from '@/views/Company/Reports.vue'
import AsignmentPage from '@/views/Company/Asignments.vue'
import IndicatorsPage from '@/views/Company/Indicators.vue'

export default {
  name: 'Empresa',
  components: {
    ReportsPage,
    AsignmentPage,
    IndicatorsPage

  },
  data () {
    return {
      instance: null,
      model: 'company',
      action: 'detail',
      tab: null,
      tabs: [
        { name: 'Reportes', val: 'rep' },
        { name: 'Asignaciones', val: 'asignaciones' },
        { name: 'Indicadores', val: 'indicators' }
      ],
      text: ''
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
      let model = this.$django.models[this.model]
      this.instance = await model[this.action](this.id)
    }
  }

}
</script>
