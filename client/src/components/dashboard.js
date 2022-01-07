import VueJwtDecode from 'vue-jwt-decode';
import common from './common.js';
export default {
    name: 'Dashboard',
    data() {
        return {
            username: ''
        };
    },
    methods: {
        getUserDetails() {
            // get token from localstorage
            let token = common.getStorageUserToken();
            try {
                //decode token here and attach to the user object
                let decoded_jwt = VueJwtDecode.decode(token);
                // console.log("DECODED JWT: " + JSON.stringify(decoded_jwt));
                this.username = decoded_jwt.username;
                // console.log("DECODED USERNAME: " + JSON.stringify(this.username));
            } catch (error) {
                this.$router.push("/");
                // return error in production env
                // console.log(error, 'Error decoding token');
            }
        },
        logUserOut() {
            localStorage.removeItem('user');
            this.$router.push('/');
        },
    },
    created() {
        var userLogged = common.checkUserLogged();
        // console.log(JSON.stringify('DASHBOARD - USER LOGGED: ' + userLogged))
        if (!userLogged) {
            this.$router.push('/');
        } else {
            this.getUserDetails();
        }
    },
};