<template></template>
<script>
import common from './common.js';
export default {
  name: 'Logout',
  data() {
    return {};
  },
  methods: {},
  created() {
    var userLogged = common.checkUserLogged();
    // console.log(JSON.stringify('HOME - USER LOGGED: ' + userLogged))
    if (userLogged) {
      common.logUserOut();
    }
    this.$router.push('/');
  },
};
</script>