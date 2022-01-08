import Vue from 'vue';
import Router from 'vue-router';
import Home from '../components/Home.vue';
import Register from '../components/Register.vue';
import Dashboard from '../components/Dashboard.vue';
import Logout from '../components/Logout.vue';

Vue.use(Router);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [{
            path: '/',
            name: 'Home',
            component: Home,
        },
        {
            path: '/register',
            name: 'Register',
            component: Register,
        },
        {
            path: '/dashboard',
            name: 'Dashboard',
            component: Dashboard,
        },
        {
            path: '/logout',
            name: 'Logout',
            component: Logout,
        },
    ],
});