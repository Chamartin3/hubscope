import Vue from 'vue'
import vuetify from './plugins/vuetify'
import router from './router'
import store from './store'
import './plugins'
import './directives'
import './components/base'
import './components/global'
import App from './App.vue'

Vue.config.productionTip = false

new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')
