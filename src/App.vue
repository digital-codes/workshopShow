<!-- src/App.vue -->
<template>
  <div class="app x-full">
    <TitleBar />

    <div v-if="carouselItems.length > 0">

    <Carousel 
      :items="carouselItems"
      v-model:selectedId="selectedId"
    />

    <MainDetail :item="selectedItem" />
    </div>
    <div v-else style="padding: 2rem; text-align: center;">
      Loading items...
    </div>
    <FooterBar />
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import TitleBar from '@/components/TitleBar.vue';
import Carousel from '@/components/Carousel.vue';
import MainDetail from '@/components/MainDetail.vue';
import FooterBar from '@/components/FooterBar.vue';
import { onMounted } from 'vue';

type Item = {
  id: number;
  title: string;
  description: string;
  image: string;
  doc: string;
  author: string;
};

// --- State ----------------------------------------------------
const sampleItems = ref<Item[]>([]);
const selectedId = ref(0); // will be set after load

// Items needed for the carousel (only the fields it uses)
const carouselItems = computed(() =>
  sampleItems.value.map(({ id, title, image }) => ({ id, title, image }))
);

// Resolve the full object for the main detail view
const selectedItem = computed(() =>
  sampleItems.value.find((it) => it.id === selectedId.value)!
);

// load items.json at runtime using the app base URL
onMounted(async () => {
  try {
    const base = (import.meta.env?.BASE_URL || '/').replace(/\/$/, '') + '/';
    const res = await fetch(base + 'data/items.json');
    if (!res.ok) throw new Error(`Failed to fetch items.json: ${res.status}`);
    const data = (await res.json()) as Item[];

    // rewrite image/doc URLs to be absolute (to work with Vite base URL)
    for (const it of data) {
      it.image = base + it.image.replace(/^\//, '');
      it.doc = base + it.doc.replace(/^\//, '');
    }

    sampleItems.value = data;

    // start with first item if available
    if (sampleItems.value.length > 0) {
      const first = sampleItems.value[0];
      if (first) {
        selectedId.value = first.id;
      }
    }
  } catch (err) {
    // keep this minimal — surface to console for debugging
    // in a real app you might show an error UI
    // eslint-disable-next-line no-console
    console.error(err);
  }
});
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