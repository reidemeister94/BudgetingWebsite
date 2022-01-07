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
              <div class="invalid-feedback">Password must be at least 4 characters!</div>
            </div>
            <b-row
              class="mb-2"
              align-h="center"
            >
              <button
                v-on:click.stop.prevent="submit"
                class="btn btn-dark w-50"
              >Login</button>
            </b-row>

            <b-row
              class="mb-3 text-center"
              align-h="center"
            >
              <button
                v-on:click.stop.prevent="register"
                class="btn btn-dark w-50"
              >Register</button>
            </b-row>
          </div>
          <alert
            :message='message'
            v-if='wrong_credentials'
          ></alert>
        </div>
      </div>
    </div>
  </div>
</template>

<style src="../assets/css/home.css"></style>
<script src="./home.js"></script>