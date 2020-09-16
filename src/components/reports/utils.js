import moment from 'moment'
import { simpleRange } from '@/components/utils'

const Statuses = {
  cerrada: {
    'color': 'grey',
    'name': 'Cerrado',
    'desc': 'El reporte no puede ser modificado'
  },
  entregada: {
    'color': 'green',
    'name': 'Entegado',
    'desc': 'El reporte ya fué entregado'
  },
  esperando: {
    'color': 'secondary lighten-1',
    'name': 'Evaluando',
    'desc': 'El reporte aun esta dentro de los tiempos estipulados'
  },
  abierta: {
    'color': 'warning',
    'name': 'En Espera',
    'desc': 'Esperando por la entrega del reporte'
  },
  atrasada: {
    'color': 'red',
    'name': 'Atrasado',
    'desc': 'El reporte no se ha entregado a tiempo'
  },
  activa: {
    'color': 'green darken-2',
    'name': 'Activo',
    'desc': 'El reporte se esta usando como punto de referencia'
  }
}
const Filters = {
  methods: {
    ___simplyfy_period (begin, end) {

    }
  },
  filters: {
    date (time) {
      return moment(time).format('dddd, DD MMMM YYYY')
    },
    minidate (time) {
      return moment(time).format('dddd, DD MMM-YY')
    },
    nulluser (user) {
      if (user) return user.fullname
      return 'Sistema Automatizado'
    },
    period (item) {
      let begin = moment(item.begin).format('DD MMM-YYYY')
      let end = moment(item.end).format('DD MMM-YYYY')
      return `${begin} - ${end}`
    },
    simpleperiod: item => {
      return simpleRange(item.begin, item.end)
    },
    days (item) {
      if (item.days === 1) return `${1} dia`
      return `${item.days} dias`
    },
    days_until (time) {
      let dias = moment(time).diff(moment(), 'days')
      if (dias === 0) return `Hoy`
      let text
      if (dias < 0) {
        dias = -dias
        text = `Hace ${dias} `
      } else {
        text = `Dentro de ${dias} `
      }
      if (dias == 1) return text + 'dia'
      return text + 'dias'
    },
    number (num) {
      return parseInt(num).toLocaleString()
    }
  }
}
export {
  Statuses,
  Filters
}
