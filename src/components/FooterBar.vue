<template>
  <footer class="footer">
    <p>
      © 2025 My Gallery – All rights reserved.
      <a href="#" @click.prevent="showImprint">Imprint</a> |
      <a href="#" @click.prevent="showGDPR">GDPR Notice</a>
    </p>
    <!-- Simple modal placeholders -->
    <div v-if="modal === 'imprint'" class="modal">
      <h3>Imprint</h3>
      <p>Company Name<br/>Address line 1<br/>Address line 2</p>
      <button @click="close">Close</button>
    </div>

    <div v-if="modal === 'gdpr'" class="modal">
      <h3>GDPR Notice</h3>
      <p>
        We process personal data only to the extent necessary for providing the
        service. No data is shared with third parties without explicit consent.
      </p>
      <button @click="close">Close</button>
    </div>
  </footer>
</template>

<script setup lang="ts">
import { ref } from 'vue';
const modal = ref<string | null>(null);

function showImprint() {
  modal.value = 'imprint';
}
function showGDPR() {
  modal.value = 'gdpr';
}
function close() {
  modal.value = null;
}
</script>

<style scoped>
.footer {
  background: #f5f5f5;
  padding: 1rem;
  text-align: center;
  font-size: 0.9rem;
}
.footer a {
  color: #0066cc;
  text-decoration: none;
  margin: 0 0.4rem;
}
.modal {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.45);
  display: flex;
  align-items: center;
  justify-content: center;
}
.modal > div {
  background: #fff;
  padding: 1.5rem;
  border-radius: 6px;
  max-width: 90%;
}
button {
  margin-top: 1rem;
}
</style>
