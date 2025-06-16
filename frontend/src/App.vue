<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header class="header">
    <div class="nav-wrapper">
      <nav class="nav">
        <RouterLink to="/" class="nav-link">Начало</RouterLink>
        <RouterLink to="/charts" class="nav-link">Диаграми</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
.header {
  display: flex;
  justify-content: center;
  margin-top: 2rem;
}

.nav-wrapper {
  background-color: #f0f0f0;
  padding: 1rem 2rem;
  border-radius: 1rem;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

.nav {
  display: flex;
  gap: 1.5rem;
  justify-content: center;
}

.nav-link {
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 9999px; /* fully rounded */
  background-color: #ffffff;
  color: #333;
  font-weight: bold;
  transition: background-color 0.3s;
}

.nav-link:hover {
  background-color: #e0e0e0;
}
</style>
