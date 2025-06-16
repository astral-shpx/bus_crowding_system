<script setup>
import { Line } from 'vue-chartjs'
import { defineProps } from 'vue'
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

const props = defineProps({
  chartData: {
    type: Object,
    required: true,
  },
  chartOptions: {
    type: Object,
    required: true,
  },
})
</script>

<template>
  <div class="chart-wrapper">
    <div class="chart-scroll">
      <Line :data="props.chartData" :options="props.chartOptions" />
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
