<template>
  <main>
    <CarItem v-for="(c, index) of cars" :key="index" :car="c" />
  </main>
</template>

<script>
import CarItem from "../components/CarItem.vue";
export default {
  components: {
    CarItem,
  },

  computed: {
    cars() {
      return this.$store.state.cars;
    },
  },
};
</script>

<style scoped>
</style>