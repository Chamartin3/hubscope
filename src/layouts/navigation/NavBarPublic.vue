<template lang="pug">
v-app-bar(
  color='primary'
  fixed app
  max-height="60")
  v-toolbar-items.white--text
    v-btn(dark v-for="link in links" text :to="{ name: link.name, params: {} }")  {{link.show_name}}
</template>
<script>
import UserDropdown from '@/layouts/utils/UserDropdown'
export default {
  components: { UserDropdown },
  data () {
    return {
      links: [
        {
          show_name:'Home',
          name:'home'
        },
        {
          show_name:'Libros',
          name:'accountbooks'
        },
        {
          show_name:'Map',
          name:'modelsmap'
        },
        // {
        //   section:'AboutSection',
        //   name:'Información Institucional'
        // },
        // {
        //   section:'CreditsSection',
        //   name:'Beneficios'
        // },
        // {
        //   section:'ContactSection',
        //   name:'Contacto'
        // },
      ]
    }
  },
  methods: {
    goTo (section) {
      if (this.$route.name === 'index') {
        this.scrollTo(section)
      } else {
        this.$router.push(
          {
            name: 'index',
            params: { scroll: section }
          }
        )
      }
    },
    scrollTo (section) {
      this.$vuetify.goTo(`#${section}`, { duration: 800 })
    }
  },
  mounted () {
    console.log(this.$django)
  }
}
</script>
