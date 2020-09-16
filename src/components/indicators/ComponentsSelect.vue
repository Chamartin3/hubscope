<template lang="pug">
.container
  .row.justify-center(v-for="(component, idx) in tipodeComponente.componentes")
    MetricMenu(
      @reset="resetVal($event)"
      :ref="'menumetric'+idx"
      @input="setVal(component.value, $event, 'menumetric'+idx)",
      :component="component")
</template>
<script>
import { Tipos } from './utils'
import MetricMenu from './MetricMenu'
export default {
  name: 'ComponentSelect',
  components: { MetricMenu },
  props: {
    type: {
      type: String,
      default: 'A',
      validator: v => ['A', 'C', 'E', 'P', 'SA'].indexOf(v) !== -1
    }
  },
  data () {
    return {
      ta: Tipos,
      components: []
    }
  },
  computed: {
    tipodeComponente () {
      return Tipos.find(t => t.value === this.type)
    },
    componentesRequeridos () {
      if (!this.tipodeComponente.componentes) return 0
      return this.tipodeComponente.componentes.length
    }
  },
  watch: {
    // componentsSet(val) {

    // },
    components: {
      deep: true,
      handler (val) {
        if (this.componentesRequeridos &&
          val.length === this.componentesRequeridos) {
          this.$emit('input', val)
        }
      }
    },
    'tipodeComponente.componentes': {
      handler (val) {
        this.components = []
        this.$emit('input', [])
        // let obj = {}
        // for (let c = 0; c < val.length; c++) {
        //   let attr = val[c].value
        //   obj[attr] = null
        // }
        // console.log(obj)
        // if (!val.length) obj = null
        // this.componentsSet = obj
      }
    }
  },
  methods: {
    resetVal (value) {
      let index = this.components.map(e => e.metric_id).indexOf(value)
      if (index === -1) return
      this.components.splice(index, 1)
      this.$emit('input', [])
    },
    setVal (name, value, idx) {
      let isRepeated = this.components.find(c => c.metric_id === value)
      let found = this.components.find(c => c.role === name)
      if (isRepeated && found) {
        if (isRepeated.role === found.role) return
      }
      if (isRepeated) {
        this.$alert('danger', 'Metrica Repetida')
        this.$emit('input', [])
        this.$emit('error')
        return
      }
      if (found) {
        let index = this.components.indexOf(found)
        this.components[index] = { role: name, metrica: value }
      } else {
        this.components.push({ role: name, metrica: value })
      }
    }
  }
}
</script>
