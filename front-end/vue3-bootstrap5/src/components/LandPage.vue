<template>
    <nav class="navbar navbar-expand-lg navbar-light fixed-top py-3 navbar-shrink" id="mainNav">
        <div class="container-fluid">
            <a class="navbar-brand" href="#page-top">Probless</a>
            <button class="navbar-toggler navbar-toggler-right" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false"
                aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
            <div class="collapse navbar-collapse" id="navbarResponsive">
                <ul class="navbar-nav ms-auto my-2 my-lg-0">
                    <li class="nav-item"><a class="nav-link" href="#about">Home</a></li>
                    <router-link class="nav-link" to="/dashboard">Dashboard</router-link>
                    <li class="nav-item"><a class="nav-link" href="#portfolio">Settings</a></li>
                    <li class="nav-item"><a class="nav-link" href="#contact">.......</a></li>
                    <!-- Add custom classes for both buttons -->
                    <div class="d-flex gap-2">
                        <router-link to="/signin" class="btn btn-danger custom-btn">Sign In</router-link>
                        <router-link to="/login" class="btn btn-danger custom-btn">Log In</router-link>
                    </div>
                </ul>
            </div>
        </div>
    </nav>
</template>

<style>
body {
    background-color: white;
}

/* Custom Button Styles */
.custom-btn {
    width: 70px;
    height: 35px;
    font-size: 0.9rem;
    padding: 5px 10px;
    text-align: center;
}


/* Adjust the gap if needed */
.d-flex.gap-2 {
    gap: 15px; /* Adjust space between buttons */
}
</style>
