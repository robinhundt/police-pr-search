<template>
    <v-form>
        <v-text-field
                v-model="title"
                label="Title"
        />
        <v-textarea
                v-model="body"
                label="(Partial) body of the article"
        />
        <v-text-field
                v-model="location"
                label="Location"
        />
        <v-layout row>

            <v-menu
                    ref="menuFrom"
                    :close-on-content-click="false"
                    v-model="menuFrom"
                    :nudge-right="40"
                    :return-value.sync="dateFrom"
                    lazy
                    transition="scale-transition"
                    offset-y
                    full-width
                    min-width="290px"
            >
                <v-text-field
                        slot="activator"
                        v-model="dateFrom"
                        label="From Date"
                        prepend-icon="event"
                        readonly
                ></v-text-field>
                <v-date-picker v-model="dateFrom" no-title scrollable>
                    <v-spacer></v-spacer>
                    <v-btn flat color="primary" @click="menuFrom = false">Cancel</v-btn>
                    <v-btn flat color="primary" @click="$refs.menuFrom.save(dateFrom)">OK</v-btn>
                </v-date-picker>
            </v-menu>
            <v-menu
                    ref="menuTo"
                    :close-on-content-click="false"
                    v-model="menuTo"
                    :nudge-right="40"
                    :return-value.sync="dateTo"
                    lazy
                    transition="scale-transition"
                    offset-y
                    full-width
                    min-width="290px"
            >
                <v-text-field
                        slot="activator"
                        v-model="dateTo"
                        label="To Date"
                        prepend-icon="event"
                        readonly
                ></v-text-field>
                <v-date-picker v-model="dateTo" no-title scrollable>
                    <v-spacer></v-spacer>
                    <v-btn flat color="primary" @click="menuTo = false">Cancel</v-btn>
                    <v-btn flat color="primary" @click="$refs.menuTo.save(dateTo)">OK</v-btn>
                </v-date-picker>
            </v-menu>
        </v-layout>
    </v-form>
</template>

<script>
export default {
  name: 'SearchForm',
  data () {
    return {
      menuFrom: false,
      menuTo: false,
      title: '',
      body: '',
      location: '',
      dateFrom: undefined,
      dateTo: undefined
    }
  }
}
</script>

<style scoped>

</style>
