<template>
    <nav class="navbar navbar-dark navbar-expand-lg bg-dark shadow">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">
                <img src="@/assets/images/pizza-slice.png"
                    alt="site_logo"
                    class="d-inline-block align-text-top navbar-brand-logo">
            </a>
            <button
                class="navbar-toggler"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#navbarNavAltMarkup"
                aria-controls="navbarNavAltMarkup"
                aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse"
                id="navbarNavAltMarkup">
                <div class="navbar-nav">
                    <router-link class="nav-link"
                        to="/"
                        active-class="active text-primary">
                        Home
                    </router-link>
                    <router-link class="nav-link"
                        to="/about"
                        active-class="active text-primary">
                        About
                    </router-link>
                    <router-link class="nav-link"
                        to="/email-validator"
                        active-class="active text-primary">
                        Email Validator
                    </router-link>
                </div>

                <div class="navbar-nav ms-auto">
                    <a class="btn btn-outline-primary"
                        href="https://github.com/pizza-society/unicornify"
                        target="_blank">
                        <i class="fa-brands fa-github-alt"></i>
                        Github
                    </a>
                </div>
            </div>
        </div>
    </nav>
</template>