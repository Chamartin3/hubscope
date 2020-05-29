<template>
<v-card
    class="mx-auto"
    :color="color"
    dark
    min-width="250"
  >
    <v-card-title>
      <v-icon
        large
        left
      >
        {{icon}}
      </v-icon>
      <span class="title font-weight-light"></span>
    </v-card-title>

    <v-card-text class="headline font-weight-bold">
      {{ titulo }}
    </v-card-text>

    <v-card-actions>
      <v-list-item class="grow">

        <v-list-item-content>
          <v-list-item-title> {{ subtitle }} </v-list-item-title>
        </v-list-item-content>

        <v-row
          align="center"
          justify="end"
        >
          <v-icon class="mr-1"> fa-calendar-alt</v-icon>
          <span class="subheading"> sin fecha </span>
          <span class="mr-1">·</span>
          <v-icon> fa-edit </v-icon>
          <span class="subheading mr-2">0</span>
        </v-row>
      </v-list-item>
    </v-card-actions>
  </v-card>
</template>
<script>
export default {
    props: ['color', 'icon', 'titulo', 'subtitle'],
}
</script>