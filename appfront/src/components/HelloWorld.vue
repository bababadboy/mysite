<template>
  <div>
    <p>{{ greeting }} World!</p>
    <ul v-for="item in info"
        v-bind:title="todotiem"
        v-bind:key="item.id">
      <li>{{item.fields.text}}</li>
    </ul>
    <!-- <p>{{info}}</p> -->
  </div>
</template>

<script>

export default {
  name: "todo",
  data() {
    return {
      greeting: "JUST DO IT!",
      items:["itemTest"],
      info: null
    };
  },
  mounted() {
    this.$http
      .get('http://localhost:8000/api/show_todos/')
      .then(response => (this.info = response.data.list))
      .catch(error => console.log(error))
  },
  methods:{
    // goback:function(){
    // console.log('hah');
    // this.$http.get('http://localhost:8000/api/show_todos/') //把url地址换成你的接口地址即可
    //   .then(res => {
    //     //this.request.response = res.data
    //     this.items = res.data.data.item; //把取item的数据赋给 item: []中
    //     console.log(res.data.data.item);
    //     if (res.data.code == '0') {
    //       console.log('haha结束了');
    //     }else{
    //       alert('数据不存在');
    //     }
    //   })
    //   .catch(err => {
    //     alert('请求失败');
    //   })
    // }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
p {
  font-size: 2em;
  text-align: center;
}
</style>
