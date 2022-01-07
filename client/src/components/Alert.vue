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
      return this.message.toLowerCase().includes('wrong') ? 'danger' : success;
    },
  },
};
</script>
