<template lang='pug'>
LightCard.ma-2(
  width="250"
  :title="name"
  :sub="frecuencyText")
  .container
    .row.justify-center
      .col.text-center
        strong {{ asignment.total_genetated_reports }} reportes generados
    .row.justify-center
      .col.text-center
        strong Desde: {{ asignment.first_report_date | readableDate}}
    .row.justify-center(v-for="(val, status) in asignment.reports_by_status")
      .col
        .overline.text-center
          .caption {{ ReportStatus[status].name }}
        v-progress-linear(
          rounded
          :value="val/asignment.total_genetated_reports *100"
          :color='ReportStatus[status].color'
          height='15')
          template(v-slot='{ value }')
            .caption {{val}} ({{ Math.ceil(value) }}%)

      //- v-progress-linear(v-model='val' color='blue-grey' height='25')
  .row.justify-end(v-django-groups="'Admin'")
    v-btn(text @click="$emit('borrar',asignment.id )" )
      v-icon(x-small) fas fa-trash
</template>
<script>
import { Statuses } from '@/components/reports/utils.js'
import { readableDate } from '@/components/utils.js'
export default {
  name: 'AsignmentCard',
  filters: {
    readableDate: readableDate
  },
  props: ['asignment'],
  data () {
    return {
      ReportStatus: Statuses,
      weekdays: [
        'Lunes',
        'Martes',
        'Miercoles',
        'Jueves',
        'Viernes',
        'Sabbados',
        'Domingos'
      ]
    }
  },
  computed: {
    name () {
      return this.asignment.metric_info.name
    },
    selectedText () {
      if (this.asignment.frecuency === 'DAY') return this.asignment.metafreq
      let days = this.asignment.metafreq.split(',')
      let last = days.pop()
      const self = this
      if (this.asignment.frecuency === 'MONT') {
        if (days.length < 1) return last
        return days.join(',') + ' y ' + last
      }
      if (this.asignment.frecuency === 'WEEK') {
        if (days.length < 1) return self.weekdays[last]
        return days.map(d => self.weekdays[d]).join(',') + ' y ' + self.weekdays[last]
      } else {
        return 1
      }
    },
    frecuencyText () {
      if (!this.selectedText) return null
      if (this.asignment.frecuency === 'MONT') {
        return `Los ${this.selectedText} de cada mes`
      }
      if (this.asignment.frecuency === 'WEEK') {
        return `Semanalmente los ${this.selectedText}`
      }
      if (this.asignment.frecuency === 'DAY') {
        return `Cada ${this.selectedText} dias`
      }
      return 'Solo una vez'
    }
  }
}
</script>
