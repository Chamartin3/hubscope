import Vue from 'vue'

const DJANGO = Vue.$django ? Vue.$django : DJANGO_CONTEXT || null
const USER_AUTH = DJANGO ? DJANGO.user : DJANGO
const USER_GROUPS = USER_AUTH ? USER_AUTH.groups.map(x => x.name) : []

// Navigation Guards

const beforeEach = function (to, from, next) {
  let goingToLogin = to.name === 'login'
  if (!USER_AUTH) {
    if (!goingToLogin) next({ name: 'login' })
    else next()
  } else if (to.name === 'login') {
    next({ name: 'main' })
  } else {
    next()
  }
}

const beforeResolve = function (to, from, next) {
  return to
}

const afterEach = function (to, from, next) {
  return to
}

// Access Filters

const groupAccess = function (path) {
  if (!path.access) return true
  if (USER_GROUPS.includes('Admin')) return true
  for (var i = 0; i < USER_GROUPS.length; i++) {
    if (path.access.groups.includes(USER_GROUPS[i])) return true
  }
  return false
}

const FILTERS = [ groupAccess ]

const accessFilters = function (path) {
  for (let i = 0; i < FILTERS.length; i++) {
    if (!FILTERS[i](path)) return false
  }
  return true
}

export {
  beforeEach,
  beforeResolve,
  afterEach,
  accessFilters
}
