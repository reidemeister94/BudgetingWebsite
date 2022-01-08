/* eslint-disable indent */
/* eslint-disable eol-last */
import Vue from 'vue';
import App from './App.vue';
import router from './router';
// import '@/assets/css/main.css';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueSidebarMenuAkahon from "vue-sidebar-menu-akahon";
Vue.component('vue-sidebar-menu-akahon', VueSidebarMenuAkahon);
// import VueSidebarMenu from 'vue-sidebar-menu'
// import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'
// Vue.use(VueSidebarMenu)
// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

Vue.config.productionTip = false;


new Vue({
    router,
    render: (h) => h(App),
}).$mount('#app');