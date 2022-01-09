<template>
  <div>
    <!-- <b-navbar
      id="navbar"
      toggleable="md"
      type="dark"
      variant="info"
    >
      <b-navbar-brand href="#">
        You are currently viewing the Vue_JWT_App
      </b-navbar-brand>
      <b-navbar-nav class="ml-auto">
        <b-nav-item
          @click="logUserOut"
          active
        >Logout</b-nav-item>
      </b-navbar-nav>
    </b-navbar> -->
    <section>
      <div class="container mt-5">
        <div class="row">
          <div class="col-md-12">
            <ul class="list-group">
              <li class="list-group-item">
                Username : {{ username }}
              </li>
            </ul>
          </div>
          <!-- <div>
            <SampleChart />
          </div> -->
          <!-- <div>
            <pie-chart
              :data="chartData"
              :options="chartOptions"
            ></pie-chart>
          </div> -->
        </div>
      </div>
    </section>
  </div>
</template>


<script src="./dashboard.js"></script>