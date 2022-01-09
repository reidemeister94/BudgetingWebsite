import axios from 'axios';
import Alert from './Alert.vue';
import common from './common.js';
export default {
    name: 'Home',
    data() {
        return {
            email: '',
            emailBlured: false,
            valid: false,
            submitted: false,
            password: '',
            message: '',
            passwordBlured: false,
            wrong_credentials: false,
            alertvariant: ''
        };
    },
    components: {
        alert: Alert,
    },
    methods: {
        register() {
            this.$router.push('/register');
        },
        login(payload) {
            const path = this.$apiEndpoint + 'login';
            axios
                .post(path, payload)
                .then((res) => {
                    // console.log('RESPONSE LOGIN CALL');
                    // console.log(JSON.stringify(this.login_data));
                    // console.log('='.repeat(75));
                    if (res.status == 200 && 'access_token' in res.data) {
                        // console.log(JSON.stringify(res.status));
                        // this.login_data = res.data;
                        this.access_token = res.data.access_token;
                        // this.request_config = {
                        //     headers: { Authorization: `Bearer ${this.access_token}` },
                        // };
                        common.setStorageUserToken(this.access_token)
                        this.$router.push('/dashboard')
                    }
                    // this.getLoggedStatus();
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    if (error.response.status === 401) {
                        this.request_config = null;
                        this.wrong_credentials = true;
                        this.message = 'Wrong Credentials';
                        this.alertvariant = 'danger';
                        console.clear();
                    }
                });
        },
        validate() {
            this.emailBlured = true;
            this.passwordBlured = true;
            if (this.validEmail(this.email) && this.validPassword(this.password)) {
                this.valid = true;
            } else {
                this.valid = false;
            }
        },
        validEmail(email) {
            return true;
            // var re = /(.+)@(.+){2,}\.(.+){2,}/;
            // if (re.test(email.toLowerCase())) {
            //   return true;
            // }
        },
        validPassword(password) {
            if (password.length > 3) {
                return true;
            }
        },
        submit() {
            this.wrong_credentials = false;
            this.validate();
            if (this.valid) {
                const payload = {
                    username: this.email,
                    password: this.password,
                };
                this.login(payload);
            }
        },
    },
    created() {
        var userLogged = common.checkUserLogged();
        // console.log(JSON.stringify('HOME - USER LOGGED: ' + userLogged))
        if (userLogged) {
            this.$router.push('/dashboard')
        }
    },
};