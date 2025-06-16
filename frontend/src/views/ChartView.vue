<script setup>
import LineScrollChart from '@/components/LineScrollChart.vue'
import { onMounted, ref } from 'vue'

const apires = ref(null)

onMounted(async () => {
  try {
    const res = await fetch('http://192.168.1.8:5000/api/people_count_last_10x10min')
    if (!res.ok) throw new Error('Failed to fetch')
    const data = await res.json()
    apires.value = data
    console.log(apires.value)
  } catch (error) {
    apires.value = { status: 'error', message: error.message }
  }
})
</script>

<template>
  <div class="about">
    <div>{{ apires }}</div>
    <LineScrollChart />
  </div>
</template>

<style></style>
