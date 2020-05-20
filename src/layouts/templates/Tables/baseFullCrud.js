// import SSPagination from '@/mixins/serverSidePagination.js'
// import clientSideCrud from '@/mixins/clientSideCrud.js'

import {SSList} from '#/Lists'
// import detailDialog from './DetailDialog'
export default {
  mixins:[SSList],
  data () {
    return {
      filterFields: "look out fields",
      filtering: true,
      searchField:true,
    }
  },
}
