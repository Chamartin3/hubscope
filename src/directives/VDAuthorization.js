import Vue from 'vue'

Vue.directive('django-role', {
  inserted: function (el, binding, vnode) {
    let self = vnode.context
    let comp_rol = binding.value
    let user_rol = self.$django.user.rol
    let evaluation = comp_rol >= user_rol
    if (!evaluation) vnode.elm.parentNode.removeChild(vnode.elm)
  }
})

Vue.directive('django-groups', {
  inserted: function (el, binding, vnode) {
    const DJANGO = vnode.context.$root.$django

    if (!binding.value) {
      console.error('A string with the autorized groups is necesary to use the django-groups directive')
      return
    }

    let userGroups = DJANGO.user.groups.map(x => x.name)
    let allowedGroups = binding.value.split(',')
    let evaluation = false
    for (var i = 0; i < allowedGroups.length; i++) {
      if (userGroups.includes(allowedGroups[i])) {
        evaluation = true
        break
      }
    }
    if (!evaluation) vnode.elm.parentElement.removeChild(vnode.elm)
  }
})
