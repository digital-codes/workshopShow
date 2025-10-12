import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath, URL } from 'node:url';

// https://vite.dev/config/
export default defineConfig({
  base: '/reports/', // Set your subdirectory here
  plugins: [vue()],
  resolve: {
    alias: {
      // This makes both "@/..." and "@/" work
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
})
