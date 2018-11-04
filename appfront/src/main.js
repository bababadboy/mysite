// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios' // 导入网络通信库

Vue.prototype.$http = axios // 配置axios,设置别名this.$http
Vue.config.productionTip = false
Vue.config.devtools = true// 浏览器可以打开Vue pannel

// Vue.use(axios)// 使用网络通信库

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
