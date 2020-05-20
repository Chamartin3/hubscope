export default {
  data() {
    return {
      edit_form_var: false
    }
  },
  methods: {
    toggleEdition() {
      this.edit_form_var = !this.edit_form_var
    }
  },
  computed: {
    viewMode() {
      if (this.subForm) {
        return this.$parent.viewMode
      } else if (this.mode === 'creation') {
        return false
      } else {
        if (this.edit_form_var) { return false }
        return true
      }
    }
  }
}
