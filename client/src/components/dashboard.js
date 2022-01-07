import VueJwtDecode from 'vue-jwt-decode';
export default {
    name: 'Dashboard',
    data() {
        return {
            user: {},
        };
    },
    methods: {
        getUserDetails() {
            // get token from localstorage
            let token = localStorage.getItem('user');
            try {
                //decode token here and attach to the user object
                let decoded_jwt = VueJwtDecode.decode(token);
                this.username = decoded_jwt.username;
                console.log(JSON.stringify(this.username));
            } catch (error) {
                // return error in production env
                console.log(error, 'Error decoding token');
            }
        },
        logUserOut() {
            localStorage.removeItem('user');
            this.$router.push('/');
        },
    },
    created() {
        this.getUserDetails();
    },
};