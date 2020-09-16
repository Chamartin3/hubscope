<template lang='pug'>
v-menu.primary(
  ref="menu"
  dark
  v-model='menu'
  :close-on-content-click='false'
  transition='scale-transition'
  max-width='300px')
  template(v-slot:activator='{ on }')
    .col.text-center
      v-chip(label :color="value ? 'primary darken-3': 'grey'" large
        @click='menu = true') {{ value ? value.name : component.name }}
  .container.primary.justify-center
    .row.justify-center
      .col.text-center
        //- v-select(
        //-   autocomplete
        //-   :label="component.name"
        //-   :items="items",
        //-   item-text="name"
        //-   v-model="value")
        v-autocomplete(
          v-model="value"
          :items="options"
          :loading="isLoading"
          :search-input.sync="search"
          label="Metrica"
          placeholder="Metrica"
          prepend-icon="fas fa-ruler"
          item-text="name"
          item-value="id"
          return-object
          )
          template(v-slot:no-data)
            .container(v-if="!search")
              | Por favor empiece a escribir el nombre de la metrica
              | para buscar las opciones
            .container(v-else)
              | No hay metricas que concuerden con la busqueda
    .row.justify-space-around
      v-btn(color='red'
        x-small
        @click='reset') Cancelar
      v-btn(color='green'
        x-small @click='menu = false'
        ) OK
        //- @click='$refs.menu.save(params)'

</template>
<script>

export default {
  name: 'MenuMetric',
  props: {
    component: {
      type: Object,
      default: null
    }
  },
  data () {
    return {
      value: null,
      items: [],
      menu: false,
      options: [],
      model: this.$django.models.metric,
      listMethod: 'all',
      isLoading: false,
      search: null
    }
  },
  watch: {
    value (val) {
      if (val) this.$emit('input', val.id)
    },
    search (val) {
      if (!val && this.value) return
      this.getOptions(val)
    }
  },
  mounted () {
    this.getItems()
  },
  methods: {
    async getItems () {
      if (!this.company) this.items = await this.$django.models.metric.all()
      else this.items = await this.$django.models.company.reportsByMetric(this.company)
    },
    reset () {
      this.$emit('reset', this.value.id)
      this.value = null
      this.menu = false
    },
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
