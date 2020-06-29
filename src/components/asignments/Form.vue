<template lang="pug">
extends ../../layouts/templates/Modal/ModalForm
append content
  .container.pa-5.theme--dark
    .row.justify-center
      .col
        //- @input="$set(form, 'metric', $event.id)")
        MetricasSelect(
          :outErrors="errors.metric"
          v-modelMod:id.attr="form.metric")
    .row.justify-space-around 
        v-text-field(
          style="max-width:190px"
          label="Tiempo para entregar"
          suffix="dias" 
          type="number" 
          :error-messages="errors.delivery_time"
          v-model="form.delivery_time")
        v-checkbox(
          color="secondary"
          label="Periodica"
          v-model="form.periodic")
    .row(v-if="form.periodic")
      Periodicity(
        :outErrors="errors"
        v-modelMod.merge="form"
        )
    .row
      v-menu.primary(
        ref="datemenu2"
        dark
        v-model='datemenu2'
        :close-on-content-click='false'
        transition='scale-transition'
        min-width='290px')
        template(v-slot:activator='{ on }')
          v-text-field(
            v-model='form.last'
            label='Fecha Inicial'
            prepend-icon='fas fa-calendar-alt'
            :error-messages="errors.last"
            readonly
            v-on='on')
        v-date-picker(v-model='form.last' no-title scrollable)
          .row.justify-space-around 
            v-btn(color='red' @click='datemenu2 = false') Cancelar
            v-btn(color='green' @click='$refs.datemenu2.save(form)') OK

      v-menu.primary(
        v-if="!form.periodic"
        ref="datemenu"
        dark
        v-model='datemenu'
        :close-on-content-click='false'
        transition='scale-transition'
        min-width='290px')
        template(v-slot:activator='{ on }')
          v-text-field(
            v-model='form.next_ocurrence'
            label='Fecha Final'
            prepend-icon='fas fa-calendar-alt'
            readonly
            v-on='on')
        v-date-picker(
            :min="form.last"
            :error-messages="errors.next_ocurrence"
            v-model='form.next_ocurrence' no-title scrollable)
          .row.justify-space-around 
            v-btn(color='red' @click='datemenu = false') Cancelar
            v-btn(color='green' @click='$refs.datemenu.save(form)') OK
    .row.justify-center()
      | {{ periodText }}
block title
  v-card-title(color="primary")
    .col.primary
      .text-center.headline-1.white--text
        h2
          strong Nueva Asignación

</template>
<script>
import { formModal } from "@/mixins/Modal";
import MetricasSelect from "@/components/metrics/Autocomplete";
import Periodicity from "./periodicityForm";
import moment from 'moment'
export default {
  props: {
    fullmode: { default: false },
    company: { default: null },
    button: { default: false }
  },
  components: {
    MetricasSelect,
    Periodicity
  },
  mixins: [formModal],
  computed: {
    formTitle() {
      return "Add new";
    },
    periodText(){
      if (!this.form.periodic && this.form.next_ocurrence){
        return `Desde ${this.form.last} hasta ${this.form.next_ocurrence}`
      }else{
        return null
      }
    },
    // completed() {
    //   // return Object.values(this.form)
    //   return Object.values(this.form).reduce(function(prev, cur) {
    //     let test = cur === null && cur != "" ? true : false
    //     return test && prev;
    //   }, true);
    // }
  },
  // watch: {
  //   completed(val){
  //     if(!val) this.valid=false
  //   }
  // },
  data() {
    return {
      // activator:this.button,
      datemenu:false,
      datemenu2:false,
      dialog: true,
      period: null,
      buttomText: "Agregar",
      maxWidth: null,
      modalTitle: "Nueva Asinación",
      modalColor: "primary",
      modalDark: true,
      model_name: "Asignación",
      model: this.$django.models.asignment,
      form: {
        metric: null,
        company: this.company,
        periodic: false,
        delivery_time: 3,
        frecuency: null,
        metafreq: "",
        last: moment().format("YYYY-MM-DD")
      }
    };
  }
};
</script>
