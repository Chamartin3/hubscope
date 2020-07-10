import Vue from 'vue'
import Vuetify from 'vuetify/lib'// Icons
import '@fortawesome/fontawesome-free/css/all.css'

Vue.use(Vuetify)

export default new Vuetify({
  theme: {
    options: {
      customProperties: true
    },
    themes: {
      dark: {
        primary: '#68bc2',
        background: '#DC1F1F'
      },
      light: {
        primary: '#68bc2',
        // primary: '#8c8c8c',
        terciary: '#25AAE1',
        secondary: '#F27023',
        fouth: '#B95106',
        error: '#F71212',
        info: '#2196F3',
        success: '#4CAF50',
        warning: '#d19e04',
        ////////////////////////
      }
    }
  },
  icons: {iconfont: 'fa'}
})
