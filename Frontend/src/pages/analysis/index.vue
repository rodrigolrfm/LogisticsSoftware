<template>
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