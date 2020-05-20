import JsonBox from '@/components/base/JsonTest'

export default {
  components:{JsonBox},
  data(){
    return {
      meta:{
        // DetalleEdoCuentaAnt:null,
        // DetalleEdoCuentaBack:null,
        // DetalleEdoCuentaDetalle:null,
        DetalleEdoCuentaNew:null,
        // DetalleEdoCuentaPatron:null,
        // DetalleEdoCuentaAvg:null
      }
    }
  },
  watch:{
    'i':{
      deep:true,
      handler:'getMeta'
    },
  },
  methods:{
    async getMeta(){
      // this.DetalleEdoctaprestper = await this.model.DetalleEdoctaprestper(this.i.id)
      // this.meta.DetalleEdoCuentaAnt = await this.model.DetalleEdoCuentaAnt(this.i.id)
      // this.meta.DetalleEdoCuentaBack = await this.model.DetalleEdoCuentaBack(this.i.id)
      // this.meta.DetalleEdoCuentaDetalle = await this.model.DetalleEdoCuentaDetalle(this.i.id)
      this.meta.DetalleEdoCuentaNew = await this.model.DetalleEdoCuentaNew(this.i.id)
      // this.DetalleEdoCuentaPatron = await this.model.DetalleEdoCuentaPatron(this.i.id)
    },

  },
}
