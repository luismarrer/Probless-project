<template>
    <div class="container">
        <main class="form-signin m-auto" style="width: 400px;">
            <form>
            <h1 class="h3 mb-3 fw-normal">Sign In To Get Started</h1>

            <div class="form-floating">
                <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
                <label for="floatingInput">Email address</label>
            </div>
            <div class="form-floating">
                <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
                <label for="floatingPassword">Password</label>
            </div>

            <button class="btn btn-primary w-100 py-2" type="submit">Sign in</button>
            <p class="mt-5 mb-3 text-body-secondary">© 2017–2024</p>
        </form>
    </main>
</div>
</template>

<script>
export default {
    name: 'NewComponent',
};
</script>

<style scoped>
/* Add any component-specific styles here */
</style>