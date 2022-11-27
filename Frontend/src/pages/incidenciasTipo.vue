<template>
    <a-card :style="{  background: '#fff', minHeight: '360px' }">
      <a-breadcrumb >
        <a-breadcrumb-item>
          <home-outlined />
        </a-breadcrumb-item>
        <a-breadcrumb-item>Indicadores</a-breadcrumb-item>
        <a-breadcrumb-item>Dashboard</a-breadcrumb-item>
        <a-breadcrumb-item>Datos</a-breadcrumb-item>
        <p class="dashboard-title">Dashboard</p>
        <a-row type="flex" justify="start" >
          <a-col :span="4">
            <p>Fecha inicio:</p>
            <p>{{fechaInicio}}</p>
          </a-col>
          <a-col :span="4">
            <p>Fecha fin:</p>
            <p>{{fechaFin}}</p>
          </a-col>
          <a-col :span="5">
            <p>Cliente:</p>
            <p>{{clienteTexto}}</p>
          </a-col>
          <a-col :span="4">
            <p>Departamento:</p>
            <p>{{departamentoTexto}}</p>
          </a-col>
        </a-row>
        <a-row type="flex" justify="center" v-if="mostrarGraficosIncidencia">
          <a-col :span="10">
            <p class="donut-chart">Porcentaje de incidencias</p>
            <apexchart
                style="padding-top: 40px"
                width="400"
                
                type="donut"
                :options="optionsDonut"
                :series="seriesDonut"
                @dataPointSelection="mostrarDatosTipoIncidencia"
            ></apexchart>
          </a-col>
          <a-col :span="10">
            <p class="donut-chart">Proveedor</p>
            <span><a-select
              v-model:value="proveedor"
              placeholder="Proveedor"
              style="width: 200px"
              :options="opcionesProveedores"
              @change="cambioProveedor"
            >
            </a-select>
            <a-input disabled :value="porcentajeProveedor" style="width: 5rem;"></a-input></span>
          </a-col>
        </a-row>
      </a-breadcrumb>
    </a-card>
  </template>
  
  <script>
  import { HomeOutlined } from '@ant-design/icons-vue';
  import {getIncidenciasPorTipo, getPorcentajeProveedor, getProveedores} from '../services/index';
  
  export default {
    components: {
      HomeOutlined,
    },
    name: "index",
    data() {
      return {
        cliente: null,
        clienteTexto: '',
        departamento: null,
        departamentoTexto: '',
        fechaInicio: '',
        fechaFin: '',
        proveedor:null,

        opcionesProveedores:[],
        opcionesTipoIncidencia:{},

        mostrarGraficosIncidencia:false,
        porcentajeProveedor:"12%",

        optionsDonut: {
          labels: ['No', 'Sí'],
          plotOptions: {
            donut: {
              labels: {
                show: true,
              }
            }
          }
        },
        seriesDonut: [30, 70],
      }
    },
    methods: {
      mostrarDatosTipoIncidencia(event, chartContext, config){
        console.log(config);
        console.log(config.dataPointIndex);
        sessionStorage.setItem("tipoIncidenciaTexto",this.opcionesTipoIncidencia[config.dataPointIndex].nombre);
        this.$router.push({
          name:"solicitudes",
        });
      },
      async cambioProveedor(value){
        console.log(value);
        let data=await getPorcentajeProveedor(this.fechaInicio,this.fechaFin,this.clienteTexto,this.departamentoTexto,this.proveedor);
        console.log(data);
        /*let data1={
          porcentaje:11,
        }*/
        if(true){//data.data.status=="success"
          this.porcentajeProveedor=data.porcentaje.toString()+"%";
        }
      },
    },
    async created(){
      this.fechaInicio=sessionStorage.fechaInicioIncidencia;
      this.fechaFin=sessionStorage.fechaFinIncidencia;
      this.cliente=sessionStorage.clienteIncidenciaID;
      this.departamento=sessionStorage.departamentoIncidenciaID;
      this.clienteTexto=sessionStorage.clienteIncidenciaTexto;
      this.departamentoTexto=sessionStorage.departamentoIncidenciaTexto;
      try{
        let data=await getIncidenciasPorTipo(this.fechaInicio,this.fechaFin,this.clienteTexto,this.departamentoTexto);
        console.log(data);
        let data2=await getProveedores();
        console.log(data2);
        /*let data={
          listaIncidencias:[
            {
              nombre:"Incidencia Tipo 1",
              cantTipoIncidencia:50,
            },
            {
              nombre:"Incidencia Tipo 2",
              cantTipoIncidencia:121,
            }
          ]
        };
        let data2=[
          {
            id:1,
            proveedor:"Proveedor 1",
          },
          {
            id:2,
            proveedor:"Proveedor 2",
          },
        ];*/
        if(true){//data.status==success
          this.optionsDonut.labels=[];
          this.seriesDonut=[];
          this.opcionesTipoIncidencia=data.listaIncidencias;
          for(let i=0;i<data.listaIncidencias.length;i++){
            this.optionsDonut.labels.push(data.listaIncidencias[i].nombreIncidencia + ": " + data.listaIncidencias[i].cantTipoIncidencia.toString() + " casos.");
            this.seriesDonut.push(data.listaIncidencias[i].cantTipoIncidencia);
          }

          for(let j=0;j<data2.length;j++){
            this.opcionesProveedores.push({
              value:data2[j].id,
              label:data2[j].proveedor,
            });
          }

          setTimeout(()=>{
            this.mostrarGraficosIncidencia=true;
          },500);
        }
      }catch(err){
        console.log(err);
      }
    }
  }
  </script>
  
  <style scoped>
  .dashboard-title {
    padding-top: 30px;
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