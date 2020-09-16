<template lang='pug'>
.container
  .row.justify-center
    .col
      v-select(
        :items="periodOptions"
        v-model="form.frecuency"
        label="Periodicidad"
        item-text="text"
        item-value="value"
        :error-messages="errors.frecuency"
      )

  .row.justify-center(v-if="form.frecuency==='DAY'")
    | Cada
    v-text-field.mx-4.mt-n2(
      style="max-width:50px"
      dense
      min="1"
      type="number"
      v-model="form.metafreq"
      :error-messages="errors.metafreq"
      single-lin)
    | dias

  .row.justify-center(v-if="form.frecuency==='WEEK'")
    v-btn.pointer.ma-2.text-center.align-center(
      v-for="(day, idx) in weekdays"
      :class="{'secondary':selected.includes(idx), 'primary darken-3':!selected.includes(idx)}"
      @click="toggleSelection(idx)"
      fab
      )
      .overline
        h2 {{ day }}

  .row.justify-center(v-if="form.frecuency==='MONT'")
    v-btn.ma-2.text-center.pointer(
      small fab
      v-for="num in 30"
      @click="toggleSelection(num)"
      :class="{'secondary':selected.includes(num), 'primary darken-3':!selected.includes(num)}"
      )
      .overline
        h2 {{ num }}
  .row.justify-center()
    | {{ frecuencyText }}

</template>
<script>
import { baseSubForm } from '#/Forms'
export default {
  name: 'Periodicity',
  mixins: [ baseSubForm ],
  data () {
    return {
      periodOptions: [
        { value: 'MONT', text: 'Mensual' },
        { value: 'WEEK', text: 'Semanal' },
        { value: 'DAY', text: 'Diario' }
      ],
      selected: [],
      weekdays: [
        'Lun',
        'Mar',
        'Mie',
        'Jue',
        'Vie',
        'Sab',
        'Dom'
      ],
      form: {
        frecuency: '',
        metafreq: ''
      }
    }
  },
  computed: {
    selectedText () {
      if (this.form.frecuency === 'DAY') return this.form.metafreq
      let days = [...this.selected]
      let last = days.pop()
      const self = this
      if (this.form.frecuency === 'MONT') {
        if (days.length < 1) return last
        return days.join(',') + ' y ' + last
      }
      if (this.form.frecuency === 'WEEK') {
        if (days.length < 1) return self.weekdays[last]
        return days.map(d => self.weekdays[d]).join(',') + ' y ' + self.weekdays[last]
      }
    },
    frecuencyText () {
      if (!this.selectedText) return null
      if (this.form.frecuency === 'MONT') {
        return `Los ${this.selectedText} de cada mes`
      }
      if (this.form.frecuency === 'WEEK') {
        return `Semanalmente los ${this.selectedText}`
      }
      return null
    }
  },
  watch: {
    'form.frecuency': {
      handler (val) {
        this.selected = []
      }
    },
    selected: {
      deep: true,
      handler (val) {
        this.form.metafreq = val.join(',')
      }
    }
  },
  methods: {
    toggleSelection (id) {
      let idx = this.selected.indexOf(id)
      if (idx === -1) this.selected.push(parseInt(id))
      else this.selected.splice(idx, 1)
      this.selected.sort((a, b) => a - b)
    }
  }
}
</script>
