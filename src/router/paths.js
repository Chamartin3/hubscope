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
    name: 'main',
    show_name: 'Inicio',
    show_icon: 'fa-home',
    access: null,
    component: () => import('@/views/Dashboard.vue')
  },
  {
    parent: 'dashboard',
    path: 'users',
    name: 'users',
    show_name: 'Usuarios',
    show_icon: 'fa-users',
    access: { groups: [ 'Admin', 'Gerente' ] },
    component: () => import('@/views/Users.vue')
  },
  {
    parent: 'dashboard',
    path: 'companies',
    name: 'companies',
    show_name: 'Empresas/Oficinas',
    show_icon: 'fa-building',
    access: { groups: [ 'Admin', 'Gerente' ] },
    component: () => import('@/views/Companies.vue')
  },
  {
    parent: 'dashboard',
    path: 'reports',
    name: 'reports',
    show_name: 'Reportes',
    show_icon: 'fas fa-file-alt',
    access: { groups: [ 'Admin', 'Gerente', 'Registrador' ] },
    component: () => import('@/views/Reports.vue')
  },
  {
    parent: 'dashboard',
    path: 'asignaciones',
    name: 'asignaciones',
    show_name: 'Asignaciones',
    show_icon: 'fas fa-tasks',
    access: { groups: [ 'Admin', 'Gerente', 'Registrador' ] },
    component: () => import('@/views/Asignaciones.vue')
  },
  {
    parent: 'dashboard',
    path: 'indicators',
    name: 'indicadores',
    show_name: 'Indicadores',
    show_icon: 'fas fa-chart-pie',
    access: { groups: [ 'Admin', 'Gerente', 'Registrador' ] },
    component: () => import('@/views/Indicators.vue')
  },
  {
    parent: 'dashboard',
    path: 'metas',
    name: 'goals',
    show_name: 'Metas',
    show_icon: 'fas fa-bullseye',
    access: { groups: [ 'Admin', 'Gerente' ] },
    component: () => import('@/views/Goals.vue')
  },
  {
    parent: 'dashboard',
    path: 'empresa/:id',
    name: 'empresa',
    show_name: 'Empresa',
    access: null,
    hide: true,
    component: () => import('@/views/Empresa.vue'),
    redirect: 'empresa/:id/reports',
    children: [
      {
        path: 'reports',
        name: 'reporte-empresa',
        meta: {
          show_name: 'Reportes de Organización'
        },
        access: null,
        hide: true,
        component: () => import('@/views/Company/Reports.vue')
      },
      {
        parent: 'dashboard',
        path: 'asigments',
        name: 'tareas-empresa',
        meta: {
          show_name: 'Tareas de Organización'
        },
        access: null,
        hide: true,
        component: () => import('@/views/Company/Asignments.vue')
      },
      {
        parent: 'dashboard',
        path: 'indicators',
        name: 'indicators-empresa',
        meta: {
          show_name: 'Metricas de Organización'
        },
        access: null,
        hide: true,
        component: () => import('@/views/Company/Indicators.vue')
      }

    ]

  },

  {
    parent: 'dashboard',
    path: 'informe/empresa/:id',
    name: 'resumen_empresa',
    show_name: 'Resumen Metas',
    access: null,
    hide: true,
    component: () => import('@/views/InformeEmpresa.vue')

  }

  // {
  // {
  //   parent: 'dashboard',
  //   path: 'empresa/:id/asigments',
  //   name: 'empresa',
  //   show_name: 'Empresa',
  //   access:null,
  //   hide:true,
  //   component: () => import('@/views/Company/Asignments.vue')
  // },
  // {
  //   parent: 'dashboard',
  //   path: 'empresa/:id/reports',
  //   name: 'empresa',
  //   show_name: 'Empresa',
  //   access:null,
  //   hide:true,
  //   component: () => import('@/views/Company/Asignments.vue')
  // }
]
