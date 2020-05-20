<template lang="pug">
v-hover(v-slot:default="{ hover }", open-delay="200")
  v-card.ma-4(:elevation="hover ? 16 : 2")
    v-img(
      :gradient="hover ? hoverGradient : gradient"
      :src="image",
      height="30vh")
      v-container(fill-height)
        v-row.text-left(align="start")
          v-col
            h1.display-2.white--text.font-weight-black.tit {{title}}
        v-row(align="end")
          v-col.text-right
            slot
              v-tooltip(bottom)
                template(v-slot:activator="{ on }")
                  v-btn.gray--text(color="gray"  v-on="on") Solicitar
                span Proximamente
</template>
<script >
export default {
  name: "imageCard",
  props:{
    image:{default:null},
    title:{default:null},
    gradient:{default:null},
    hoverGradient:{default:null}}
}
</script>
