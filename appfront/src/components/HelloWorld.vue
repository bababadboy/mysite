<template>
  <p>{{ greeting }} World!</p>
</template>

<script>
export default {
  name: 'todo',
  data () {
    return {
      greeting: 'JUST DO IT!'
    }
  },
  components: {

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
p {
  font-size: 2em;
  text-align: center;
}
</style>
