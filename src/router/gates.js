import Vue from 'vue'

const DJANGO = Vue.$django ? Vue.$django : DJANGO_CONTEXT || null
const USER_AUTH = DJANGO ? DJANGO.user : DJANGO
const USER_GROUPS = USER_AUTH ? USER_AUTH.groups.map(x => x.name) : []

// Route callbacks

const MAIN = function (path) {
  if (USER_GROUPS.includes('Admin')) path.component = () => import('@/views/Dashboard.vue')
  else path.component = () => import('@/views/Dashboard.vue')
  return path
}

const GATELIST = {
  main: MAIN
}

// Gate Procesing
const Gates = path => {
  for (var [pathname, callback] of Object.entries(GATELIST)) {
    if (path.name === pathname) path = callback(path)
  }
  return path
}

export default Gates
