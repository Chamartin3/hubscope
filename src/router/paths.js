export default [
  {
    parent: 'base',
    path: '/login',
    name: 'login',
    component: () => import('@/views/Login.vue')
  },
  {
    parent: 'dashboard',
    path: '/dashboard/main',
    name: 'index',
    component: () => import('@/views/Dashboard.vue')
  }
]
