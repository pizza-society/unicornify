<template>
    <nav class="navbar navbar-dark navbar-expand-lg bg-dark shadow">
        <div class="container-fluid">
            <a
                class="navbar-brand"
                href="#">
                <img
                    src="@/assets/images/pizza-slice.png"
                    alt="site_logo"
                    class="d-inline-block align-text-top navbar-brand-logo" />
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

            <div
                id="navbarNavAltMarkup"
                class="collapse navbar-collapse">
                <div class="navbar-nav">
                    <router-link
                        class="nav-link"
                        to="/"
                        active-class="active text-primary">
                        Home
                    </router-link>

                    <router-link
                        class="nav-link"
                        to="/about"
                        active-class="active text-primary">
                        About
                    </router-link>

                    <router-link
                        class="nav-link"
                        to="/testing"
                        active-class="active text-primary">
                        Testing
                    </router-link>

                    <!-- TODO: Add support to mobile phone. -->
                    <li 
                        class="nav-item dropdown"
                        @mouseover="toggleDropdownMenu('downloaders')"
                        @mouseleave="toggleDropdownMenu('')">
                        <a
                            class="nav-link dropdown-toggle" 
                            data-bs-toggle="dropdown"
                            role="button"
                            :aria-expanded="currentToggledMenu === 'downloaders' ? 'true' : 'false'"
                            :class="{
                                'show': currentToggledMenu === 'downloaders'
                            }">
                            Downloaders
                        </a>

                        <ul
                            class="dropdown-menu"
                            @mouseover="toggleDropdownMenu('downloaders')"
                            @mouseleave="toggleDropdownMenu('')"
                            :class="{
                                'show': currentToggledMenu === 'downloaders'
                            }">
                            <li>
                                <router-link 
                                    class="dropdown-item"
                                    to="/twitter-downloader"
                                    active-class="active text-primary">
                                    Twitter Downloader
                                </router-link>
                            </li>
                        </ul>
                    </li>

                    <li 
                        class="nav-item dropdown"
                        @mouseover="toggleDropdownMenu('generators')"
                        @mouseleave="toggleDropdownMenu('')">
                        <a 
                            class="nav-link dropdown-toggle" 
                            data-bs-toggle="dropdown"
                            role="button"
                            :aria-expanded="currentToggledMenu === 'generators' ? 'true' : 'false'"
                            :class="{
                                'show': currentToggledMenu === 'generators'
                            }">
                            Generators
                        </a>
                        <ul 
                            @mouseover="toggleDropdownMenu('generators')"
                            @mouseleave="toggleDropdownMenu('')"
                            class="dropdown-menu"
                            :class="{
                                'show': currentToggledMenu === 'generators'
                            }">
                            <li>
                                <router-link
                                    class="dropdown-item"
                                    to="/calendar-link-generator"
                                    active-class="active text-primary">
                                    Calendar Link Generator
                                </router-link>
                                <router-link
                                    class="dropdown-item"
                                    to="/qr-code-generator"
                                    active-class="active text-primary">
                                    QR Generator
                                </router-link>
                            </li>
                        </ul>
                    </li>

                    <li 
                        class="nav-item dropdown"
                        @mouseover="toggleDropdownMenu('validators')"
                        @mouseleave="toggleDropdownMenu('')">
                        <a 
                            class="nav-link dropdown-toggle" 
                            data-bs-toggle="dropdown"
                            role="button"
                            :aria-expanded="currentToggledMenu === 'validators' ? 'true' : 'false'"
                            :class="{
                                'show': currentToggledMenu === 'validators'
                            }">
                            Validators
                        </a>
                        <ul 
                            @mouseover="toggleDropdownMenu('validators')"
                            @mouseleave="toggleDropdownMenu('')"
                            class="dropdown-menu"
                            :class="{
                                'show': currentToggledMenu === 'validators'
                            }">
                            <li>
                                <router-link
                                    class="dropdown-item"
                                    to="/email-validator"
                                    active-class="active text-primary">
                                    Email Validator
                                </router-link>
                            </li>
                        </ul>
                    </li>

                    <li 
                        class="nav-item dropdown"
                        @mouseover="toggleDropdownMenu('others')"
                        @mouseleave="toggleDropdownMenu('')">
                        <a 
                            class="nav-link dropdown-toggle" 
                            data-bs-toggle="dropdown"
                            role="button"
                            :aria-expanded="currentToggledMenu === 'others' ? 'true' : 'false'"
                            :class="{
                                'show': currentToggledMenu === 'others'
                            }">
                            Others
                        </a>
                        <ul 
                            @mouseover="toggleDropdownMenu('others')"
                            @mouseleave="toggleDropdownMenu('')"
                            class="dropdown-menu"
                            :class="{
                                'show': currentToggledMenu === 'others'
                            }">
                            <li>
                                <router-link
                                    class="dropdown-item"
                                    to="/clock-converter"
                                    active-class="active text-primary">
                                    Clock Converter
                                </router-link>
                            </li>
                        </ul>
                    </li>
                </div>

                <div class="navbar-nav ms-auto">
                    <a
                        class="btn btn-outline-primary"
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

<script lang="ts">
import { defineComponent, ref } from 'vue'

export default defineComponent({
    name: 'NavbarMain',
    setup() {

        // Checkers
        const currentToggledMenu = ref<string>('')

        const toggleDropdownMenu = (menuName: string) => {
            return currentToggledMenu.value === menuName ? currentToggledMenu.value = '' : currentToggledMenu.value = menuName
        }

        return {
            toggleDropdownMenu,
            currentToggledMenu,
        }
    }
})
</script>
