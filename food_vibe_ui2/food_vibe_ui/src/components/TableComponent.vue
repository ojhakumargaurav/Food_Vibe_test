<template>
  <v-card>
    <v-card-title>
      Restaurant Found
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table :headers="headers" :items="restaurant_details" :search="search"></v-data-table>
  </v-card>
</template>

<script>
export default {
  computed: {
    restaurant_details() {
      return this.$store.state.restaurant_details;
    },
  },
  data() {
    return {
      search: "",
      headers: [
        {
          text: "Name",
          align: "start",
          value: "Title",
        },
        { text: "Tags", value: "Tags" },
        { text: "Area", value: "Area" },
        { text: "Category", value: "Category" },
        { text: "Timings", value: "Timings" },
        { text: "Cost For Two", value: "Cost_for_two" },
      ],
    };
  },
  mounted() {
    this.$store.dispatch("get_restaurant_details");
  },
};
</script>