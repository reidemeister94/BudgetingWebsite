<template>
  <div class='container'>
    <ul id="example-1">
      <li
        v-for="user in users"
        :key="user.username"
      >
        {{ user.username }}
      </li>
    </ul>
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
