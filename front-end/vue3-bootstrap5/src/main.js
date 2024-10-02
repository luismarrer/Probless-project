import "bootstrap/dist/css/bootstrap.css";
import { createApp, h } from 'vue';
import App from './App.vue';

const app = createApp({
    render: () => h(App),
});

app.mount('#app');

import "bootstrap/dist/js/bootstrap.js";