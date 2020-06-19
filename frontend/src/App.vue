<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
import index from "./router/";
export default {
  name: "App",
  components: index,
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
