import Vue from 'vue'
import LoadingComponent from '@/layouts/utils/Loading'

import DeleteConfirmation from './deleteConfirmDialog'
import DynamicField from './DynamicField'
import EditableElement from './EditableElement'
import ModalEdit from './ModalEdit'
import DaySelect from './DaySelect'
import RangeSelect from './RangeSelect'



Vue.component('LoadingComponent', LoadingComponent)
Vue.component('DeleteConfirmation', DeleteConfirmation)
Vue.component('EditableElement', EditableElement)
Vue.component('DynamicField', DynamicField)
Vue.component('ModalEdit', ModalEdit)
Vue.component('DaySelect', DaySelect)
Vue.component('RangeSelect', RangeSelect)
