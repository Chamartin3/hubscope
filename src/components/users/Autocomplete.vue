<template lang="pug">
v-autocomplete(
  v-model="value"
  :items="options"
  :loading="isLoading"
  :search-input.sync="search"
  label="Usuario"
  placeholder="Buscar usuario"
  prepend-icon="fas fa-users"
  item-text="fullname"
  return-object
  )
  template(v-slot:no-data) 
    .container No hay usuarios que concuerden con la busqueda

  template(v-slot:selection='{item}')
    .headline {{ item.first_name }} {{ item.last_name }}

  template(v-slot:item='{ item }')
      v-list-item-content
        v-list-item-title {{ item.first_name }} {{ item.last_name }}
        v-list-item-subtitle(v-html='item.username')

</template>
<script>
export default {
  data() {
    return {
      isLoading: false,
      search: null,
      value: null,
      options: [],
      model: this.$django.models.accounts,
      listMethod: "search",
      textField: "name",
      valueField: "name"
    };
  },
  watch: {
    search (val) { 
      if (!val && this.value) return
      this.getOptions(val) 
    },
    value(newVal) {
      this.$emit("input", newVal);
    }
  },
  methods: {
    filterOptions(option){
      if(!this.filtered) return true
      return this.filteredOptions.includes(option.name)
    },
    async getOptions(search) {
      this.isLoading = true
      if (!search || search === '') {
        this.options=[]
        return
      }
      let params = { search: search }
      this.options = await this.model[this.listMethod](params)
      this.isLoading = false
    }
  }
};
</script>