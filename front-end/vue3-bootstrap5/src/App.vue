<template>
  <div id="app">
    <!-- Use the new component name here -->
    <SignInComponent />
  </div>
 </template>
 
 
 <script>
  // Import the renamed component
  import SignInComponent from './components/SignInComponent.vue';
 
 
  export default {
    name: 'App',
    components: {
      // Register the new component
      SignInComponent
    }
  };
 </script>
 
 
 <style>
 /* Add any global styles if needed */
 </style>
 
 
 