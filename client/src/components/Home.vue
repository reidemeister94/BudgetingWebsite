<template>
  <div class="container mt-5">
    <div class="row d-flex justify-content-center">
      <div class="col-md-6">
        <div
          class="card px-5 py-5"
          id="form1"
        >
          <div
            class="form-data"
            v-if="!submitted"
          >
            <div class="forms-inputs mb-4"> <span>Email or username</span> <input
                autocomplete="off"
                type="text"
                v-model="email"
                v-bind:class="{'form-control':true,'is-invalid' : !validEmail(email) && emailBlured}"
                v-on:blur="emailBlured = true"
              >
              <div class="invalid-feedback">A valid email is required!</div>
            </div>
            <div class="forms-inputs mb-4"> <span>Password</span> <input
                autocomplete="off"
                type="password"
                v-model="password"
                v-bind:class="{'form-control':true,
								'is-invalid' : !validPassword(password) && passwordBlured}"
                v-on:blur="passwordBlured = true"
              >
              <div class="invalid-feedback">Password must be at least 4 character!</div>
            </div>
            <div class="mb-3"> <button
                v-on:click.stop.prevent="submit"
                class="btn btn-dark w-100"
              >Login</button> </div>
          </div>
          <div
            class="success-data"
            v-else
          >
            <div class="text-center d-flex flex-column">
              <i class='bx bxs-badge-check'></i>
              <span class="text-center fs-1">You have been logged in <br> Successfully</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Home',
  data() {
    return {
      email: '',
      emailBlured: false,
      valid: false,
      submitted: false,
      password: '',
      passwordBlured: false,
    };
  },
  methods: {
    getLoggedStatus() {
      const path = 'http://localhost:4794/';
      axios
        .get(path, this.request_config)
        .then((res) => {
          this.data = res.data.msg;
          console.log(JSON.stringify(this.data));
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    login(payload) {
      const path = 'http://localhost:4794/login';
      axios
        .post(path, payload)
        .then((res) => {
          this.login_data = res.data;
          console.log('RESPONSE LOGIN CALL');
          console.log(JSON.stringify(this.login_data));
          console.log('='.repeat(75));
          if ('access_token' in this.login_data) {
            var token = this.login_data.access_token;
            this.request_config = {
              headers: { Authorization: `Bearer ${token}` },
            };
          } else {
            this.request_config = null;
          }
          this.getLoggedStatus();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    validate() {
      this.emailBlured = true;
      this.passwordBlured = true;
      if (this.validEmail(this.email) && this.validPassword(this.password)) {
        console.log('dai');
        this.valid = true;
      } else {
        console.log('zio cane');
        this.valid = false;
      }
    },
    validEmail(email) {
      return true;
      // var re = /(.+)@(.+){2,}\.(.+){2,}/;
      // if (re.test(email.toLowerCase())) {
      //   return true;
      // }
    },
    validPassword(password) {
      if (password.length > 3) {
        return true;
      }
    },
    submit() {
      this.validate();
      if (this.valid) {
        const payload = {
          username: this.email,
          password: this.password,
        };
        this.login(payload);
      }
    },
  },
  created() {
    this.getLoggedStatus();
  },
};
</script>
