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
      </a-breadcrumb>
    </a-row>
    <br>
    <a-row justify="left">
      <a-col :span="10">
        <p class="dashboard-title">Búsqueda de Solicitudes</p>
      </a-col>
      <a-col>
        <a-button class="btnAnalisisGeneral">
          <router-link
              to="/solicitudes/analisisGeneral"
          >Análisis General
          </router-link>
        </a-button>
      </a-col>
    </a-row>
    <a-table :dataSource="dataSolicitudes" :columns="columnas">
      <template #bodyCell="{ column, record }">
        <template v-if="column.key==='detalle'">
          <a-button class="btnAnalisisGeneral">
            <router-link
              to="/solicitudes/detalleSolicitud"
              @click="verDetalleSolicitud(record.guia)"
            >Seleccionar</router-link>
          </a-button>
        </template>
      </template>
    </a-table>
  </a-card>
        
      </a-layout-content>
    </a-layout>
    </a-layout>
</template>
<script>
import { HomeOutlined } from '@ant-design/icons-vue';
import {getListaSolicitud} from '../../services/index';

export default {
  components: {
    HomeOutlined,
  },
  name: "index",
  data() {
    return{
      fechaInicio:'',
      fechaFin:'',
      tipoIncidencia:'',
      clienteTexto:'',
      departamentoTexto:'',
      dataSolicitudes: [],

      columnas: [
        {
          title: 'Guía',
          dataIndex: 'guia',
          key: 'guia',
        },
        {
          title: 'Fecha Compromiso',
          dataIndex: 'fechaCompromiso',
          key: 'fechaCompromiso',
        },
        {
          title: 'Fecha de Entrega',
          dataIndex: 'fechaEntrega',
          key: 'fechaEntrega',
        },
        {
          title: 'Nombre Cliente',
          dataIndex: 'cliente',
          key: 'cliente',
        },
        {
          title: 'Cantidad Paquetes',
          dataIndex: 'numeroPaquete',
          key: 'numeroPaquete',
        },
        {
          title: 'Estado',
          dataIndex: 'estado',
          key: 'estado',
        },
        {
          title: 'Detalle',
          key: 'detalle',
        },
      ],
    }
  },
  methods: {
    verDetalleSolicitud(guia){
      console.log(guia);
      sessionStorage.setItem("guiaSolicitud",guia);
    },
    async obtenerListaSolicitud(){
      this.data=[];
      console.log(this.fechaInicio,this.fechaFin,this.tipoIncidencia);
      try{
        let data=await getListaSolicitud(this.fechaInicio,this.fechaFin,this.tipoIncidencia);
        console.log(data);
        /*let data=[
          {
            guia: "SW093885",
            fechaCompromiso: "2022-04-20T00:00:00",
            fechaEntrega: "2022-04-21T00:00:00",
            numeroPaquete: 1,
            cliente: "SWISSJUST LATINOAMERICA S.A. SUCURSAL PERU",
            estado: "Entregada"
          },
          {
            guia: "SW093886",
            fechaCompromiso: "2022-04-20T00:00:00",
            fechaEntrega: "2022-05-21T00:00:00",
            numeroPaquete: 2,
            cliente: "SWISSJUST SUCURSAL BRASIL",
            estado: "En proceso"
          },
        ];*/
        if(true){//data.data.status=="success"
          for(let i=0;i<data.data.length;i++){
            let keyI=(i+1).toString();
            let fechaCompromisoFormato=data.data[i].fechaCompromiso.substring(0,10);
            let fechaEntregaFormato=data.data[i].fechaEntrega.substring(0,10);
            let itemListaSolicitud={
              key:keyI,
              guia:data.data[i].guia,
              fechaCompromiso:fechaCompromisoFormato,
              fechaEntrega:fechaEntregaFormato,
              numeroPaquete:data.data[i].numeroPaquete,
              cliente:data.data[i].cliente,
              estado:data.data[i].estado,
            };
            this.dataSolicitudes.push(itemListaSolicitud);
          }
        }
      }catch(err){
        console.log(err);
      }
    }
  },
  async created(){
    this.fechaInicio=sessionStorage.fechaInicioIncidencia;
    this.fechaFin=sessionStorage.fechaFinIncidencia;
    this.tipoIncidencia=sessionStorage.tipoIncidenciaTexto;
    this.tipoIncidencia=sessionStorage.tipoIncidenciaTexto;
    this.clienteTexto=sessionStorage.clienteIncidenciaTexto;
    await this.obtenerListaSolicitud();
  },
}
</script>

<style scoped>
.btnAnalisisGeneral{
    color:#FFFFFF;
    background-color: #BF0909;
    
}
.dashboard-title {
  font-size: 18px;
  font-weight: 500;
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