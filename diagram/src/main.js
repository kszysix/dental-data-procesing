// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'

import { library } from '@fortawesome/fontawesome-svg-core'
import { faTooth } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { BModal, BButton, TabsPlugin, FormInputPlugin, BForm, FormRadioPlugin, PopoverPlugin, ListGroupPlugin, CollapsePlugin, CardPlugin, AlertPlugin, ToastPlugin  } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.component('b-modal', BModal)
Vue.component('b-button', BButton)
Vue.component('b-form', BForm)

library.add(faTooth)
Vue.config.productionTip = false
Vue.use(TabsPlugin)
Vue.use(FormInputPlugin)
Vue.use(FormRadioPlugin)
Vue.use(PopoverPlugin)
Vue.use(ListGroupPlugin)
Vue.use(CollapsePlugin)
Vue.use(CardPlugin)
Vue.use(AlertPlugin)
Vue.use(ToastPlugin)

import VueHtmlToPaper from 'vue-html-to-paper';

const options = {
  name: '_blank',
  specs: [
    'fullscreen=yes',
    'titlebar=yes',
    'scrollbars=yes'
  ],
  styles: [
    'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css',
    'https://unpkg.com/kidlat-css/css/kidlat.css'
  ]
}

Vue.use(VueHtmlToPaper, options);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>',
})