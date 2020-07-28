  <template lang="pug">
div
  LoadingComponent(v-if="loading || !instance")
  .container.fill-height(v-else)
    .row.typing--text.align-start
      .col
        .display-3 {{ instance.name }}
        hr.sline
    .row.typing--text.align-start
    .row.justify-space-between
      v-col
        v-card.py-5.px-3(dark color="secondary")
          .headline Metas activas
    .row.justify-space-between(v-for="g in instance.open_goals")
      .col
        Detail(:id="g.id")
 
    v-btn.mb-7(color='secondary'
    @click="$router.push({name:'dashboard'})"
    dark large absolute bottom right fab)
      v-icon fas fa-arrow-left
</template>
<script>
import Detail from '@/components/informe/Detail.vue'

export default {
  name: 'Empresa',
  components:{
    Detail
  },
  data() {
    return {
      instance:null,
      model: 'company',
      action: 'detail',
      text: '',
      loading: false
    }
  },
  computed:{
    id() {
      return this.$route.params.id
    }
  },
  methods: {
    async getInstance(){
      this.loadind=true
      let model = this.$django.models[this.model]
      this.instance = await model[this.action](this.id)
      this.loadind=false
    },
  },
  mounted(){
    this.getInstance()
  }

}
</script>