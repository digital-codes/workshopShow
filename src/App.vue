<!-- src/App.vue -->
<template>
  <div class="app">
    <TitleBar />

    <Carousel
      :items="carouselItems"
      v-model:selectedId="selectedId"
    />

    <MainDetail :item="selectedItem" />

    <FooterBar />
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import TitleBar from '@/components/TitleBar.vue';
import Carousel from '@/components/Carousel.vue';
import MainDetail from '@/components/MainDetail.vue';
import FooterBar from '@/components/FooterBar.vue';
import { items as sampleItems } from '@/data/SampleItems';

// --- State ----------------------------------------------------
const selectedId = ref(sampleItems[0]?.id  || 0); // start with first item

// rewrite image URLs to be absolute (to work with Vite base URL)
for (const it of sampleItems) {
  it.image = (import.meta.env.BASE_URL || '/').replace(/\/$/, '') + '/' + it.image.replace(/^\//, '');
  it.doc = (import.meta.env.BASE_URL || '/').replace(/\/$/, '') + '/' + it.doc.replace(/^\//, '');
}

// Items needed for the carousel (only the fields it uses)
const carouselItems = sampleItems.map(({ id, title, image }) => ({
  id,
  title,
  image
}));

// Resolve the full object for the main detail view
const selectedItem = computed(() =>
  sampleItems.find((it) => it.id === selectedId.value)!
);
</script>

<style>
body {
  margin: 0;
  font-family: system-ui, sans-serif;
  background: #fafafa;
}
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  width: 100%;
  box-sizing: border-box;
}
</style>