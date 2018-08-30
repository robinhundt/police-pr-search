import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

let ax = axios.create({
  baseURL: 'http://localhost:5000/'
})

function initialState () {
  return {
    url: '',
    results: []
  }
}

export default new Vuex.Store({
  state: initialState(),
  mutations: {
    'SET_SEARCH_URL': function (state, url) {
      state.url = url
    },
    'SET_RESULTS': function (state, results) {
      state.results = results
    }
  },
  actions: {
    searchByUrl: async function ({state, commit}) {
      let res = await ax.post('/', {url: state.url})
      commit('SET_RESULTS', res.data)
    }
  }
})
