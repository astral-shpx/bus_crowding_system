// stores/apiStore.js
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useApiStore = defineStore('api', () => {
  const lastPeopleCount = ref(null)

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

  return { lastPeopleCount, fetchLastPeopleCount }
})
