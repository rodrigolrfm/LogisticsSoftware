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
        <a-space size="9000">
            <a-card style="width: 550%;" :bordered="false" title="Andes Express" />
            <p>:Administ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.________________________________________________</p>
            <a-card style="width: 150%;" :bordered="false" title="Administrador" />
        </a-space>
      </a-layout-header>
      <a-layout-content>
        
        <a-row>
    <div class="upload-container">
      <a-card class="upload-card" :head-style="{textAlign: 'center'}" title="Adjunte su oficio aquí">
        <a-upload-dragger
            name="file"
            class="upload"
            :multiple="true"
            :before-upload="beforeUpload"
            action="http://localhost:8000/general/uploadfileGrupal/"
            @change="handleChange"
        >
          <div class="ant-upload-drag-container">
            <p class="upload-text">Arrastre su archivo aquí o de click para seleccionarlo.</p>
          </div>
        </a-upload-dragger>
        <template #actions>
          <a-row justify="center">
            <a-col>
              <a-button type="primary" @click="realizarAnalisis">Realizar Análisis</a-button>
            </a-col>
          </a-row>
        </template>
      </a-card>
    </div>
  </a-row>
    
    </a-layout-content>
    </a-layout>
    </a-layout>

</template>

<script>
import { HomeOutlined } from '@ant-design/icons-vue';
import {Workbook} from 'exceljs';
import * as fs from 'file-saver';

export default {
  components: {
    HomeOutlined,
  },
  name: "index",
  data(){
    return{
      file:[],
    }
  },
  methods: {
    handleChange({file}) {
      console.log(file);
      const {status} = file;
      console.log(status);
      this.status = status;

      if (status === 'done') {
        this.uploaded = true;

        console.log(file);
        this.file=file;
        setTimeout(()=>{
          console.log(file);
        },2000);
        return this.$message.success(`${file.name} subido correctamente.`);
      }
      if (status === 'error') {
        return this.$message.error(`${file.name} ha fallado al subir.`);
      }
    },
    realizarAnalisis(){
      console.log(this.file);
      this.descargarReporte(this.file.response.Sugerencia);
    },
    descargarReporte(contenido1){
      console.log(contenido1);
      let contenido=JSON.parse(contenido1);
      console.log(contenido); 
      let workbook=new Workbook();
      let worksheet=workbook.addWorksheet("Sugerencias");

      worksheet.addRow(contenido.columns);
      for(let i=1;i<53;i++){
        worksheet.getCell(1,i).fill={
          type:'pattern',
          pattern:'solid',
          fgColor:{argb:'B2FFFF'},
        };
        worksheet.getCell(1,i).border={
          top: {style:'thin'},
          left: {style:'thin'},
          bottom: {style:'thin'},
          right: {style:'thin'}
        };
      }

      for(let i=0;i<contenido.data.length;i++){
        worksheet.addRow(contenido.data[i]);
      }

      workbook.xlsx.writeBuffer().then((data)=>{
        let blob=new Blob([data],{
          type:"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        });
        fs.saveAs(blob,"Reporte.xlsx");
      });
    },
    beforeUpload(file) {
      const isLt1GB = file.size / 1024 < 1048;
      console.log(file.size);
      if (!isLt1GB) {
        this.$message.error('Sólo puedes subir archivos menores a 1GB!');
      }
      return isLt1GB;
    },
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