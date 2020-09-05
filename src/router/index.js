import Vue from 'vue'
import Router from 'vue-router'

import paths from '@/router/paths'
import { beforeEach, accessFilters } from '@/router/guards'
import Gates from '@/router/gates'
import basePaths from '@/router/basePaths'

const DJANGO = Vue.$django ? Vue.$django : DJANGO_CONTEXT || null

// Rutas padre e hijas
function route (path) {
  return {
    name: path.name,
    path: path.path,
    component: path.component,
    meta: { ...path }
  }
}

let routes = basePaths.map(function (parent) {
  let children = paths
    .filter(x => x.parent === parent.name)
    .filter(accessFilters)
    .map(Gates)
  return {
    ...parent,
    component: parent.component,
    children: children.map(x => route(x))
  }
})

console.log(routes)
// NavPaths
let NavPaths
NavPaths = Vue.$django ? Vue.$django.navigation_paths : ''
let FinalRoutes = NavPaths ? routes.concat(NavPaths) : routes

console.log(FinalRoutes)
// Router
const ROUTER = new Router({
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

// Navigation Guards
ROUTER.beforeEach(beforeEach)
Vue.use(Router)

export default ROUTER
