<template>
  <div class="home">
    <SearchComponent />
    <TableComponent />
  </div>
</template>

<script>
// @ is an alias to /src
import SearchComponent from "@/components/SearchComponent.vue";
import TableComponent from "@/components/TableComponent.vue";

export default {
  name: "Home",
  components: {
    SearchComponent,
    TableComponent,
  },
};
</script>
