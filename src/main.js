import Vue from 'vue'
import vuetify from './plugins/vuetify'
import router from './router/index'
import store from './store'
import './plugins'
import './directives'
import './components/base'


Vue.config.productionTip = false
import App from './App.vue'

new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')
