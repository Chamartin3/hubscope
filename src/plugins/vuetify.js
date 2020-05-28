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
      light: {
        terciary: '#25AAE1',
        secondary: '#F27023',
        primary: '#0C3173',
        fouth: '#B95106',
        error: '#F71212',
        info: '#2196F3',
        success: '#4CAF50',
        warning: '#FFC107'
      }
    }
  },
  icons: {iconfont: 'fa'}
})
