<template lang="pug">
extends ../../layouts/templates/Modal/ModalForm
append content
  .row
    .col
      v-text-field(
        label="Nombre" placeholder="Nombre de métrica"
        :error-messages="errors.name"
        v-model="form.name"
        )
  .row
    .col
      v-text-field(
        label="Descripción" placeholder="Descripción de métrica"
        v-model="form.desc"
        :error-messages="errors.desc"
        )
  .row
    .col
      v-select(
      :items="tipos"
      v-model="form.tipo"
      :error-messages="errors.tipo"
      label="Tipo"
      item-text="name"
      item-value="value"
      )
      .caption(v-if="tipoDesc")
        .overline(v-if="tipoDesc") {{tipoDesc}}
  .row
    .col
      v-text-field(
        label="Unidad" placeholder="Unidad de medida de métrica"
        v-model="form.unidad"
        :error-messages="errors.unidad"
        )
  .row(v-if="form.tipo==='C'")
    .col
      v-text-field(
        label="Valor de la constante" placeholder="Valor"
        v-model="form.value"
        :error-messages="errors.value"
        )
</template>
<script>
import { formModal } from '#/Modal'

export default {
  name: 'MetricForm',
  mixins: [formModal],
  data () {
    return {
      // activator:this.button,
      // customFormTitle: 'Llenar reporte',
      tipos: [
        {
          value: 'A',
          name: 'Simple',
          desc: 'Cada registro suma al valor total'
        },
        {
          value: 'C',
          name: 'Constante',
          desc: 'Solo puede ser registrada por administradores, y el valor se mantiene cada dia'
        },
        {
          value: 'E',
          name: 'Estado',
          desc: 'Cada registro cambia el valor expresado'
        }
      ],
      modalDark: true,
      modalColor: 'primary',
      model_name: 'metrica',
      model: this.$django.models.metric,
      form: {
        name: '',
        desc: '',
        tipo: '',
        unidad: ''
      }
    }
  },
  computed: {
    tipoDesc () {
      if (!this.form.tipo || this.form.tipo == '') return
      let tipo = this.tipos.filter(t => t.value === this.form.tipo)[0]
      return tipo.desc
    }
  }
}

</script>
