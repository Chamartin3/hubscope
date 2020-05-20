// https://vuex.vuejs.org/en/getters.html

export default {
  isInGroup: (state) => (group) => {
    let user_group_names = state.user.groups.map(x=>x.name)
    if (user_group_names.includes(group)) return true
    else return false
  }
}
