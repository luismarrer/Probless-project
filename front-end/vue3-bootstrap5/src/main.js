// src/main.js
import "bootstrap/dist/css/bootstrap.css";
import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Import your router

const app = createApp(App);

app.use(router); // Use the router

app.mount('#app');

import "bootstrap/dist/js/bootstrap.js"; 
