<template>
  <a-layout style="min-height: 100vh">
    
    
      <a-layout-content>
        <slot/>
      </a-layout-content>
    
  </a-layout>
</template>

<script>
import { HomeOutlined } from '@ant-design/icons-vue';
export default {
  components: {
    HomeOutlined,
  },
  name: "default",
  data() {
    return {
      selectedKeys: ['1'],
      openKeys: ['sub1'],
      mostrarLayout:true,
    }
  },
  created(){
    
  }
}
</script>

<style>
body {
  font-family: 'Montserrat', sans-serif !important;
}
</style>