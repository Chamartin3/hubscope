// https://vuex.vuejs.org/en/actions.html

function failCalback (fail) {
  let msg = fail.detail ? fail.detail : fail.message ? fail.message : fail
  commit('showAlert', {
    type: 'Danger',
    tit: 'error',
    msg: msg
  })
}

export default {

}
