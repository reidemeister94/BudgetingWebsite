import axios from 'axios';

export default {
    name: 'Register',
    data() {
        return {
            email: "",
            emailBlured: false,
            valid: false,
            submitted: false,
            password: "",
            passwordBlured: false,
            username: "",
            usernameBlured: false,
            phone: "",
            phoneBlured: false
        };
    },
    methods: {
        validate() {
            this.emailBlured = true;
            this.passwordBlured = true;
            this.usernameBlured = true;
            this.phoneBlured = true;
            if (this.validEmail(this.email) && this.validPassword(this.password) && this.validPhone(this.phone) && this.validUsername(this.username)) {
                this.valid = true;
            }
        },

        validEmail(email) {
            var re = /(.+)@(.+){2,}\.(.+){2,}/;
            if (re.test(email.toLowerCase())) {
                return true;
            }
        },

        validPassword(password) {
            if (password.length > 7) {
                return true;
            }
        },

        validUsername(username) {

            if (!/\s/.test(username)) {
                return true;
            }
        },

        validPhone(phone) {
            if (phone.length > 9 && phone.length < 12) { return true; }
        },
        submit() { this.validate(); if (this.valid) { this.submitted = true; } }
    }
};