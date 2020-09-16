import Vue from 'vue'
import LoadingComponent from '@/layouts/utils/Loading'

import backButton from './backButton'
import GeneralPagination from './GeneralPagination'
import lightCard from './lightCard'
Vue.component('BackButton', backButton)
Vue.component('LightCard', lightCard)
Vue.component('GeneralPagination', GeneralPagination)
