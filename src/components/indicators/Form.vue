<template lang="pug">
extends ../../layouts/templates/Modal/ModalForm
append content
  .row
    .col
      v-text-field(
        label="Nombre" placeholder="Nombre del Indicador"
        :errors="errors.name"
        v-model="form.name")
    .col
      v-text-field(
        label="Unidad"
        placeholder="Unidad de medida"
        v-model="form.unidad"
        :errors="errors.unidad"
        )
  .row

    .col
      EmpresaSelect(
        ref="selectEmpresa"
        single, takeID
        v-model="form.company"
        :outErrors="errors.company")
  .row
    .col
      v-text-field(
        label="Descripción"
        placeholder="Descripción del Indicador"
        :errors="errors.desc"
        v-model="form.desc")
  .row
    .col
      v-select(
        :items="tipos"
        label="Tipo"
        v-model="form.tipo"
        :errors="errors.tipo"
        item-value="value"
        item-text ="name"
      )
  .row(v-if="form.tipo")
    .col
      ComponentsSelect(
        v-model="form.components"
        :type="form.tipo"
        @error="form.tipo=null"
        )

</template>
<script>
import { formModal } from '#/Modal'
import { Tipos } from './utils'
import ComponentsSelect from './ComponentsSelect'
import EmpresaSelect from '@/components/empresas/Select'

export default {
  name: 'IndicatorForm',
  components: {
    ComponentsSelect, EmpresaSelect
  },
  mixins: [formModal],
  data () {
    return {
      // activator:this.button,
      // customFormTitle: 'Llenar reporte',
      tipos: Tipos,
      modalDark: true,
      modalColor: 'primary',
      model_name: 'Indicador',
      model: this.$django.models.indicator,
      form: {
        name: '',
        desc: '',
        tipo: '',
        unidad: '',
        components: []
      }
    }
  },
  computed: {
    tipoDesc () {
      if (!this.form.tipo || this.form.tipo == '') return
      let tipo = this.tipos.filter(t => t.value === this.form.tipo)[0]
      return tipo.desc
    }
  },
  methods: {
    onClose () {
      this.$refs.selectEmpresa._clearForm()
    }
  }
}

</script>
