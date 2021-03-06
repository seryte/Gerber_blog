import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from "../pages/Home";
import Login from "../pages/Login";


Vue.use(VueRouter)


const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
        meta: {
            auth: true
        },
        // component: resolve => require(['../pages/Home.vue'], resolve),
    },
    {
        path: '/login',
        name: 'Login',
        component: Login,
        meta: {
            auth: false
        },
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../pages/About.vue')
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
