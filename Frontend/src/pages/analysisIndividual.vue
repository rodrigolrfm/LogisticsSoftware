<template>
  <a-card :style="{  background: '#fff', minHeight: '360px' }">
    <a-row>
      <a-breadcrumb >
        <a-breadcrumb-item>
          <home-outlined />
        </a-breadcrumb-item>
        <a-breadcrumb-item>Análisis</a-breadcrumb-item>
        <a-breadcrumb-item>Análisis Individual</a-breadcrumb-item>
      </a-breadcrumb>
    </a-row>
    <br><br>
    <a-row justify="left">
      <a-col :span="8">
        <p>Sugerencia</p><br>
        <a-textarea
          solo
          :value="mensaje"
          disabled
          rows="10"
        ></a-textarea>
      </a-col>
      <a-col>
        <a-button style="color:#82868B" @click="mostrarModal">
          Subir archivo
        </a-button>
        <p>{{nombreArchivo}}</p>
      </a-col>
    </a-row>
    <ModalSubirArchivos
      :modalVisible="modalVisible"
      @clickCancelar="clickCancelar"
      @clickAnalizar="clickAnalizar"
    />
  </a-card>
</template>

<script>
  import { HomeOutlined } from '@ant-design/icons-vue';
  import ModalSubirArchivos from '../components/ModalSubirArchivos.vue'
  
  export default {
    components: {
      HomeOutlined,
      ModalSubirArchivos,
    },
    data(){
        return {
            mensaje:"Debe subir un archivo a analizar.",
            nombreArchivo:"No hay ningún archivo subido.",
            modalVisible:false,
        }
    },
    methods: {
      mostrarModal(){
        this.modalVisible=true;
      },
      clickCancelar(){
        this.modalVisible=false;
      },
      clickAnalizar(file){
        console.log(file);
        this.nombreArchivo=file.name;
        this.mensaje=file.response.Sugerencia;
        this.modalVisible=false;
      }
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