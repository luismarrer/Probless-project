// src/router.js
import { createRouter, createWebHistory } from 'vue-router';
import SignInComponent from './components/SignInComponent.vue';
import LandPage from './components/LandPage.vue';
import Dashboard from './components/DashBoard.vue';
import CreateTicket from './components/CreateTicket.vue';
import LogIn from './components/LogIn.vue';

const routes = [
  {
    path: '/',
    component: LandPage,
  },
  {
    path: '/signin',
    component: SignInComponent,
  },
  {
    path: '/login',
    component: LogIn,
  },
  {
    path: '/dashboard',
    component: Dashboard,
  },
  {
    path: '/create-ticket',
    component: CreateTicket,
  }

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;