<template lang="pug">
div
  v-pagination(
    v-model="page"
    v-if="pagination.total > pagination.per_page"
    :color="color"
    class="my-4",
    :circle="circle"
    total-visible="5"
    :length="pagination.last_page")
  .col.text-center
    .overline(v-if="pagination.total > pagination.per_page")  mostrando de {{ pagination.from }} hasta {{ pagination.to }}
    .overline(v-if="thereIsPagination" ) {{ pagination.total }} {{ pagination.total === 1 ? names.singular : names.plural  }} en total
    slot

</template>
<script>
export default {
  name: 'GeneralPagination',
  props: {
    value: {
      type: Number,
      required: true
    },
    pagination: {
      type: Object,
      required: true
    },
    names: {
      type: Object,
      default () {
        return {
          plural: 'objeto',
          singular: 'objetos'
        }
      }
    },
    color: {
      type: String,
      default: 'primary'
    },
    circle: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      page: this.value
    }
  },
  computed: {
    thereIsPagination () {
      if (Object.keys(this.pagination).length) return true
      return false
    }
  },
  watch: {
    page (val) { this.$emit('input', val) }
  }
}
</script>
