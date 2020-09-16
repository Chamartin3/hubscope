import moment from 'moment'
moment.locale('es')
const SSDATE_FORMAT = 'DD/MM/YY'

const goalStatuses = {
  'good': {
    color: 'success'
  },
  'medium': {
    color: 'warning'
  },
  'bad': {
    color: 'red'
  }
}

const simpleRangeMini = function (begin, end) {
  const sameYear = begin.year() === end.year()
  const sameMonth = begin.month() === end.month()
  const sameDay = begin.day() === end.day()
  let format
  let complement
  if (sameYear && sameMonth && sameDay) return begin.format('DD, MMMM YYYY')
  if (sameYear && sameMonth) {
    format = 'DD'
    complement = ` ${begin.format('MMMM-YYYY')}`
  } else if (sameYear) {
    format = 'DD MMMM'
    complement = ` ${begin.format('YYYY')}`
  }
  return `${begin.format(format)} a ${end.format(format)} ${complement}`
}

const simpleRange = function (initialbegin, initialend, formato = null) {
  let begin
  let end
  if (formato) {
    begin = moment(initialbegin).format(formato)
    end = moment(initialend).format(formato)
  } else {
    begin = moment(initialbegin)
    end = moment(initialend)
  }
  const sameYear = begin.year() === end.year()
  const sameMonth = begin.month() === end.month()
  const sameDay = begin.date() === end.date()

  let format = 'DD, MMMM YYYY'
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
}

const nulluser = function (user) {
  if (user) return user.fullname
  return 'Sistema Automatizado'
}
const period = function (item) {
  let begin = moment(item.begin).format('DD MMM-YYYY')
  let end = moment(item.end).format('DD MMM-YYYY')
  return `${begin} - ${end}`
}
const days = function (item) {
  if (item.days === 1) return `${1} dia`
  return `${item.dias} dias`
}

const readableDate = function (time) {
  return moment(time).format('dddd, DD MMMM YYYY')
}

const readableDateMini = function (time) {
  return moment(time).format('DD MMMM YYYY')
}

const days_until = function (time) {
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
}

const number = function (num) {
  return parseInt(num).toLocaleString()
}

const filterLabels = function (label) {
  const FORMAT = 'DD-MMM YY'
  let d = label.split('-')

  let b = moment(d[0], 'DD/MM/YY').format(FORMAT)
  let e = moment(d[1], 'DD/MM/YY').format(FORMAT)

  if (b == e) return `${b}`
  return `${b} a ${e}`
}

export {
  filterLabels,
  number,
  days_until,
  readableDate,
  days,
  period,
  nulluser,
  readableDateMini,
  SSDATE_FORMAT,
  goalStatuses,
  simpleRange,
  simpleRangeMini
}
