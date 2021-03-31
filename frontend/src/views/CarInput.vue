<template>
  <form @submit.prevent="displayCar">
    <input v-model="brand" type="text" placeholder="Brand..." />
    <input v-model="model" type="text" placeholder="Model..." />
    <input v-model="image" type="text" placeholder="Image..." />
    <button type="submit">Add Car</button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      brand: "",
      model: "",
      image: "",
    };
  },
  methods: {
    async displayCar() {
      let newCar = {
        brand: this.brand,
        model: this.model,
        image: this.image,
      };
      let car = await fetch("/rest/cars", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newCar),
      });

      if (car.ok) {
        car = await car.json();
        console.log(car);
        this.$store.commit("appendCar", car);
      }

      this.$router.push("/");
    },
  },
};
</script>

<style scoped>
form {
  width: 400px;
  margin: auto;
  border: 3px solid grey;
  border-radius: 5px;
  background-color: wheat;
}

input {
  display: block;
  margin: 10px auto;
  width: 380px;
  outline: none;
  border: 1px solid grey;
  border-radius: 5px;
}

button {
  margin-bottom: 10px;
}
</style>