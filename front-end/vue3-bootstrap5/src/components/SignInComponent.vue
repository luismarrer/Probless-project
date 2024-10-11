<template>
    <div class="container-fluid">
      <main class="form-signin m-auto" style="width: 800px;">
        <form> 
          <!-- Sign In Title with Horizontal Lines -->
          <div class="sign-in-title text-white">
            <span>Create Account</span>
          </div>
 

          <div class="row">
            <!-- Left Column: Department and Password -->
            <div class="col-md-6">
              <div class="form-floating mb-3">
                <input type="text" class="form-control" id="floatingDepartment" placeholder="Department">
                <label for="floatingDepartment">Department</label>
              </div>
             
              <div class="form-floating mb-3">
                <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
                <label for="floatingPassword">Provided Password</label>
              </div>
            </div>
           
            <!-- Right Column: Username and Email -->
            <div class="col-md-6">
              <div class="form-floating mb-3">
                <input type="email" class="form-control" id="floatingEmail" placeholder="name@example.com">
                <label for="floatingEmail">Company email</label>
              </div>
             
              <div class="form-floating mb-3">
                <input type="text" class="form-control" id="floatingUsername" placeholder="Username">
                <label for="floatingUsername">Username</label>
              </div>
            </div>
          </div>
           <!-- Role Input Centered Below the Two Columns -->
          <div class="form-floating mb-3 role-centered">
            <input type="text" class="form-control text-centered" id="floatingRole" placeholder="Role">
            <label for="floatingRole">Role</label>
            <div class="link-centered">
            <p><a class="link-opacity-75" href="#">Already have an account?</a></p>
            <div class="btn-centered">
            <button class="btn btn-primary btn-lg w-100 py-2" type="submit">Sign in</button>
            <p class="mt-5 mb-3 text-body-secondary text-center">© 2024</p>
          </div>
          </div>
          </div>
 
 
 
 
        </form>
      </main>
    </div>
  </template>
   <script>
  export default {
    name: 'SignInComponent',
  };
  </script>
   <style scoped>
  /* Add any component-specific styles here */
   .container-fluid {
    height: 100vh;
    display: flex;
    background:gray;
  }
   .btn-primary {
    display: center;
    background-color: white;
    color: black;
  }
   .form-signin {
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
   .role-centered {
    width: 50%;
    margin: 0 auto;
  }
 
 
  .link-centered {
    width: 50%;
    margin: 0 auto;
  }
 
 
  .btn-centered {
    size: 200%;
    width: 50%;
    margin: 0 auto;
  }
   /* Styling for the Sign In title with lines */
  .sign-in-title {
    display: flex;
    align-items: center;
    text-align: center;
    margin-bottom: 20px;
  }
   .sign-in-title::before,
  .sign-in-title::after {
    content: '';
    flex: 1;
    border-bottom: 1px solid white;  /* Line color */
    margin: 0 10px;
  }
   .sign-in-title span {
    font-size: 1.5rem;
    font-weight: bold;
  }
  </style>
 