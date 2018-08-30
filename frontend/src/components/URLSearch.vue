<template>
    <v-form>
        <v-container>
            <v-layout row>
                <v-text-field
                        label="URL"
                        v-model="url"
                />
                <v-btn @click="search" :loading="loading">search</v-btn>
            </v-layout>
        </v-container>
    </v-form>
</template>

<script>
export default {
  name: 'URLSearch',
  components: {},
  data () {
    return {
      loading: false
    }
  },
  computed: {
    url: {
      get () {
        return this.$store.state.url
      },
      set (val) {
        this.$store.commit('SET_SEARCH_URL', val)
      }
    }
  },
  methods: {
    search () {
      this.loading = true
      this.$store.dispatch('searchByUrl').then(() => {
        this.$router.push({name: 'search'})
      }).finally(() => {
        this.loading = false
      })
    }
  }
}
</script>

<style scoped>

</style>
