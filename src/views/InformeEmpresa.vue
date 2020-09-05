  <template lang="pug">
.container
  LoadingComponent(v-if="loading || !instance")
  div(v-else)
    header.secondary.text-center.white--text.pa-5
      .display-3 {{ instance.name }}
    .row.typing--text.align-start
      .col
        //- hr.sline
    .container
      //- .row.typing--text.align-start
      //-   .row.justify-space-between
      //-     v-col
      //-       v-card.py-5.px-3(dark color="secondary")
      //-         .headline Metas activas
      .row.justify-space-between(v-for="g in instance.open_goals")
        .col
          Detail(:id="g.id")
  BackButton(to="dashboard" mensaje="Volver al home")
</template>
<script>
import Detail from '@/components/informe/Detail.vue'

export default {
  name: 'Empresa',
  components: {
    Detail
  },
  data () {
    return {
      instance: null,
      model: 'company',
      action: 'detail',
      text: '',
      loading: false
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
      this.loadind = true
      let model = this.$django.models[this.model]
      this.instance = await model[this.action](this.id)
      this.loadind = false
    }
  }

}
</script>
