<template>
  <v-container fill-height>
    <v-flex class="md6 offset-md3">
      <h1 class="text-xs-center mb-5">Police Press Release Search</h1>
      <u-r-l-search/>
    </v-flex>
  </v-container>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
<script>
import SearchForm from '../components/SearchForm'
import URLSearch from '../components/URLSearch'
export default {
  components: {URLSearch, SearchForm}
}
</script>
