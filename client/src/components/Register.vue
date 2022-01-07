<template>
  <div class="container mt-5">
    <div class="row d-flex justify-content-center">
      <div class="col-md-7">
        <div
          class="card px-5 py-4"
          id="form1"
        >
          <div class="form-data">
            <div class="text-center mb-4">
              <h4>Register Now</h4>
            </div>
            <div class="forms-inputs mb-4"> <span>Username</span> <input
                type="text"
                v-model="username"
                v-bind:class="{'form-control':true, 'is-invalid' : !validUsername(username) && usernameBlured}"
                v-on:blur="usernameBlured = true"
              >
              <div class="invalid-feedback">A valid username is required!</div>
            </div>
            <div class="forms-inputs mb-4"> <span>Password</span> <input
                type="password"
                v-model="password"
                v-bind:class="{'form-control':true, 'is-invalid' : !validPassword(password) && passwordBlured}"
                v-on:blur="passwordBlured = true"
              >
              <div class="invalid-feedback">Password must be 4 character!</div>
            </div>
            <div class="mb-3">
              <b-row
                class="mb-3 text-center"
                align-h="center"
              > <button
                  v-on:click.stop.prevent="submit"
                  class="btn btn-dark w-50"
                >Register</button></b-row>
              <b-row
                class="mb-3 text-center"
                align-h="center"
              >
                <alert
                  :message='msg_user_exists'
                  v-if='user_already_exists'
                ></alert>
              </b-row>
              <b-row
                class="mb-3 text-center"
                align-h="center"
              >
                <alert
                  :message='msg_invalid_fields'
                  v-if='invalid_fields'
                ></alert>
              </b-row>
              <b-row
                class="mb-3 text-center"
                align-h="center"
              >
                <alert
                  :message='msg_smth_wrong'
                  v-if='smth_wrong'
                ></alert>
              </b-row>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style src="../assets/css/register.css"></style>
<script src="./register.js"></script>