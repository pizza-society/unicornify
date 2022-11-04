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
                        to="/qr-code-generator"
                        active-class="active text-primary">
                        QR Generator
                    </router-link>
                    <router-link class="nav-link"
                        to="/email-validator"
                        active-class="active text-primary">
                        Email Validator
                    </router-link>
                    <router-link class="nav-link"
                        to="/24h-to-12h"
                        active-class="active text-primary">
                        24 Hour Time Converter
                    </router-link>
                    <router-link class="nav-link"
                        to="/calendar-link-generator"
                        active-class="active text-primary">
                        Calendar Link Generator
                    </router-link>
                    <router-link class="nav-link"
                        to="/testing"
                        active-class="active text-primary">
                        Testing
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