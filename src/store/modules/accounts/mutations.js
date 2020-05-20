// https://vuex.vuejs.org/en/mutations.html

export default {

  updateUser(state, userInfo){
    state.user = userInfo
  },
  updateProfile(state, profileInfo){
    state.profile = profileInfo
    console.log(state)
  },
  updateSocio(state, socioInfo){
    state.socio = socioInfo
  },

}
