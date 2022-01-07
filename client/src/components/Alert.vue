<template>
  <div>
    <b-alert
      :variant="alertVariant"
      :show=5
      dismissible
      fade
    >{{ message }}</b-alert>
  </div>
</template>

<script>
export default {
  props: ['message'],
  name: 'Alert',
  computed: {
    alertVariant() {
      var message = this.message.toLowerCase();
      if (message.includes('wrong')) {
        return 'danger';
      } else if (
        message.includes('user already') ||
        message.includes('check format')
      ) {
        return 'warning';
      } else {
        return 'success';
      }
    },
  },
};
</script>
