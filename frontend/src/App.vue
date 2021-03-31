<template>
  <main>
    <Navbar />
    <router-view />
  </main>
</template>

<script>
import Navbar from "./components/Navbar.vue";

export default {
  name: "App",
  components: {
    Navbar,
  },

  created(){
    this.$store.dispatch('initCars')
  },
  beforeCreate(){
    console.log("BeforeCreate Hook Ran...")
  },

  mounted(){
    console.log("Mounted hook ran...")
  }
};
</script>

<style scoped>
</style>
