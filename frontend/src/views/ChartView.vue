<script setup>
import LineScrollChart from '@/components/LineScrollChart.vue'
import { ref, watch, onMounted, onUnmounted } from 'vue'
import { useApiStore } from '@/stores/apiStore'

const apiStore = useApiStore()

const lastPeopleCountChartData = ref({
  labels: [],
  datasets: [],
})

const chartOptions = ref({
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    y: {
      min: 0,
      max: 100,
    },
    x: {
      ticks: {
        autoSkip: false,
      },
    },
  },
  plugins: {
    legend: {
      position: 'top',
    },
    title: {
      display: true,
      text: 'Брой пътници',
    },
  },
})

watch(
  () => apiStore.lastPeopleCount,
  (newVal) => {
    if (newVal && newVal?.data) {
      const rawData = newVal.data

      const inCounts = rawData.map((d) => d.in_count)
      const outCounts = rawData.map((d) => d.out_count)
      const onboardCounts = rawData.map((d) => d.onboard)

      const minY = Math.min(...inCounts, ...outCounts, ...onboardCounts)
      const maxY = Math.max(...inCounts, ...outCounts, ...onboardCounts)

      lastPeopleCountChartData.value = {
        labels: rawData.map((item) => {
          const date = new Date(item.timestamp)
          const options = { month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' }
          return date.toLocaleString('bg-BG', options)
        }),
        datasets: [
          {
            label: 'Брой влезли',
            data: inCounts,
            borderColor: '#42A5F5',
            backgroundColor: 'rgba(66,165,245,0.2)',
            fill: false,
            tension: 0.4,
          },
          {
            label: 'Брой излезли',
            data: outCounts,
            borderColor: '#FF6384',
            backgroundColor: 'rgba(255,99,132,0.2)',
            fill: false,
            tension: 0.4,
          },
          {
            label: 'Брой вътре',
            data: onboardCounts,
            borderColor: '#FFCE56',
            backgroundColor: 'rgba(255,206,86,0.2)',
            fill: false,
            tension: 0.4,
          },
        ],
      }

      chartOptions.value.scales.y.min = Math.floor(minY - 1)
      chartOptions.value.scales.y.max = Math.ceil(maxY + 1)
    }
  },
  { immediate: true },
)

let intervalId = null

onMounted(() => {
  apiStore.fetchLastPeopleCount()

  intervalId = setInterval(() => {
    apiStore.fetchLastPeopleCount()
  }, 5000)
})

onUnmounted(() => {
  clearInterval(intervalId)
})
</script>

<template>
  <div class="charts">
    <LineScrollChart :chartData="lastPeopleCountChartData" :chartOptions="chartOptions" />
  </div>
</template>

<style scoped>
.charts {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
  margin-top: 2rem;
}
</style>
