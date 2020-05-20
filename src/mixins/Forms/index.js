
import baseFormMixin from './baseForm'
import mainFormMixin from './mainForm'
import subFormMixin from './subForm'

import errorsMixin from './formErrors'
import viewModeMixin from './viewMode'
import fileForm from './fileForm'

const baseMainForm ={
  mixins:[baseFormMixin, mainFormMixin, errorsMixin]
}

const baseSubForm ={
  mixins:[baseFormMixin, subFormMixin, errorsMixin]
}


export {
  // base
  baseFormMixin,
  mainFormMixin,
  subFormMixin,

  // extras
  errorsMixin,
  viewModeMixin,
  fileForm,

  // bundles
  baseMainForm,
  baseSubForm
}
