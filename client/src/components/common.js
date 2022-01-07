// import axios from 'axios';

var common = {
    getStorageUserToken() {
        // console.log('TOKEN IN STORAGE: ' + JSON.stringify(localStorage.getItem('user')))
        return localStorage.getItem('user');
    },
    setStorageUserToken(user_token) {
        localStorage.setItem("user", user_token);
        this.getStorageUserToken()
    },
    checkUserLogged() {
        var token = this.getStorageUserToken()
            // console.log("TOKEN " + JSON.stringify(token))
            // console.log(token == "undefined")
        if (token == null) {
            // user not logged
            return false
        } else {
            return true
        }
    }
}

export default common