const Statuses = {
  cerrada:{
    'color':'gray',
    'name':'Cerrado',
    'desc':'El reporte no puede ser modificado'
  },
  entregada:{
    'color':'green',
    'name':'Entegado',
    'desc':'El reporte ya fué entregado'
  },
  esperando:{
    'color':'secondary lighten-1',
    'name':'Evaluando',
    'desc':'El reporte aun esta dentro de los tiempos estipulados'
  },
  abierta:{
    'color':'warning',
    'name':'En Espera',
    'desc':'Esperando por la entrega del reporte'
  },
  atrasada:{
    'color':'red',
    'name':'Atrasado',
    'desc':'El reporte no se ha entregado a tiempo'
  }
}

export {
  Statuses
}