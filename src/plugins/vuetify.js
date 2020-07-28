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
        primary: '#a1a1a1',
        secondary: '#F27023',
        terciary: '#25AAE1',
        typing: '#262626',
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
