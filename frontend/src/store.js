import { createStore } from 'vuex'


const state = {
  cars: [],
}

const mutations = {
  setCars(state, cars){
    state.cars = cars
  },
  removeCar(state, carToRemove){
    state.cars = state.cars.filter(car => car !== carToRemove)
  },
  appendCar(state, carToAdd){
    state.cars.push(carToAdd)
  }
}

const actions = {
  async initCars(store){
    let cars = await fetch('/rest/cars')
    cars = await cars.json()
    store.commit('setCars', cars)
    console.log(cars)
  },
}




export default createStore({state, mutations, actions})