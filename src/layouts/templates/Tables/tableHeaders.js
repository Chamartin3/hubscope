
const generateHeaders= function addHeaders(list=[], def=true ) {
  // Table Headers
  // {
  //   text: string
  //   value: string
  //   align?: 'start' | 'center' | 'end'
  //   sortable?: boolean
  //   filterable?: boolean
  //   divider?: boolean
  //   class?: string | string[]
  //   width?: string | number
  //   filter?: (value: any, search: string, item: any) => boolean
  //   sort?: (a: any, b: any) => number
  // }
  const DEFAULT_HEADERS=[
    {
      sortable: false,
      text: 'Detail',
      value: 'actions',
      align: 'center'
    },
    {
      sortable: false,
      text: 'Delete',
      value: 'delete',
      align: 'center'
    }
  ]
  let produced =list.map(el=>{
    let BASE={
        sortable: true,
        text: el,
        value: el,
        align: 'center'
      }

    if (typeof el === 'string') {
      BASE['text']=el
      BASE['value']=el
      return BASE
    }
    if (typeof el === 'object') {
      return {...BASE, ...el}
    }
  })
  if (def) return produced.concat(DEFAULT_HEADERS)
  return produced
}

export default generateHeaders
