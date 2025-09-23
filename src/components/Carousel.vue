<!-- Carousel.vue -->
<template>
  <div class="carousel-wrapper">
    <swiper
      :modules="[Navigation, Pagination]"
      :breakpoints="{
        300: { slidesPerView: 2, spaceBetween: 10 },
        640: { slidesPerView: 3, spaceBetween: 16 },
        960: { slidesPerView: 5, spaceBetween: 20 }
      }"
      :navigation="true"
      :initial-slide="items.findIndex((it) => it.id === selectedId)"
      @slideChange="onSlideChange"
      class="carousel"
    >
      <swiper-slide v-for="item in items" :key="item.id">
 <div
        class="card"
        :class="{ active: item.id === selectedId }"
        @click="select(item.id)"
        :style="{backgroundImage: 'url(' + item.image + ')', backgroundSize: 'cover', backgroundPosition: 'center'}"
      >
      <!--<img :src="item.image" alt="" class="thumb" />-->
        <p class="title">{{ item.title }}</p>
      </div>
         </swiper-slide>
    </swiper>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import { Navigation, Pagination } from 'swiper/modules';
import { Swiper, SwiperSlide } from 'swiper/vue';
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';

interface Props {
  items: Array<{
    id: number;
    title: string;
    image: string;
  }>;
  selectedId: number; // currently selected id (v-model)
}
const props = defineProps<Props>();
const emit = defineEmits<{
  (e: 'update:selectedId', id: number): void;
}>();


/* ---------- Local state ---------- */
const localSelected = ref(props.selectedId);

/* Keep local copy in sync when parent changes */
watch(
  () => props.selectedId,
  (newVal) => (localSelected.value = newVal)
);

/* Click on a card → tell parent */
function select(id: number) {
  localSelected.value = id;
  emit('update:selectedId', id);
}

/* Swiper slide change → map activeIndex → item ID */
function onSlideChange(swiper: any) {
  // `activeIndex` is the index of the *currently centered* slide
  const idx = swiper.activeIndex; // 0‑based
  const id = props.items[idx]?.id;
  if (id !== undefined) select(id);
}
</script>

<style scoped>
.carousel {
  padding: 1rem 0;
  --swiper-navigation-size: 2rem;
  --swiper-navigation-top-offset: 7rem;
  --swiper-navigation-slides-offset: 1rem;
}
.card {
  cursor: pointer;
  text-align: center;
  border-radius: 6px;
  overflow: hidden;
  transition: transform 0.2s, box-shadow 0.2s;
}
.card.active {
  transform: scale(1.05);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}
.thumb {
  width: 100%;
  height: 6rem;
  object-fit: cover;
}
.title {
  margin: 0.4rem 0;
  font-weight: 500;
  background: rgba(255, 255, 255, 0.5);
  line-height: 200%;
  backdrop-filter: blur(5px);
}
/* Carousel.vue scoped style */
.carousel-wrapper {
  width: 100%;                 /* fill the parent */
  max-width: 1200px;            /* or any breakpoint you like */
  margin: 0 auto;              /* centre horizontally */
  overflow: hidden;            /* hide any stray overflow */
  padding: 0 1rem;             /* optional side padding */
  box-sizing: border-box;
  height: 8rem
}

</style>

