<template lang="pug">
extends ../../layouts/templates/Modal/ModalForm
append content
  .container.pa-5.theme--dark
    .row.justify-center
      .overline
        h3 Indicador
    .row.justify-center(v-if="indicator")
      .headline Indicador {{ indicator.name }}
    .row.justify-center(v-else)
      IndicatorSelect
    .row.justify-center
      RangeSelect(
        :errors="errors"
        v-modelMod.merge="form")
    .row
      .col.text-center.justify-center
        v-text-field.align-center(
          v-model="form.goal"
          label="Meta"
          type="number"
          min="1"
          style="max-width:70px;  margin: auto;"
        )
      .col.text-center(v-if="form.fail")
        v-text-field(
          v-model="form.fail"
          label="Intermedio"
          type="number"
          min="1"
          :max="form.goal"
          style="max-width:70px; margin: auto;"
        )
    .row.justify-center.mt-5(v-if="form.goal")
      .col.text-center
        .overline Rango de cumplimiento
    .row.justify-center.mt-5(v-if="form.goal")
      .col
        //- track-fill-color="warning"
        LevelBar(:logro="form.goal", :intermedio="form.fail")

block title
  v-card-title(color="primary")
    .col.primary
      .text-center.headline-1.white--text
        h2
          strong Nueva Meta
</template>
<script>
import { formModal } from '@/mixins/Modal'
import IndicatorSelect from '@/components/indicators/Select'
import moment from 'moment'
import LevelBar from './LevelBar'
export default {
  components: {
    IndicatorSelect, LevelBar
  },
  mixins: [formModal],
  props: {
    fullmode: { default: false },
    company: { default: null },
    button: { default: false },
    indicator: { default: null }
  },
  data () {
    return {
      // activator:this.button,
      dialog: false,
      buttomText: 'Agregar',
      maxWidth: null,
      modalTitle: 'Nueva Meta',
      modalColor: 'primary',
      modalDark: true,
      model_name: 'Meta',
      model: this.$django.models.goal,
      range: 0,
      fail: null,
      form: {
        begin: null,
        end: null,
        goal: 1,
        fail: null
      }
    }
  },
  computed: {
    formTitle () {
      return 'Nueva Meta'
    },
    max () {
      return this.form.goal
    }
  },
  watch: {
    max (val) {
      if (val < 2) {
        this.range = 0
        return
      }
      let bad = val / 3
      let good = bad * 2
      this.range = good
    },
    indicator (val) {
      if (val) this.form.indicator = val.id
    },
    fail (val) {
      if (val === this.form.goal) this.form.fail = null
      else this.form.fail = val
    },
    range (val) {
      if (this.range === 0) {
        this.fail = null
        return
      }
      this.fail = Math.round(val)
    }
  }
}
</script>
