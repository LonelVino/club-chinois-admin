
import Layout from '@/layout'
const tableRouter = {
    path: '/finance',
    component: Layout,
    redirect: '/finance/finance-items',
    name: 'Finance',
    children: [
        {
          path: 'finance-items',
          component: () => import('@/views/finance/index'),
          name: 'FinanceItems',
          meta: { title: 'Items' }
        },
        {
          path: 'finance-cat',
          component: () => import('@/views/finance/categories'),
          name: 'FinanceCats',
          meta: { title: 'Categories' }
        },
      ]
    }
export default tableRouter
