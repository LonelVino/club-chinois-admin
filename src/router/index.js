import Vue from 'vue'
import Router from 'vue-router'


Vue.use(Router)

/* Layout */
import Layout from '@/layout'

import Login from '../views/login/';
import HelloWorld from '@/components/HelloWorld'


export const constantRoutes = [
  {
    path: '/',
    component: Login,
    redirect: '/login',
    name: 'MainPage',
  },
  { 
    path: '/login', 
    name: 'Login',
    component: Login 
  },
  {
    path: '/helloworld',
    name: 'HelloWorld',
    component: HelloWorld
  }
]

export const asyncRoutes = []


const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()


export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}


export default new Router({
  routes: [
    {
      path: '/',
      component: Login,
      redirect: '/login',
      name: 'MainPage',
    },
    { 
      path: '/login', 
      name: 'Login',
      component: Login 
    },
    {
      path: '/helloworld',
      name: 'HelloWorld',
      component: HelloWorld
    }
  ]
})
