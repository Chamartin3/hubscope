<template lang="pug">
v-select(
    placeholder="Rol"
    :items="options"
    :item-text="textField",
    :item-value="valueField",
    clearable
    prepend-icon="fas fa-sitemap"
    v-model="value")

  template( v-slot:no-data )
     
</template>
<script>
export default {
  props: ['filtered'],
  data() {
    return {
      options: [],
      filteredOptions:['Gerente','Registrador'],
      value: "",
      model: this.$django.models.accounts,
      listMethod: "groups",
      textField: "name",
      valueField: "name"
    };
  },
  watch: {
    value(newVal) {
      if( typeof(newVal)==='object'){
        this.$emit("input", newVal.name);
      } else {
        this.$emit("input", newVal);
      }
    }
  },
  methods: {
    _clearForm () {this.value = null },
    filterOptions(option){
      if(!this.filtered) return true
      return this.filteredOptions.includes(option.name)
    },
    async getOptions() {
      let options = await this.model[this.listMethod]()
      this.options = options.filter(this.filterOptions)
    }
  },
  mounted() {
    this.getOptions();
  }
};
</script>