export default [
  {
    path: '',
    name: 'base',
    component: () => import('@/layouts/LayoutPublic.vue'),
    redirect: 'login'
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: () => import('@/layouts/LayoutDashboard.vue'),
    redirect: '/dashboard/main'
  }
]
