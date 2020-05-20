import Vue from 'vue'
import Router from 'vue-router'

import paths from '@/router/paths'
import basePaths from '@/router/basePaths'

Vue.use(Router)

let NavPaths
NavPaths = Vue.$django ? Vue.$django.navigation_paths : ''

function route (path) {
  return {
    name: path.name,
    path: path.path,
    component: path.component,
    meta: { ...path }
  }
}

let routes = basePaths.map(function (parent) {
  let children = paths.filter(x => x.parent === parent.name)
  return {
    ...parent,
    component: parent.component,
    children: children.map(x => route(x))
  }
})

let FinalRoutes = NavPaths ? routes.concat(NavPaths) : routes

export default new Router({
  mode: 'history',
  routes: FinalRoutes,
  scrollBehavior (to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    }
    if (to.hash) {
      return { selector: to.hash }
    }
    return { x: 0, y: 0 }
  }
})
