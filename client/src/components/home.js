import axios from 'axios';
import Alert from './Alert.vue';
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
        getStorageUserToken() {
            let token = localStorage.getItem('user');
            // console.log('TOKEN IN STORAGE: ' + JSON.stringify(token))
            if (token == null) {
                return "undefined"
            } else {
                return token
            }
        },
        setStorageUserToken(user_token) {
            localStorage.setItem("user", user_token);
        },
        getLoggedStatus() {
            var token = this.getStorageUserToken()
                // console.log("TOKEN " + JSON.stringify(token))
                // console.log(token == "undefined")
            if (token != "undefined") {
                this.request_config = {
                    headers: { Authorization: `Bearer ${token}` },
                };
            }
            const path = 'http://localhost:4794/';
            axios
                .get(path, this.request_config)
                .then((res) => {
                    this.data = res.data.msg;
                    // console.log(JSON.stringify(this.data));
                    if (this.data == 'logged') {
                        // console.log('Setting token to storage:');
                        // console.log(JSON.stringify(this.access_token));
                        // this.setStorageUserToken(this.access_token);
                        // navigate to a protected resource
                        this.$router.push("/dashboard");
                    }

                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });
        },
        login(payload) {
            const path = 'http://localhost:4794/login';
            axios
                .post(path, payload)
                .then((res) => {
                    // console.log('RESPONSE LOGIN CALL');
                    // console.log(JSON.stringify(this.login_data));
                    // console.log('='.repeat(75));
                    if (res.status == 200 && 'access_token' in res.data) {
                        // console.log(JSON.stringify(res.status));
                        this.login_data = res.data;
                        this.access_token = this.login_data.access_token;
                        this.request_config = {
                            headers: { Authorization: `Bearer ${this.access_token}` },
                        };
                        this.setStorageUserToken(this.access_token)
                    }
                    this.getLoggedStatus();
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
        this.getLoggedStatus();
    },
};