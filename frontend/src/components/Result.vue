<template>
    <v-card>
        <v-card-title class="title">
            {{title}}
        </v-card-title>
        <v-card-body>
            <pre
                    class="pl-5"
                    v-if="!showMore"
            >{{bodyPreview}}<span
                    class="show-span"
                    @click="show"
            > show more</span></pre>
            <pre
                    class="pl-5"
                    v-if="showMore"
            >{{body}}<br/><span
                    class="show-span"
                    @click="hide"
            > show less</span></pre>
        </v-card-body>
    </v-card>
</template>

<script>
export default {
  name: 'Result',
  props: {
    title: {
      type: String,
      required: true
    },
    body: {
      type: String,
      required: true
    }
  },
  data () {
    return {
      showMore: false
    }
  },
  computed: {
    bodyPreview () {
      return this.body.split(' ').slice(0, 30).join(' ') + '...'
    }
  },
  methods: {
    hide () {
      this.showMore = false
    },
    show () {
      this.showMore = true
    }
  }
}
</script>

<style scoped>
    .show-span {
        font-weight: bold;
        cursor: pointer;
    }
</style>
