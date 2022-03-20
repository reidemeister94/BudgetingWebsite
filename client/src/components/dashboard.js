import VueJwtDecode from 'vue-jwt-decode';
import common from './common.js';
import axios from 'axios';


export default {
    name: 'Dashboard',
    data() {
        return {
            edit: null,
            username: '',
            request_config: '',
            current_balance: 0,
            user_info: {},
            user_categories: [],
            user_previsions: [],
            user_transactions: [],
            transaction_fields: [{ label: "Amount", key: "amount" },
                { label: "Category", key: "category" },
                { label: "Date", key: "transaction_date" },
                { label: "Description", key: "transaction_description" },
                {
                    key: 'actions',
                    label: 'Actions'
                }
            ]
        };
    },
    computed: {
        rows() {
            return this.user_transactions.length
        }
    },
    // watch: {
    //     this.current_amount: this.computeCurrentBalance();
    // },
    methods: {
        onEdit(id) {
            this.edit = this.edit !== id ? id : null;
        },
        onDelete(id) {},
        getUserDashboard() {
            // get token from localstorage
            let token = common.getStorageUserToken();
            try {
                //decode token here and attach to the user object
                let decoded_jwt = VueJwtDecode.decode(token);
                console.log("DECODED JWT: " + JSON.stringify(decoded_jwt));
                this.username = decoded_jwt.sub;
                console.log('USERNAME: ' + JSON.stringify(this.username))
                const path = this.$apiEndpoint + 'dashboard';
                console.log('REQUEST PATH: ' + JSON.stringify(path))
                this.request_config = {
                    headers: { Authorization: `Bearer ${token}` },
                };
                axios.post(path, "", this.request_config).then((res) => {
                        console.log('RESPONSE DASHBOARD CALL');
                        // console.log(JSON.stringify(res.data));
                        // console.log('='.repeat(75));
                        if (res.status == 200 && 'user_history' in res.data) {
                            console.log(JSON.stringify(res.data.user_history));
                            // this.login_data = res.data;
                            this.user_info = res.data.user_history.user_info;
                            this.user_transactions = res.data.user_history.user_transactions;
                            this.user_previsions = res.data.user_history.user_previsions;
                            this.user_categories = res.data.user_history.user_categories;
                            this.current_amount = this.computeCurrentBalance();
                        }
                    })
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.log(error)
                    });
                // console.log("DECODED USERNAME: " + JSON.stringify(this.username));
            } catch (error) {
                console.log(error)
                common.logUserOut()
                this.$router.push("/");
                // return error in production env
                // console.log(error, 'Error decoding token');
            }
        },
        computeCurrentBalance() {
            console.log('INITIAL BALANCE: ' + JSON.stringify(this.user_info.starting_balance))
            this.current_balance = this.user_info.starting_balance
            for (let transaction of this.user_transactions) {
                if (transaction.transaction_type == 0) {
                    this.current_balance -= transaction.amount
                } else {
                    this.current_balance += transaction.amount
                }
            }
            console.log('CURRENT BALANCE: ' + JSON.stringify(this.current_balance))
        }
    },
    created() {
        var userLogged = common.checkUserLogged();
        console.log(JSON.stringify('DASHBOARD - USER LOGGED: ' + userLogged))
        if (!userLogged) {
            this.$router.push('/');
        } else {
            this.getUserDashboard();
        }
    },
};