import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import * as constants from './const'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    restaurant_details: []
  },
  mutations: {
    restaurant_mutation(state, payload) {
      state.restaurant_details = payload;
    }
  },
  actions: {
    get_restaurant_details(context) {
      console.log("actions called")
      axios.get(constants.base_url + "list-restaurant/1/40").then(data => {
        console.log(data)
        context.commit("restaurant_mutation", data.data.restaurant_list);
      }).catch(error => {
        console.log("error happened" + error);
      })
    },
    get_restaurant_searched(context, payload) {
      console.log(payload)
      axios.post(constants.base_url + "list-restaurant-search", { "search_string": payload, page_no: 1 }).then(data => {
        console.log(data.data);
        context.commit("restaurant_mutation", data.data.restaurant_list);
      }).catch(error => {
        console.log(error)
      })
    }
  },
  modules: {
  }
})
