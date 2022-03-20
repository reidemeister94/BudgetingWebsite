<template>
  <b-table
    striped
    hover
    :items="user_transactions"
    :fields="transaction_fields"
  >
    <template v-slot:cell()="{ value, item, field: { key }}">
      <template v-if="edit != item.id">{{ value }}</template>
      <b-form-input
        v-else
        v-model="item[key]"
      />
    </template>

    <template v-slot:cell(actions)="{ item: { id }}">
      <b-dropdown
        variant="primary"
        text="Actions"
      >
        <b-dropdown-item @click="onEdit(id)">{{ edit === id ? 'Save' : 'Edit' }}</b-dropdown-item>
        <b-dropdown-divider></b-dropdown-divider>
        <b-dropdown-item @click="onDelete(id)">Delete</b-dropdown-item>
      </b-dropdown>
    </template>
  </b-table>
</template>


<script src="./dashboard.js"></script>