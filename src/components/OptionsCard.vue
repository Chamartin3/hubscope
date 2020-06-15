<template lang="pug">
v-card.mx-auto(:color='ccolor' dark min-width='250')
  v-card-title.justify-space-around 
      .headline Opacidad
      .headline {{ cocient }}
  v-card-text.headline.font-weight-bold
    v-btn( icon @mousedown="start" 
      @mouseleave="stop" 
      @mouseup="stop" 
      @touchstart="start" 
      @touchend="stop" 
      @touchcancel="stop")
      v-icon far fa-caret-square-up    
    v-btn( icon @mousedown="startdown" 
      @mouseleave="stop" 
      @mouseup="stop" 
      @touchstart="startdown" 
      @touchend="stop" 
      @touchcancel="stop")
      v-icon far fa-caret-square-down
    v-btn(@click='setColor') Seleccionar
    
</template>
<script>
export default {
    props: ['color', 'icon', 'titulo', 'subtitle'],
    data() {
      return {
        cocient:10,
        interval:false,
      }
    },
    computed: { 
      ccolor(){
        return this.LightenDarkenColor(this.color, this.cocient)
        // return this.$vuetify.theme.themes.light[this.color]
      },
    },
    methods: {
        LightenDarkenColor(col, amt) {
          var usePound = false;
          if ( col[0] == "#" ) {
              col = col.slice(1);
              usePound = true;
          }
          var num = parseInt(col, 16);
          var r = (num >> 16) + amt;
          var b = ((num >> 8) & 0x00FF) + amt;
          var g = (num & 0x0000FF) + amt;
          var newColor = g | (b << 8) | (r << 16);
          return (usePound?"#":"") + (g | (b << 8) | (r << 16)).toString(16);
      },
      setColor(){
        this.$vuetify.theme.themes.light.primary=this.ccolor
      },
      	start(){
        if(!this.interval){
          this.interval = setInterval(() => this.cocient++, 30)	
        }
      },
      stop(){
        clearInterval(this.interval)
        this.interval = false
      },
      startdown(){
        if(!this.interval){
          this.interval = setInterval(() => this.cocient--, 30)	
        }
      },
    }
}
</script>