import Vue from 'vue'

const isObj = o => o?.constructor === Object;
function assignToPath(obj, keyPath, value, merge) {
  var current = obj
  keyPath.forEach(function (key, index) {
    if (!current[key]) current[key] = {}
    if (index === keyPath.length -1) {
      if (merge){
        if(isObj(value) && !isObj(current[key])) current[key] = {}
        current[key] = Object.assign(current[key],value) 
      } else {
        current[key] = value 
      }
    } 
    else current = current[key]
  })
}

Vue.directive('modelMod', {
  bind: function (el, binding, vnode) {
    // .merge Merge the destiny object with a new object
    // .attr asumes that the value is an object and gets an atribute
    let knownModifiers = [
      'attr', 
      'merge'
    ]
    let mod = binding.modifiers
    let attr = binding.arg
    let path = binding.expression.split('.')
    let unknownMod
    Object.keys(mod).forEach(function (key) {
      if (!knownModifiers.includes(key)) unknownMod = key
    })
    if (unknownMod) console.error(`${unknownMod} modifier is unknown`) 

    vnode.componentInstance.$on('input', function(value) {  
      if (mod.attr) {
        value = value[attr]
      }    
    assignToPath(vnode.context._data, path, value, mod.merge)
    })
  }
})
