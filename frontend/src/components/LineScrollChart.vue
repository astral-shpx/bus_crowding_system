<script setup>
import { Line } from 'vue-chartjs'
import { onMounted, ref, watch, onUnmounted } from 'vue'
import { useApiStore } from '@/stores/apiStore'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale,
  Filler,
} from 'chart.js'

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale,
  Filler,
)

const apiStore = useApiStore()

let intervalId = null

const chartData = ref({
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
  () => apiStore.peopleCount,
  (newVal) => {
    if (newVal && newVal.content?.data) {
      const rawData = newVal.content.data

      const inCounts = rawData.map((d) => d.in_count)
      const outCounts = rawData.map((d) => d.out_count)
      const onboardCounts = rawData.map((d) => d.onboard)

      const minY = Math.min(...inCounts, ...outCounts, ...onboardCounts)
      const maxY = Math.max(...inCounts, ...outCounts, ...onboardCounts)

      chartData.value = {
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

onMounted(() => {
  apiStore.fetchPeopleCount()

  intervalId = setInterval(() => {
    apiStore.fetchPeopleCount()
  }, 5000)
})

onUnmounted(() => {
  clearInterval(intervalId)
})
</script>

<template>
  <div class="chart-wrapper">
    <div class="chart-scroll">
      <Line :data="chartData" :options="chartOptions" />
    </div>
  </div>
</template>

<style scoped>
.chart-wrapper {
  width: 1000px;
  max-width: 100%;
  margin: 2rem auto 0;
  overflow-x: auto;
}

.chart-scroll {
  min-width: 600px;
  height: 400px;
  display: flex;
  justify-content: center;
}
</style>
