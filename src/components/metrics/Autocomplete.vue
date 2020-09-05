<template lang="pug">
v-autocomplete(
  v-model="form"
  :items="options"
  :loading="isLoading"
  :search-input.sync="search"
  label="Metrica"
  placeholder="Metrica"
  prepend-icon="fas fa-ruler"
  item-text="name"
  item-value="id"
  return-object
  :error-messages="errors.name"
  )
  template(v-slot:no-data)
    .container
      | No hay metricas que concuerden con la busqueda
      //- v-btn Crear

  //- template(v-slot:selection='{item}')
  //-   .headline {{ item.first_name }} {{ item.last_name }}

  //- template(v-slot:item='{ item }')
  //-     v-list-item-content
  //-       v-list-item-title {{ item.first_name }} {{ item.last_name }}
  //-       v-list-item-subtitle(v-html='item.username')

</template>
<script>
import { baseSubForm } from '#/Forms'

export default {
  mixins: [baseSubForm],
  data () {
    return {
      isLoading: false,
      search: null,
      form: {
        name: null
      },
      options: [],
      model: this.$django.models.metric,
      listMethod: 'all',
      textField: 'name',
      valueField: 'name'
    }
  },
  watch: {
    search (val) {
      if (!val && this.value) return
      this.getOptions(val)
    }
    // value(newVal) {
    //   this.$emit("input", newVal);
    // }
  },
  methods: {
    filterOptions (option) {
      if (!this.filtered) return true
      return this.filteredOptions.includes(option.name)
    },
    onInput () {
      this.cleanInErrors()
    },
    async getOptions (search) {
      this.isLoading = true
      if (!search || search === '') {
        this.options = []
        return
      }
      let params = { search: search }
      this.options = await this.model[this.listMethod](params)
      this.isLoading = false
    }
  }
}
</script>
