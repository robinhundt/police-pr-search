import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

function getInstanceBaseUrl () {
  if (process.env.NODE_ENV === 'production') {
    return `${window.location.protocol}//${window.location.host}${window.location.pathname}`
  } else {
    return 'http://localhost:8000/'
  }
}

let ax = axios.create({
  baseURL: getInstanceBaseUrl()
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
      let res = await ax.post('/api', {url: state.url})
      commit('SET_RESULTS', res.data)
    }
  }
})
