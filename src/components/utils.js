import moment from 'moment'
moment.locale('es');
const SSDATE_FORMAT = 'DD/MM/YY'

const goalStatuses = {
  'good':{
    color:"success"
  },
  'medium':{
    color:"warning"
  },
  'bad':{
    color:"red"
  },
}



const nulluser = function (user){
  if (user) return user.fullname
  return 'Sistema Automatizado'
}
const period = function (item){
  let begin = moment(item.begin).format('DD MMM-YYYY')
  let end = moment(item.end).format('DD MMM-YYYY')
  return `${begin} - ${end}`
}
const days = function (item){
  if(item.days===1) return `${1} dia` 
  return `${item.dias} dias`
}

const readableDate = function (time){
  return moment(time).format('dddd, DD MMMM YYYY')
}

const readableDateMini = function (time){
  return moment(time).format('DD MMMM YYYY')
}

const days_until = function (time) {
  let dias = moment(time).diff(moment(),'days')
  if(dias===0) return `Hoy` 
  let text
  if(dias<0){
    dias = -dias
    text = `Hace ${dias} `
  }else{
    text = `Dentro de ${dias} `
  }
  if (dias==1) return text+'dia'
  return text+'dias'
}

const number = function (num) {
  return parseInt(num).toLocaleString()
}

const filterLabels = function (label) {

  const FORMAT = "DD-MMM YY"
  let d = label.split('-')

  let b = moment(d[0], 'DD/MM/YY').format(FORMAT)
  let e = moment(d[1], 'DD/MM/YY').format(FORMAT) 
  
  if (b==e) return `${b}`
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
  goalStatuses
}