<template>
  <div id="app">
    <VueSidebarMenuAkahon
      v-if="this.$route.name != 'Home'"
      :menuTitle="menuTitle"
      :menuIcon="menuIcon"
      :menuItems="menu"
    />
    <router-view />
  </div>
</template>

<script>
import VueSidebarMenuAkahon from 'vue-sidebar-menu-akahon';
export default {
  data() {
    return {
      logged: false,
      menuTitle: 'You Need a Budget',
      menuIcon: 'bx-money',
      menu: [
        {
          link: '/dashboard',
          name: 'Dashboard',
          tooltip: 'Dashboard',
          icon: 'bx-grid-alt',
        },
        {
          link: '/history',
          name: 'History',
          tooltip: 'History',
          icon: 'bx-transfer',
        },
        {
          link: '/logout',
          name: 'Logout',
          tooltip: 'Logout',
          icon: 'bx-exit',
        },
      ],
    };
  },
  components: { VueSidebarMenuAkahon },
  // created() {
  //   // console.log(this.$route.name);
  //   var userLogged = common.checkUserLogged();
  //   // console.log(JSON.stringify('HOME - USER LOGGED: ' + userLogged));
  //   if (userLogged) {
  //     this.logged = true;
  //   }
  // },
};
</script>

<style>
#app {
  margin-top: 60px;
}
</style>
