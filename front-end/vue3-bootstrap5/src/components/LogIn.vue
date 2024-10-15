<template>
    <div class="container-fluid">
        <main class="form-signin m-auto" style="width: 800px;">
            <form>
                <!-- Sign In Title with Horizontal Lines -->
                <div class="sign-in-title">
                    <span>Welcome Back!</span>
                </div>
                <div class="row">
                    <!-- Left Column: Department and Password -->
                    <div class="col-md-6">
                        <div class="form-floating mb-3">
                            <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
                            <label for="floatingPassword">Password</label>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="form-floating mb-3">
                            <input type="email" class="form-control" id="floatingEmail" placeholder="name@example.com">
                            <label for="floatingEmail">E-mail</label>
                        </div>
                    </div>
                </div>
                <div class="form-floating mb-3 role-centered">
                    <div class="btn-centered">
                        <button class="btn btn-danger btn-lg w-100 py-2" type="submit">Log In</button>
                        <p class="mt-5 mb-3 text-body-secondary text-center">© 2024</p>
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
    background: white;
}


.btn-primary {
    display: center;
    background-color: teal;
    color: white;
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


.btn-centered {
    width: 50%;
    margin: 100px;
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
    border-bottom: 1px solid black;
    /* Line color */
    margin: 0 10px;
}


.sign-in-title span {
    font-size: 1.5rem;
    font-weight: bold;
}
</style>