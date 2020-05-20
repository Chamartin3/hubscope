import Vue from 'vue'

Vue.directive('vdj-role', {
  bind: function (el, binding, vnode) {
    let self = vnode.context
    let comp_rol = binding.value
    let user_rol = self.$django.user.rol
    let evaluation = comp_rol >= user_rol
    let comp = new emptyComp().$mount()

    if (!evaluation) {
      vnode.elm = comp.$el
    }
  }
})

Vue.directive('vdj-evperm', {
  bind: function (el, binding, vnode) {
    let self = vnode.context
    let perm = binding.value
    let perms = self.$django.user.permissions
    let evaluation = perms.includes(perm)
    if (!evaluation) vnode.elm.parentElement.removeChild(vnode.elm)
  }
})

Vue.directive('vdj-evgroups', {
  bind: function (el, binding, vnode) {
    if (!binding.value) {
      console.error('A string with the autorized groups is necesary to use the vdj-evgroups directive')
    } else {
      let self = vnode.context
      let evaluation = true
      let allowedGroups = binding.value.split(',')
      if (self.$django.user) {
        let user_group_names = self.$django.user.groups.map(x => x.name)
        evaluation = false
        for (var i = 0; i < allowedGroups.length; i++) {
          if (user_group_names.includes(allowedGroups[i])) {
            evaluation = true
            break
          }
        }
      } else {
        evaluation = false
      }

      if (!evaluation) el.parentNode.removeChild(el)
    }
  }
})
