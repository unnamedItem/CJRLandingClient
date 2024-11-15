import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '@/views/HomeView.vue'
import CollectionView from '@/views/CollectionView.vue'
import EventView from '@/views/EventView.vue'
import Member from '@/views/Member.vue'
import MemberSearch from '@/views/MemberSearch.vue'
import NotFound from '@/views/NotFound.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/collection',
      name: 'collection',
      component: CollectionView
    },
    {
      path: '/event/:id',
      name: 'event',
      component: EventView
    },
    {
      path: '/members/:id',
      name: 'member',
      component: Member,
      props: true
    },
    {
      path: '/members',
      name: 'members',
      component: MemberSearch
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: NotFound
    }
  ]
})

export default router
