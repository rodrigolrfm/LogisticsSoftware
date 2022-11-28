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
       
        <a-card :style="{  background: '#fff', minHeight: '360px' }">
    <a-row>
      <a-breadcrumb >
        <a-breadcrumb-item>
          <home-outlined />
        </a-breadcrumb-item>
        <a-breadcrumb-item>Indicadores</a-breadcrumb-item>
        <a-breadcrumb-item>Dashboard</a-breadcrumb-item>
        <a-breadcrumb-item>Dato</a-breadcrumb-item>
        <a-breadcrumb-item>Solicitudes</a-breadcrumb-item>
        <a-breadcrumb-item>Detalle Solicitud</a-breadcrumb-item>
        <a-breadcrumb-item>Sugerencia de la Solicitud</a-breadcrumb-item>
      </a-breadcrumb>
    </a-row>
    <br>
    <a-row justify="center">
      <a-col>
        <p class="dashboard-title">{{tipoIncidencia}}</p>
      </a-col>
    </a-row>
    <a-row justify="left">
        <a-col>
            <p class="subTitle">Detalle de sugerencia:</p>
        </a-col>
    </a-row>
    <a-row justify="left">
        <a-col><p class="label">Departamento: </p></a-col>
        <a-col><p class="label">Fecha de Inicio: </p></a-col>
        <a-col><p class="label">Fecha de Fin: </p></a-col>
    </a-row>
    <a-row justify="left">
        <a-col><p class="labelTitulo">{{departamentoIncidencia}} </p></a-col>
        <a-col><p class="labelTitulo">{{fechaInicioIncidencia}} </p></a-col>
        <a-col><p class="labelTitulo">{{fechaFinIncidencia}} </p></a-col>
    </a-row>
    <a-row>
        <a-col :span="8">
        <p>Descripción</p><br>
            <a-textarea
                solo
                :value="sugerencia"
                disabled
                rows="10"
            ></a-textarea>
        </a-col>
    </a-row>
  </a-card>
        
      </a-layout-content>
    </a-layout>
    </a-layout>
</template>
<script>
import { HomeOutlined } from '@ant-design/icons-vue';
import {getDetalleSolicitud} from '../../../services/index';

export default {
  components: {
    HomeOutlined,
  },
  name: "index",
  data() {
    return{
        tipoIncidencia:'',
        departamentoIncidencia:'',
        fechaInicioIncidencia:'',
        fechaFinIncidencia:'',
    }
  },
  methods: {

  },
  async created(){
    this.tipoIncidencia=sessionStorage.tipoIncidenciaTexto;
    this.departamentoIncidencia=sessionStorage.departamentoIncidenciaTexto;
    this.fechaInicioIncidencia=sessionStorage.fechaInicioIncidencia;
    this.fechaFinIncidencia=sessionStorage.fechaFinIncidencia;
  }
}
</script>

<style scoped>

.btnAnalisisGeneral{
    color:#FFFFFF;
    background-color: #BF0909;
    
}

.label{
    margin-left: 25px;
    width: 10rem;
    font-size: 16px;
    font-weight: bolder;
}
.labelTitulo{
    margin-left: 25px;
    width: 10rem;
}
.textField{
    margin-left: 10px;
    width: 24rem;
    color:black;
}
.dashboard-title {
  font-size: 24px;
  font-weight: 500;
  color: black;
}
.subTitle {
  font-size: 19px;
  text-decoration: underline;
  color: black;
}
.donut-chart {
  padding-top: 60px;
  font-weight: 600;
  text-align: center;
  margin-right: 80px;
}
.bar-chart {
  padding-top: 60px;
  font-weight: 600;
  text-align: center;
  margin-right: 80px;
}
</style>