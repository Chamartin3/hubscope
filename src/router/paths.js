export default [
  {
    parent: 'base',
    path: 'login',
    name: 'login',
    component: () => import('@/views/Login.vue')
  },
  {
    parent: 'dashboard',
    path: 'main',
    name: 'index',
    show_name: 'Inicio',
    show_icon: 'fa-home',
    access:null,
    component: () => import('@/views/Dashboard.vue')
  },
  {
    parent: 'dashboard',
    path: 'users',
    name: 'users',
    show_name: 'Usuarios',
    show_icon: 'fa-users',
    access:null,
    component: () => import('@/views/Users.vue')
  },
  {
    parent: 'dashboard',
    path: 'companies',
    name: 'companies',
    show_name: 'Compañias',
    show_icon: 'fa-building',
    access:null,
    component: () => import('@/views/Dashboard.vue')
  }
]
