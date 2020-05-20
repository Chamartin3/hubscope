import base from './baseList'
import { CSPagination, SSPagination } from './pagination'
import { baseSearch, CSSearch } from './search'
import { baseFilters, CSFilters } from './filter'
import serverSide from './severSide'


const SSList = {
  mixins:[base, baseSearch, baseFilters, serverSide, SSPagination ]
}

const CSList = {
  mixins:[base, CSSearch, CSFilters, CSPagination]
}



export {
  base,
  serverSide,

  SSList,
  CSList
}
