import Vue from 'vue'

Vue.config.productionTip = false
Vue.prototype.$alert = function (type = 'success', tit = '', text = '') {
  this.$store.commit('showAlert', {
    type: type,
    tit: tit,
    msg: text
  })
}
