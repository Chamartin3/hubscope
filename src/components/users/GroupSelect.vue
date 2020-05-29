<template lang="pug">
v-select(
    placeholder="Rol"
    :items="options"
    :item-text="textField",
    :item-value="valueField",
    v-model="value")
  template( v-slot:no-data )
      
</template>
<script>
export default {
  data() {
    return {
      options: [],
      value: "",
      model: this.$django.models.accounts,
      listMethod: "groups",
      textField: "name",
      valueField: "name"
    };
  },
  watch: {
    value(newVal) {
      this.$emit("input", newVal);
    }
  },
  methods: {
    async getOptions() {
      this.options = await this.model[this.listMethod]();
    }
  },
  mounted() {
    this.getOptions();
  }
};
</script>