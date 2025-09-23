<template>
  <header class="title-bar">
    <img :src="logo" alt="Logo" class="logo" />
    <h1 class="app-name">My Gallery</h1>
  </header>
</template>

<script setup lang="ts">
import logo from '@/assets/logo.png';
</script>

<style scoped>
.title-bar {
  display: flex;
  align-items: center;
  padding: 0.8rem 1.2rem;
  background: #1e1e1e;
  color: #fff;
}
.logo {
  height: 4rem;
  margin-right: 0.8rem;
}
.app-name {
  font-size: 1.4rem;
  margin: 0;
}
</style>
