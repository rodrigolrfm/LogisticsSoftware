<template>
  <a-layout style="min-height: 100vh">
    <a-layout-sider theme="light" >
      <div>
        <a-image width="100%" src="../logos/Andes_express.png" :preview="false"/>
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
        <a-breadcrumb-item>Indicadores</a-breadcrumb-item>
        <a-breadcrumb-item>Dashboard</a-breadcrumb-item>
        <a-breadcrumb-item>Dato</a-breadcrumb-item>
        <a-breadcrumb-item>Solicitudes</a-breadcrumb-item>
        <a-breadcrumb-item>Detalle Solicitud</a-breadcrumb-item>
      </a-breadcrumb>
    </a-row>
    <br>
    <a-row justify="center">
      <a-col>
        <p class="dashboard-title">Detalle Solicitud</p>
      </a-col>
    </a-row>
    <a-row justify="left">
        <a-col>
            <p class="subTitle">Proceso de Transporte:</p>
        </a-col>
    </a-row>
    <a-row justify="left">
        <a-col><p class="label">Nombre/Razón Social: </p></a-col>
        <a-col><a-input disabled :value="cliente" class="textField"></a-input></a-col>
        <a-col><p class="label">Dirección: </p></a-col>
        <a-col><a-input disabled :value="primeraDireccion" class="textField"></a-input></a-col>
    </a-row>
    <a-row justify="left">
        <a-col><p class="label">Guía: </p></a-col>
        <a-col><a-input disabled :value="guia" class="textField"></a-input></a-col>
        <a-col><p class="label">Referencia: </p></a-col>
        <a-col><a-input disabled :value="segundaDireccion" class="textField"></a-input></a-col>
    </a-row>
    <a-row justify="left">
        <a-col><p class="label">Estado guía: </p></a-col>
        <a-col><a-input disabled :value="estado" class="textField"></a-input></a-col>
        <a-col><p class="label">Proveedor: </p></a-col>
        <a-col><a-input disabled :value="proveedor" class="textField"></a-input></a-col>
    </a-row>
    <a-row justify="left">
        <a-col><p class="label">Fecha entrega: </p></a-col>
        <a-col><a-input disabled :value="fechaEntrega" class="textField"></a-input></a-col>
        <a-col><p class="label">Estado Manifiesto: </p></a-col>
        <a-col><a-input disabled :value="estadoManifiesto" class="textField"></a-input></a-col>
    </a-row>
    <a-row justify="left">
        <a-col><p class="label">Cantidad de paquetes: </p></a-col>
        <a-col><a-input disabled :value="numeroPaquete" class="textField"></a-input></a-col>
        <a-col><p class="label">Fecha manifiesto informado: </p></a-col>
        <a-col><a-input disabled :value="fechaManifiestoInformado" class="textField"></a-input></a-col>
    </a-row>
    <a-row justify="left">
        <a-col><p class="label">Departamento: </p></a-col>
        <a-col><a-input disabled :value="departamentoDestino" class="textField"></a-input></a-col>
        <a-col><p class="label">Fecha manifiesto recogido: </p></a-col>
        <a-col><a-input disabled :value="fechaManifiestoRecogido" class="textField"></a-input></a-col>
    </a-row>
    <a-row justify="left">
        <a-col><p class="label">Distrito: </p></a-col>
        <a-col><a-input disabled :value="distritoDestino" class="textField"></a-input></a-col>
        <a-col><p class="label">Fecha manifiesto verificado: </p></a-col>
        <a-col><a-input disabled :value="fechaManifiestoVerificado" class="textField"></a-input></a-col>
    </a-row>
    <a-row justify="left">
        <a-col><p class="label">Provincia: </p></a-col>
        <a-col><a-input disabled :value="provinciaDestino" class="textField"></a-input></a-col>
        <a-col><p class="label">Incidencia de transporte: </p></a-col>
        <a-col><a-input disabled :value="incidenciaManifiesto" class="textField"></a-input></a-col>
    </a-row>
    <a-row justify="left">
        <a-col>
            <p class="subTitle">Proceso de Distribución:</p>
        </a-col>
    </a-row>
    <a-row justify="left">
        <a-col><p class="label">Fecha de reparto: </p></a-col>
        <a-col><a-input disabled :value="fechaReparto" class="textField"></a-input></a-col>
        <a-col><p class="label">Fecha de incidencia de reparto: </p></a-col>
        <a-col><a-input disabled :value="fechaIncidenciaReparto" class="textField"></a-input></a-col>
    </a-row>
    <a-row justify="left">
        <a-col><p class="label">Número de reparto: </p></a-col>
        <a-col><a-input disabled :value="numeroPaquete" class="textField"></a-input></a-col>
        <a-col><p class="label">Incidencia de reparto: </p></a-col>
        <a-col><a-input disabled :value="fechaIncidenciaReparto" class="textField"></a-input></a-col>
    </a-row>
    <a-row justify="left">
        <a-col><p class="label">Fecha de compromiso: </p></a-col>
        <a-col><a-input disabled :value="fechaCompromiso" class="textField"></a-input></a-col>
        <a-button class="btnAnalisisGeneral">
            <router-link
                to="/solicitudes/detalleSolicitud/sugerencia"
                @click="verSugerencia"
            >Ver sugerencia</router-link>
        </a-button>
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
      guia:'',
      estado:'',
      fechaEntrega:'',
      servicio:'',
      numeroPaquete:0,
      contadorVisitas:0,
      distritoDestino:'',
      provinciaDestino:'',
      departamentoDestino:'',
      primeraDireccion:'',
      segundaDireccion:'',
      fechaEmbarque:'',
      fechaSalidaProyectada:'',
      fechaLlegadaProyectada:'',
      fechaLlegadaReal:'',
      via:'',
      cliente:'',
      proveedor:'',
      fechaManifiesto:'',
      estadoManifiesto:'',
      incidenciaManifiesto:'',
      fechaManifiestoRecogido:'',
      fechaManifiestoInformado:'',
      fechaManifiestoVerificado:'',
      fechaReparto:'',
      tipoIncidenciaReparto:'',
      fechaIncidenciaReparto:'',
      fechaCompromiso:'',
      sugerencia:'',
    }
  },
  methods: {
    formatearFechas(fecha){
        if(fecha==null){
            return '';
        }
        return fecha.substring(0,10);
    },
    async obtenerDetalleSolicitud(){
      console.log(this.guia);
      try{
        let data=await getDetalleSolicitud(this.guia);
        console.log(data);
        /*let data={
            guia: "SW093885",
            estado: "Entregada",
            fechaEntrega: "2022-04-21T00:00:00",
            servicio: "PROVINCIA",
            numeroPaquete: 1,
            contadorVisitas: 3,
            distritoDestino: "JAEN",
            provinciaDestino: "JAEN",
            departamentoDestino: "CAJAMARCA",
            primeraDireccion: "AV. VILCHEZ 08 - CASERÍO SANTA TERESITA",
            segundaDireccion: "ENTRAS POR EL 4 DE JUNIO AH 5",
            fechaEmbarque: null,
            fechaSalidaProyectada: "2022-04-08T00:00:00",
            fechaLlegadaProyectada: "2022-04-10T00:00:00",
            fechaLlegadaReal: "2022-04-10T00:00:00",
            via: "TT",
            cliente: "SWISSJUST LATINOAMERICA S.A. SUCURSAL PERU",
            proveedor: "MOVIL BUS S.A.C",
            fechaManifiesto: "2022-04-08T00:00:00",
            estadoManifiesto: "VERIFICADO",
            incidenciaManifiesto: null,
            fechaManifiestoRecogido: "2022-04-11T00:00:00",
            fechaManifiestoInformado: "2022-04-08T00:00:00",
            fechaManifiestoVerificado: "2022-04-11T00:00:00",
            fechaReparto: "2022-04-18T00:00:00",
            tipoIncidenciaReparto: "DIRECCION INCOMPLETA",
            fechaIncidenciaReparto: "2022-04-21T00:00:00",
            fechaCompromiso: "2022-04-20T00:00:00",
            sugerencia: "JUSTIFICAR INCUMPLIMIENTO. EL CLIENTE SWISSJUST LATINOAMERICA S.A. SUCURSAL PERU DEBE REFORZAR LA FUNCIÓN DE REGISTRAR CORRECTAMENTE LA DIRECCION DE DESTINO YA QUE EL INCIDENTE OBSEVADO SE DEBE A DIRECCION INCOMPLETA"
        }*/
        if(true){//data.data.status=="sucess"
            this.guia=data.data.guia;
            this.estado=data.data.estado;
            this.fechaEntrega=this.formatearFechas(data.data.fechaEntrega);
            this.servicio=data.data.servicio;
            this.numeroPaquete=data.data.numeroPaquete;
            this.contadorVisitas=data.data.contadorVisitas;
            this.distritoDestino=data.data.distritoDestino;
            this.provinciaDestino=data.data.provinciaDestino;
            this.departamentoDestino=data.data.departamentoDestino;
            this.primeraDireccion=data.data.primeraDireccion;
            this.segundaDireccion=data.data.segundaDireccion;
            this.fechaEmbarque=this.formatearFechas(data.data.fechaEmbarque);
            this.fechaSalidaProyectada=this.formatearFechas(data.data.fechaSalidaProyectada);
            this.fechaLlegadaReal=this.formatearFechas(data.data.fechaLlegadaReal);
            this.via=data.data.via;
            this.cliente=data.data.cliente;
            this.proveedor=data.data.proveedor;
            this.fechaManifiesto=this.formatearFechas(data.data.fechaManifiesto);
            this.estadoManifiesto=data.data.estadoManifiesto;
            this.incidenciaManifiesto=data.data.incidenciaManifiesto;
            this.fechaManifiestoRecogido=this.formatearFechas(data.data.fechaManifiestoRecogido);
            this.fechaManifiestoInformado=this.formatearFechas(data.data.fechaManifiestoInformado);
            this.fechaManifiestoVerificado=this.formatearFechas(data.data.fechaManifiestoVerificado);
            this.fechaCompromiso=this.formatearFechas(data.data.fechaCompromiso);
            this.fechaReparto=this.formatearFechas(data.data.fechaReparto);
            this.tipoIncidenciaReparto=data.data.tipoIncidenciaReparto;
            this.fechaIncidenciaReparto=this.formatearFechas(data.data.fechaIncidenciaReparto);
            this.sugerencia=data.data.sugerencia;

            sessionStorage.setItem("fechaEntrega",this.fechaEntrega);
            sessionStorage.setItem("sugerencia",this.sugerencia);
        }
      }catch(err){
        console.log(err);
      }
    }
  },
  async created(){
    this.guia=sessionStorage.guiaSolicitud;
    await this.obtenerDetalleSolicitud();
  }
}
</script>

<style scoped>

.btnAnalisisGeneral{
    color:#FFFFFF;
    background-color: #BF0909;
    margin-left: 25px;
}

.label{
    margin-left: 15px;
    width: 10rem;
    height: 2rem;
}
.textField{
    margin-left: 10px;
    width: 20rem;
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