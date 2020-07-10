<template lang='pug'>
v-menu.primary(
  ref="menu"
  dark
  v-model='menu'
  :close-on-content-click='false'
  transition='scale-transition')
  template(v-slot:activator='{ on }')
    .col.text-center
      v-chip(
        color="primary darken-3"
        @click='menu = true') {{ txtfilter(value) }}
      .overline {{ desc }}
  slot
    v-date-picker(
      :max="max"
      :min="min"
      v-model='value' no-title scrollable)
        .row.justify-space-around 
          v-btn(color='red' @click='menu = false') Cancelar
          v-btn(color='green' @click='save' ) OK    
</template>
<script>
export default {
  name: 'ChipDaySelect',
  props: {
    free:{
      default:false
    },
    desc:{
      default:''
    },
    txtfilter:{
      type: Function,
      default : (x)=>x
    },
    min:{
      default:null
    },
    max:{
      default:null
    },
    
  },
  data() {
    return {
      menu: false,
      value:null
    }
  },
  methods: {
    save(){
      this.$refs.menu.save(this.value)
      this.$emit('input',this.value)
    }
  },
  watch: {
    value(val){
      if(this.free) this.$emit('input',val)
    },
    '$attrs.value':{
      immediate:true,
      handler(val){
        this.value= val
      }
    }
  },
}
</script>