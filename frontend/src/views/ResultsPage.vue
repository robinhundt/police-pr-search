<template>
    <v-container>
        <v-layout row class="justify-center">
            <v-flex class="xs1">
                <v-btn flat :to='{name: "home"}'>Home</v-btn>
            </v-flex>
            <v-flex class="xs11 md6">
                <u-r-l-search/>
            </v-flex>
        </v-layout>
        <v-flex class="xs12 md6 offset-md3">
            <result
                    v-for="pressRelease in results"
                    v-bind="pressRelease"
                    :key="pressRelease.url"
                    class="my-3"
            />
        </v-flex>
    </v-container>
</template>

<script>
import {mapState} from 'vuex'

import URLSearch from '../components/URLSearch'
import Result from '../components/Result'
export default {
  name: 'ResultsPage',
  components: {Result, URLSearch},
  computed: {
    ...mapState([
      'results'
    ])
  }
}
</script>

<style scoped>

</style>
