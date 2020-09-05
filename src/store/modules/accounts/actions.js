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
  getUserInfo ({ commit, state }, id) {
    django.models.accounts.get_information(id).then(
      done => {
        commit('updateUser', done)
      },
      fail => failCalback)
  },
  async getProfile ({ commit, getters, dispatch }, user_id) {
    django.models.profile.userProfile({ user_id: user_id }).then(
      done => {
        if (getters.isInGroup('socio')) dispatch('getSocioLeg', done.cedula)
        commit('updateProfile', done)
      },
      fail => failCalback)
  },
  async getSocioLeg ({ commit, state }, cedula) {
    django.models.socios.getFromCedula({ cedula: cedula }).then(
      done => {
        commit('updateSocio', done)
      },
      fail => failCalback)
  }
}
