// stores/apiStore.js
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useApiStore = defineStore('api', () => {
  const lastPeopleCount = ref(null)
  const mockPeopleCount = ref(null)

  const fetchLastPeopleCount = async () => {
    try {
      const res = await fetch(`${import.meta.env.VITE_API_BASE_URL}/api/people_count_last_10x5min`)
      if (!res.ok) throw new Error('Failed to fetch')
      const data = await res.json()
      lastPeopleCount.value = data
    } catch (error) {
      lastPeopleCount.value = { status: 'error', message: error.message }
    }
  }

  const fetchMockPeopleCountChartData = async ({ range, start } = {}) => {
    try {
      const params = new URLSearchParams()

      if (range) params.append('range', range)
      if (start) params.append('start', start)

      const queryString = params.toString()
      const url = `${import.meta.env.VITE_API_BASE_URL}/api/get_people_count${queryString ? '?' + queryString : ''}`

      const res = await fetch(url)
      if (!res.ok) throw new Error('Failed to fetch')
      const data = await res.json()
      mockPeopleCount.value = data
    } catch (error) {
      mockPeopleCount.value = { status: 'error', message: error.message }
    }
  }

  return {
    mockPeopleCount,
    lastPeopleCount,
    fetchLastPeopleCount,
    fetchMockPeopleCountChartData,
  }
})
