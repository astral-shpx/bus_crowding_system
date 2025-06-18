<script setup>
import LineScrollChart from '@/components/LineScrollChart.vue'
import { ref, watch, onMounted, onUnmounted } from 'vue'
import { useApiStore } from '@/stores/apiStore'

const apiStore = useApiStore()

const lastPeopleCountChartData = ref({
  labels: [],
  datasets: [],
})

const mockPeopleCountChartData = ref({
  labels: [],
  datasets: [],
})

const chartOptionsLast = ref({
  responsive: true,
  maintainAspectRatio: false,
  locale: 'bg',
  scales: {
    y: {
      title: {
        display: true,
        text: 'Брой пътници',
        font: {
          weight: 'bold',
        },
        color: '#666',
      },
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
      text: 'Последни',
    },
  },
})

const chartOptionsMock = ref({
  responsive: true,
  maintainAspectRatio: false,
  locale: 'bg',
  scales: {
    y: {
      min: 0,
      max: 35,
      title: {
        display: true,
        text: 'Брой пътници',
        font: {
          weight: 'bold',
        },
        color: '#666',
      },
    },
    x: {
      ticks: {
        autoSkip: false,
      },
      type: 'time',
      time: {
        unit: 'minute',
        stepSize: 5,
        minute: 'd MMMM, HH:mm',
        displayFormats: {
          minute: 'd MMMM, HH:mm',
        },
      },
    },
  },
  plugins: {
    legend: {
      position: 'top',
    },
    title: {
      display: true,
      text: 'За 15-ти май 2025',
    },
  },
})

watch(
  () => apiStore.lastPeopleCount,
  (newVal) => {
    // todo extract to func
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

      chartOptionsLast.value.scales.y.min = Math.floor(minY - 1)
      chartOptionsLast.value.scales.y.max = Math.ceil(maxY + 1)

      // edit chartOptions title
    }
  },
  { immediate: true },
)

let intervalId = null

onMounted(async () => {
  await apiStore.fetchMockPeopleCountChartData({
    range: '5h',
    start: '2025-05-15T09:00:00.000000',
  })

  // todo extract to func
  if (apiStore.mockPeopleCount && apiStore.mockPeopleCount?.data) {
    const rawData = apiStore.mockPeopleCount.data

    const inCounts = rawData.map((d) => d.in_count)
    const outCounts = rawData.map((d) => d.out_count)
    const onboardCounts = rawData.map((d) => d.onboard)

    const minY = Math.min(...inCounts, ...outCounts, ...onboardCounts)
    const maxY = Math.max(...inCounts, ...outCounts, ...onboardCounts)

    mockPeopleCountChartData.value = {
      labels: rawData.map((item) => item.timestamp),
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

    chartOptionsMock.value.scales.y.min = Math.floor(minY - 1)
    chartOptionsMock.value.scales.y.max = Math.ceil(maxY + 1)
  }

  await apiStore.fetchLastPeopleCount()

  const inCounts = apiStore.lastPeopleCount.data.map((d) => d.in_count)
  const outCounts = apiStore.lastPeopleCount.data.map((d) => d.out_count)
  const onboardCounts = apiStore.lastPeopleCount.data.map((d) => d.onboard)

  const minY = Math.min(...inCounts, ...outCounts, ...onboardCounts)
  const maxY = Math.max(...inCounts, ...outCounts, ...onboardCounts)
  chartOptionsLast.value.scales.y.min = Math.floor(minY - 1)
  chartOptionsLast.value.scales.y.max = Math.ceil(maxY + 1)

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
    <LineScrollChart :chartData="lastPeopleCountChartData" :chartOptions="chartOptionsLast" />
    <LineScrollChart :chartData="mockPeopleCountChartData" :chartOptions="chartOptionsMock" />
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
