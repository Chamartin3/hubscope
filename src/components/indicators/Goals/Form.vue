<template lang="pug">
extends ../../../layouts/templates/Modal/ModalForm
append content
  .container.pa-5.theme--dark
    .row.justify-center
      .overline 
        h3 Nueva meta para {{ indicator.name }}
    .row.justify-center
      RangeSelect(
        :errors="errors"
        v-modelMod.merge="form")
    .row.justify-center
      v-text-field(
        v-model="form.goal"
        label="Meta"
        type="number"
        style="max-width:70px"
      )
    .row.justify-center.mt-5(v-if="form.goal")
      .col.text-center
        .overline Cumplimiento Intermedio
    .row.justify-center.mt-5(v-if="form.goal")
      .col
        //- track-fill-color="warning"
        v-slider.align-center(
        color="red"
        thumb-color="warning"
        thumb-label="always"
        ticks
        persistent-hint
        tick-size="4"
        v-model='range' 
        :max='max' 
        :min='min')
          template(v-slot:thumb-label='props') {{props.value}}



block title
  v-card-title(color="primary")
    .col.primary
      .text-center.headline-1.white--text
        h2
          strong Nueva Meta

</template>
<script>
import { formModal } from "@/mixins/Modal";
import moment from 'moment'
export default {
  props: {
    fullmode: { default: false },
    company: { default: null },
    button: { default: false },
    indicator: { default: null }
  },
  components: {
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
    max(){
      return this.form.goal
    }
    // completed() {
    //   // return Object.values(this.form)
    //   return Object.values(this.form).reduce(function(prev, cur) {
    //     let test = cur === null && cur != "" ? true : false
    //     return test && prev;
    //   }, true);
    // }
  },
  watch: {
    max(val){
      let bad = val/3
      let good = bad *2
      this.range = good
    },
    indicator(val){
      this.form.indicator=val.id
    },
    range(val){
      this.form.fail = `[${val}]`
    }
  },
  data() {
    return {
      // activator:this.button,
      dialog: false,
      buttomText: "Agregar",
      maxWidth: null,
      modalTitle: "Nueva Meta",
      modalColor: "primary",
      modalDark: true,
      model_name: "Meta",
      model: this.$django.models.goal,
      min:0,
      range:0,
      form: {
        indicator: this.indicator.id,
        begin: null,
        end: null,
        goal: 0,
        fail:"",
      }
    };
  }
};
</script>
