<template lang="pug">
extends ../../layouts/templates/Modal/ModalForm
block title
  header.primary.text-center.py-2
    .headline.white--text Llenar Reporte
append content
  .row.text-center(v-if="instance")
    .col
      .headline {{instance.name}}
  .row.text-center(v-if="instance")
    .col
      .overline
        strong desde {{ instance.end | date }}
      .overline
        strong hasta {{ instance.end | date }}
  .row(v-if="instance")
    .col
      v-text-field(
        v-model="form.num_value"
        :label="instance.unidad"
        type="number"
        :min="1"
        style="max-width:70px; margin: auto;")

</template>
<script>
import { formModal } from '#/Modal'
import { Filters } from './utils'

export default {
  name: 'ReportForm',
  mixins: [formModal, Filters],
  data () {
    return {
      // activator:this.button,
      customFormTitle: 'Llenar reporte',
      editAction: 'fill',
      model: this.$django.models.report,
      form: {
        num_value: 0
      }
    }
  }
}
</script>
