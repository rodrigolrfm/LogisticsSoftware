<template>
  <a-layout style="min-height: 100vh">
    <a-layout-sider theme="light">
      <div>
        <a-image width="100%" src="logos/Andes_express.png" :preview="false"/>
      </div>
      <a-menu
          v-model:selectedKeys="selectedKeys"
          v-model:openKeys="openKeys"
          mode="inline"
      >
        <a-sub-menu key="sub1">
          <template #title>
            <span>
              <home-outlined />
              <span>Módulos</span>
            </span>
          </template>
          <a-menu-item key="1">
            <router-link
                to="/"
            >Dashboard
            </router-link>
          </a-menu-item>
          <a-menu-item key="2">
            <router-link to="/analysis">
              Análisis
            </router-link>
          </a-menu-item>
        </a-sub-menu>
      </a-menu>
    </a-layout-sider>
    <a-layout>
      <a-layout-header>
        <a-card :bordered="false" title="INDICADORES" />
      </a-layout-header>
      <a-layout-content>
        <slot/>
      </a-layout-content>
    </a-layout>
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
      openKeys: ['sub1']
    }
  },
}
</script>

<style>
body {
  font-family: 'Montserrat', sans-serif !important;
}
</style>