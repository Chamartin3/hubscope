import moment from 'moment'
const dateFilter = date=> moment(date).format('D, MMMM  YYYY')
const moneyFilter = num=>  parseFloat(num).toLocaleString()
const periodFilter = date=> moment(date).format('D MMM-YYYY')

export {
  dateFilter,
  moneyFilter,
  periodFilter
}
