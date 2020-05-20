import Vue from 'vue'
import EditableElement from '@/components/base/EditableElement'

const emit = (vnode, name, data) => {
  var handlers = (vnode.data && vnode.data.on) ||
    (vnode.componentOptions && vnode.componentOptions.listeners)

  if (handlers && handlers[name]) {
    handlers[name].fns(data)
  }
}
const emptyComp = Vue.component('empty', {
  template: '<span></span>'
})

Vue.directive('editable', {
  // When the bound element is inserted into the DOM...
  bind: function (el, binding, vnode) {
    // Put the edition button
    let EE = Vue.extend(EditableElement)
    let EEComponent = new EE()
    EEComponent.$vuetify.lang = {}
    EEComponent.$vuetify.lang.t = (x) => x
    EEComponent.payload = binding.value
    EEComponent.$mount()

    // Getting and evaluating the recievenr component
    let element
    let template
    if (vnode.componentInstance) {
      // Asuming that the reciever is a component
      element = vnode.componentInstance.$mount()
      template = element.$el
      EEComponent.$on('edit', e => {
        element.$emit('edit', e)
      })
    } else {
      // Asuming that the reciever is a node
      element = vnode
      template = element.elm
      EEComponent.$on('edit', e => {
        emit(element, 'edit', e)
      })
    }
    vnode.elm = EEComponent.$el
    vnode.elm.classList = template.classList
    template.classList = []
    vnode.elm.childNodes[0].childNodes[0].appendChild(template)
  }
})
