<template>
  <a-layout style="min-height: 100vh">
    <a-layout-sider theme="light" >
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
                to="/incidentes"
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
        <a-card :bordered="false" title="Andes Express" />
      </a-layout-header>
      <a-layout-content>
        
        <a-card :style="{  background: '#fff', minHeight: '360px' }">
    <a-row>
      <a-breadcrumb >
        <a-breadcrumb-item>
          <home-outlined />
        </a-breadcrumb-item>
        <a-breadcrumb-item>Análisis</a-breadcrumb-item>
      </a-breadcrumb>
    </a-row>
    <br><br>
    <a-row justify="center">
      <a-col :span="10">
        <a-button style="color:#82868B">
          <router-link
              to="/analysisIndividual"
          >Análisis Individual
          </router-link>
        </a-button>
      </a-col>
      <a-col>
        <a-button style="color:#82868B">
          <router-link
              to="/analysisGrupal"
          >Análisis Grupal
          </router-link>
        </a-button>
      </a-col>
    </a-row>
  </a-card>
    
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
  name: "index",
  methods: {
    
  }
}
</script>

<style scoped>
.upload-container {
  background-color: #BABFC7;
  width: 100%;
  margin-top: 30px;
  min-height: 450px;
}
.upload-card ::v-deep(.ant-upload) {
  min-height: 250px;
}
.upload-card ::v-deep(.ant-card-body) {
  padding: 0 50px;
}
.upload-hint {
  color: #BF0909 !important;
  font-family: 'Montserrat', sans-serif;
  font-weight: 300;
  font-size: 14px;
}
.upload-text {
  color: #BF0909 !important;
  font-family: 'Montserrat', sans-serif;
  font-weight: 600;
  font-size: 19px;
  padding-bottom: 15px;
}
.upload-card ::v-deep(.ant-upload-drag-container)  {
  display: table-cell;
  vertical-align: middle;
}
.upload-card {
  margin: 30px 120px;
}
.upload-card ::v-deep(.ant-card-head-title) {
  font-family: 'Montserrat', sans-serif;
  font-weight: 400;
  font-size: 21px;
  margin-top: 30px;
}
</style>