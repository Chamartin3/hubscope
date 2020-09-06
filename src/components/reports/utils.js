import moment from 'moment'
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
      let begin = moment(item.begin)
      let end = moment(item.end)
      const sameYear = begin.year() === end.year()
      const sameMonth = begin.month() === end.month()
      const sameDay = begin.day() === end.day()
      let format
      let complement
      if (sameYear && sameMonth && sameDay) return begin.format('DD, MMMM YYYY')
      if (sameYear && sameMonth) {
        format = 'DD'
        complement = ` de ${begin.format('MMMM-YYYY')}`
      } else if (sameYear) {
        format = 'DD MMMM'
        complement = ` de ${begin.format('YYYY')}`
      }
      return `Desde ${begin.format(format)} hasta ${end.format(format)} ${complement}`
    },
    days (item) {
      if (item.days === 1) return `${1} dia`
      return `${item.dias} dias`
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
