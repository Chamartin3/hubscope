<template lang='pug'>
.container
  .row.text-center
    .col(v-if="report.value || report.value===0")
      .display-1
        | {{ report.value | number }}
      .overline(v-if="report.value")
        .headline {{ report.metric.unidad }}
      .overline
        | {{ report |  simpleperiod  }}
      .overline
        | ({{ report | days }} )

    .col(v-else)
      .display-1
        | Pendiente
      .overline
        | Fecha esperada de reporte
      .overline
        | Despues del {{ report.end | date }}
      .overline
        | Antes del {{ report.deadline | date }}
      .overline(:class="{ 'red--text': report.delayed }")
        h3.font-weight-bold ({{ report.end | days_until }})
    .col(v-if="report.value")
      .text-center
        .overline Registrado por
        .subtitle-1.pointer(@click="$emit('user', report.registered_by)")
          | {{ report.registered_by | nulluser }}
      .text-center.mt-3(v-if="")
        .overline Modificado:
        .overline {{ report.updated_at | date }}
        .subtitle-1.pointer(@click="$emit('user', report.modified_by)")
          | {{ report.modified_by | nulluser }}

    .col.align-center
      .text-center
        v-btn.ma-1.gray(
          v-if="report.status!='cerrada'"
          color="secondary lighten-1",
          @click="$emit('editReport', report)",
          small
        )
          v-icon.mr-2(x-small) far fa-edit
          | LLenar
      .text-center
        v-btn.ma-1(
          v-django-groups="'Admin'"
          color="secondary darken-2",
          @click="$emit('deleteReport', report)",
          small
        )
          v-icon.mr-2(x-small) far fa-trash-alt
          | Eliminar

      .text-center(
        v-if="report.status!='cerrada' && report.value"
        v-django-groups="'Admin'")

        v-btn.ma-1(
          color="grey darken-2", dark
          @click="$emit('closeReport', report)",
          small)
          v-icon.mr-2(x-small) far fa-window-close
          | Cerrar

  //- td(:colspan='headers.length')
  //-     .container
  //-       .row
  //-         .col Periodo  {{ item | period }}
  //-       .row
  //-         .col Registrado el {{item.created_at | datetime}}
  //-       .row
    //- .col Registrado Por {{item.registered_by}}
</template>
<script>
import moment from 'moment'
import reportStatus from './Status'
import { Filters } from './utils'
export default {
  name: 'ReportCard',
  components: { reportStatus },
  mixins: [Filters],
  props: ['report']
}
</script>
