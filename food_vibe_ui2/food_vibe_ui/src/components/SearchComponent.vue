<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col cols="12" md="6">
          <v-text-field v-model="SearchString" label="Search String"></v-text-field>
        </v-col>
        <v-btn class="ma-2" color="primary" dark @click="search()">
          Search
          <v-icon dark right>mdi-card-search</v-icon>
        </v-btn>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
export default {
  name: "SearchComponent",
  components: {},
  data: () => ({
    SearchString: "",
  }),
  methods: {
    search() {
      this.$store.dispatch("get_restaurant_searched", this.SearchString);
    },
  },
};
</script>

<style scoped>
</style>