<template>
  <div class='container'>
    <b-list-group>
      <b-list-group-item
        v-for="user in users"
        :key="user.username"
      >{{ user.username }}</b-list-group-item>
    </b-list-group>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  name: 'Home',
  data() {
    return {
      users: [],
    };
  },
  methods: {
    getUsers() {
      const path = 'http://localhost:4794/';
      axios
        .get(path)
        .then((res) => {
          this.users = res.data.users;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getUsers();
  },
};
</script>
