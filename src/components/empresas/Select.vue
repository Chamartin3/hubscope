<template lang="pug">
v-select(
    placeholder="Empresa"
    multiple 
    :items="options"
    :item-text="textField",
    :item-value="valueField",
    v-model="value")
  template( v-slot:no-data )
    | {{ nodata }}
      
</template>
<script>
import { baseSubForm } from '#/Forms' 
export default {
  props: ['preset'],
  data() {
    return {
      options: [],
      value: [],
      model: this.$django.models.company,
      listMethod: "all",
      textField: "name",
      valueField: "name",
      nodata:'No se ha encontrado empresas'
    };
  },
  watch: {
    value(val) {
      if (val) this.$emit("input", val);
    }
  },
  methods: {
    _clearForm () { value=[] },
    async getOptions() {
      this.options = await this.model[this.listMethod]();
    }
  },
  mounted() {
    this.getOptions();
    if (this.preset) this.value=this.preset
  }
};
</script>