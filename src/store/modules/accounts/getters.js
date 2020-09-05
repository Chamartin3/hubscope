// https://vuex.vuejs.org/en/getters.html

export default {
  isInGroup: (state) => (group) => {
    let groupNames = state.user.groups.map(x => x.name)
    if (groupNames.includes(group)) return true
    else return false
  }
}
