import axios from 'axios';
import common from './common.js';
import Alert from './Alert.vue';

export default {
    name: 'Register',
    data() {
        return {
            valid: false,
            password: "",
            passwordBlured: false,
            username: "",
            usernameBlured: false,
            msg_user_exists: '',
            msg_invalid_fields: '',
            msg_smth_wrong: '',
            user_already_exists: false,
            invalid_fields: false,
            smth_wrong: false
        };
    },
    components: {
        alert: Alert,
    },
    methods: {
        validate() {
            this.passwordBlured = true;
            this.usernameBlured = true;
            if (this.validPassword(this.password) && this.validUsername(this.username)) {
                this.valid = true;
            } else {
                this.valid = false;
            }
        },
        validPassword(password) {
            if (password.length > 3) {
                return true;
            }
        },
        validUsername(username) {
            if (!/\s/.test(username)) {
                return true;
            }
        },
        register(payload) {
            const path = 'http://localhost:4794/register';
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
                    if ('msg' in res.data && res.data.msg.toLowerCase() == 'user already exists') {
                        this.user_already_exists = true;
                        this.msg_user_exists = 'User Already Exists';
                    }
                    // this.getLoggedStatus();
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    this.msg_smth_wrong = 'Something goes wrong';
                    this.smth_wrong = true;
                });
        },
        submit() {
            this.validate();
            if (this.valid) {
                const payload = {
                    username: this.username,
                    password: this.password,
                };
                this.register(payload);
            } else {
                this.invalid_fields = true;
                this.msg_invalid_fields = 'Check format of inserted fields';
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