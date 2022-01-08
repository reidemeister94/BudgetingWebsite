<template>
  <div
    id="app"
    class='app'
  >
    <div v-if="toBeDisplayed">
      <VueSidebarMenuAkahon
        :menuTitle="menuTitle"
        :menuIcon="menuIcon"
        :menuItems="menu"
        :bgColor="bgColor"
        :menuItemsTextColor="menuItemsTextColor"
        :logoTitleColor="logoTitleColor"
        :iconsColor="iconsColor"
        :menuItemsHoverColor="menuItemsHoverColor"
        class='sidebar'
      />
    </div>
    <router-view v-bind:class="[this.$route.name == 'Home' ? 'my_component_home' : 'my_component']" />
  </div>
</template>

<script>
import VueSidebarMenuAkahon from 'vue-sidebar-menu-akahon';
export default {
  data() {
    return {
      logged: false,
      toBeDisplayed: true,
      // namePage: this.$route.name,
      menuTitle: 'You Need a Budget',
      menuIcon: 'bx-bar-chart-alt-2',
      bgColor: '#eef0f4',
      menuItemsTextColor: '#595f71',
      logoTitleColor: '#222a3f',
      iconsColor: '#a1a7b6',
      menuItemsHoverColor: '#1d253b',
      // menuItemsHoverColor: '#ffffff',
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
  watch: {
    $route(to, from) {
      this.toBeDisplayed = this.checkSideBarDisplay(to.name);
    },
  },
  methods: {
    checkSideBarDisplay(nameCurrentPage) {
      if (nameCurrentPage == 'Home' || nameCurrentPage == 'Register') {
        return false;
      } else {
        return true;
      }
    },
  },
  created() {
    var nameCurrentPage = this.$route.name;
    this.toBeDisplayed = this.checkSideBarDisplay(nameCurrentPage);
  },
};
</script>

<style src="./assets/css/common.css"></style>