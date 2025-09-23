<template>
  <section class="detail">
    <img :src="item.image" alt="" class="big-image" />
    <div class="meta">
      <h2 class="title">{{ item.title }}</h2>
      <p class="author">by {{ item.author }}</p>
      <p class="desc">{{ item.description }}</p>
    </div>
  </section>
</template>

<script setup lang="ts">
import type { Item } from '@/data/SampleItems';
defineProps<{ item: Item }>();  // no const props here!

</script>

<style scoped>
.detail {
    margin-top: 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1.5rem;
    box-sizing: border-box;
    border-radius: 16px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.12);
    background: #fff;
}
.big-image {
  max-width: 100%;
  max-height: 400px;
  object-fit: contain;
  border-radius: 8px;
  margin-bottom: 1rem;
}
.meta {
  text-align: center;
}
.title {
  margin: 0.2rem 0;
  font-size: 1.8rem;
}
.author {
  margin: 0.2rem 0;
  color: #555;
}
.desc {
  margin-top: 0.6rem;
  line-height: 1.4;
}
</style>
