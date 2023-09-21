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
            path: '/newCardOrderDetails',
            name: 'newCardOrderDetails',
            component: () => import('../views/NewOrderDetailsView.vue')
        },
        {
            path: '/orderSubmissionResult',
            name: 'orderSubmissionResult',
            component: () => import('../views/OrderSubmissionResultView.vue')
        },
        {
            path: '/existingCardOrder',
            name: 'existingCardOrder',
            component: () => import('../views/ExistingOrderView.vue')
        },
        {
            path: '/requestNewLimits',
            name: 'requestNewLimits',
            component: () => import('../views/RequestNewLimitsView.vue')
        }

    ]
})

export default router
