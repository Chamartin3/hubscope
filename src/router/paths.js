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
    show_name: 'Empresas',
    show_icon: 'fa-building',
    access:null,
    component: () => import('@/views/Companies.vue')
  },    
  {
    parent: 'dashboard',
    path: 'reports',
    name: 'reports',
    show_name: 'Reportes',
    show_icon: 'fas fa-tasks',
    access:null,
    component: () => import('@/views/Reports.vue')
  },  
  {
    parent: 'dashboard',
    path: 'empresa/:id',
    name: 'empresa',
    show_name: 'Empresa',
    access:null,
    hide:true,
    component: () => import('@/views/Empresa.vue')
  },   
  {
    parent: 'dashboard',
    path: 'informe/empresa/:id',
    name: 'resumen_empresa',
    show_name: 'Resumen Metas',
    access:null,
    hide:true,
    component: () => import('@/views/InformeEmpresa.vue')
  },  
  // {
  //   parent: 'dashboard',
  //   path: 'empresa/:id/reports',
  //   name: 'empresa',
  //   show_name: 'Empresa',
  //   access:null,
  //   hide:true,
  //   component: () => import('@/views/Company/Reports.vue') 
  // },  
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
