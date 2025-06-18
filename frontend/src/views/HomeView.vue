<script setup></script>

<template>
  <div class="home">
    <h1>Добре дошли</h1>
    <p>Този демо сайт ви показва данни за броя на пътниците в реално време и за минали дати.</p>
    <RouterLink to="/charts" class="btn">Виж диаграмите</RouterLink>
  </div>
</template>

<style scoped>
.home {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 4rem 2rem;
  text-align: center;
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

p {
  font-size: 1.2rem;
  margin-bottom: 2rem;
  color: #555;
}

.btn {
  background-color: #42a5f5;
  color: white;
  padding: 0.8rem 1.6rem;
  border-radius: 999px;
  text-decoration: none;
  font-weight: bold;
  transition: background-color 0.3s;
}

.btn:hover {
  background-color: #1e88e5;
}
</style>
