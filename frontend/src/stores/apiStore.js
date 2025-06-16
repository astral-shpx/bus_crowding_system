// stores/apiStore.js
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useApiStore = defineStore('api', () => {
  const peopleCount = ref(null)

  const fetchPeopleCount = async () => {
    try {
      const res = await fetch(`${import.meta.env.VITE_API_BASE_URL}/api/people_count_last_10x10min`)
      if (!res.ok) throw new Error('Failed to fetch')
      const data = await res.json()
      peopleCount.value = data
    } catch (error) {
      peopleCount.value = { status: 'error', message: error.message }
    }
  }

  return { peopleCount, fetchPeopleCount }
})
