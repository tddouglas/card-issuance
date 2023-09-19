import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView
        },
        {
            path: '/newCardOrder',
            name: 'newCardOrder',
            component: () => import('../views/NewOrderView.vue')
        },
        {
            path: '/existingCardOrder',
            name: 'existingCardOrder',
            component: () => import('../views/ExistingOrderView.vue')
        }

    ]
})

export default router
