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
            <p>{{cliente}}</p>
          </a-col>
          <a-col :span="4">
            <p>Departamento:</p>
            <p>{{departamento}}</p>
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
            ></apexchart>
          </a-col>
          <a-col :span="10">
            <p class="donut-chart">Proveedor</p>
            <a-input disabled :value="porcentajeProveedor" style="width: 5rem;"></a-input>
          </a-col>
        </a-row>
      </a-breadcrumb>
    </a-card>
  </template>
  
  <script>
  import { HomeOutlined } from '@ant-design/icons-vue';
  import {getIncidenciasPorTipo, getPorcentajeProveedor} from '../services/index';
  
  export default {
    components: {
      HomeOutlined,
    },
    name: "index",
    data() {
      return {
        cliente: null,
        departamento: null,
        fechaInicio: '',
        fechaFin: '',

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
      
    },
    async created(){
      this.fechaInicio=sessionStorage.fechaInicioIncidencia;
      this.fechaFin=sessionStorage.fechaFinIncidencia;
      this.cliente=sessionStorage.clienteIncidencia;
      this.departamento=sessionStorage.departamentoIncidencia;
      try{
        let data=getIncidenciasPorTipo(this.fechaInicio,this.fechaFin,this.cliente,this.departamento);
        console.log(data)
        let data1=getPorcentajeProveedor(this.fechaInicio,this.fechaFin);
        console.log(data1);
        /*let data={
          listaIncidencias:[
            {
              nombreIncidencia:"Incidencia Tipo 1",
              cantTipoIncidencia:123,
            },
            {
              nombreIncidencia:"Incidencia Tipo 2",
              cantTipoIncidencia:121,
            }
          ]
        };
        let data1={
          porcentaje:16,
        }*/
        if(true){//data.status==success
          this.optionsDonut.labels=[];
          this.seriesDonut=[];
          for(let i=0;i<data.listaIncidencias.length;i++){
            this.optionsDonut.labels.push(data.listaIncidencias[i].nombreIncidencia + ": " + data.listaIncidencias[i].cantTipoIncidencia.toString() + " casos.");
            this.seriesDonut.push(data.listaIncidencias[i].cantTipoIncidencia);
          }
          this.porcentajeProveedor=data1.porcentaje.toString()+"%";
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