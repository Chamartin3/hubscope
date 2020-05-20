import baseModal from './baseModal'
import instanceMixin from './instanceModal'
import formMixin from './modalForm'

const instanceModal = {
  mixins:[ baseModal, instanceMixin ]
}
const formModal = {
  mixins:[ baseModal, formMixin ]
}

export {
  baseModal,
  instanceModal,
  formModal
}
