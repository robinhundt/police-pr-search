<template>

  <v-container fluid>
    <v-flex class="md4 offset-md4">
      <h1 class="text-xs-center">Police Press Release Search</h1>
      <search-form/>
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
export default {
  components: {SearchForm}
}
</script>
