import Vue from 'vue'
import Router from 'vue-router'

import paths from '@/router/paths'
import { beforeEach, groupAccessFilter, mainPageFilter } from '@/router/guards'
import basePaths from '@/router/basePaths'
const DJANGO = Vue.$django ? Vue.$django : DJANGO_CONTEXT ? DJANGO_CONTEXT : null
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

function accessFilter(path){
  if (!path.access) return true
  let ugroups= DJANGO.user ? DJANGO.user.groups.map(x=>x.name) : []
  if(ugroups.includes('admin')) return true
  for (var i = 0; i < ugroups.length; i++) {
    if(path.access.groups.includes(ugroups[i])) return true
  }
  return false
}


let routes = basePaths.map(function (parent) {
  // console.log(paths);
  let children = paths.filter(x => x.parent === parent.name).filter(groupAccessFilter)
  // console.log(children);
  return {
    ...parent,
    component: parent.component,
    children: children.map(x => route(x))
  }
})

let FinalRoutes = NavPaths ? routes.concat(NavPaths) : routes

const ROUTER =  new Router({
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

ROUTER.beforeEach(beforeEach)

export default ROUTER