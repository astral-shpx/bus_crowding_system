<script setup>
import { onMounted, ref } from 'vue'

const apires = ref(null)

onMounted(async () => {
  try {
    const res = await fetch('http://192.168.1.8:5000/api/get_people_count')
    if (!res.ok) throw new Error('Failed to fetch')
    const data = await res.json()
    apires.value = data
  } catch (error) {
    apires.value = { status: 'error', message: error.message }
  }
})
</script>

<template>
  <div class="about">
    <h1>This is an about page</h1>
    <div>{{ apires }}</div>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    /* min-height: 100vh; */
    display: flex;
    align-items: center;
  }
}
</style>
