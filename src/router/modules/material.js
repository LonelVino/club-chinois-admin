
import Layout from '@/layout'
const tableRouter = {
    path: '/material',
    component: Layout,
    redirect: '/material/material-items',
    name: 'Material',
    children: [
        {
          path: 'material-items',
          component: () => import('@/views/material/index'),
          name: 'MaterialItems',
          meta: { title: 'Items' }
        },
        {
          path: 'material-cat',
          component: () => import('@/views/material/categories'),
          name: 'MaterialCats',
          meta: { title: 'Categories' }
        },
      ]
    }
export default tableRouter
