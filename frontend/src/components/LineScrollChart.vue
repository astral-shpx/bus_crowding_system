<script setup>
import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale,
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, LineElement, PointElement, CategoryScale, LinearScale)

const chartData = {
  labels: Array.from({ length: 50 }, (_, i) => `T${i}`),
  datasets: [
    {
      label: 'People Count',
      data: Array.from({ length: 50 }, () => Math.floor(Math.random() * 20)),
      borderColor: '#42A5F5',
      backgroundColor: 'rgba(66,165,245,0.2)',
      fill: true,
      tension: 0.4,
    },
  ],
}

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
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
      text: 'Line Chart (Side Scroll)',
    },
  },
}
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
  width: 100%;
  overflow-x: auto;
}
.chart-scroll {
  width: 1000px; /* todo auto expand based on data */
  min-width: 600px;
  height: 400px;
}
</style>
