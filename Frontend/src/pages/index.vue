<template>
  <a-card :style="{  background: '#fff', minHeight: '360px' }">
    <a-breadcrumb >
      <a-breadcrumb-item>
        <home-outlined />
      </a-breadcrumb-item>
      <a-breadcrumb-item>Indicadores</a-breadcrumb-item>
      <a-breadcrumb-item>Dashboard</a-breadcrumb-item>
      <p class="dashboard-title">Dashboard</p>
      <a-row type="flex" justify="start" >
        <a-col :span="4">
          Fecha inicio
          <a-date-picker placeholder="Fecha de inicio" format="DD/MM/YYYY" @change="cambioFechaInicio"/>
        </a-col>
        <a-col :span="4">
          Fecha fin
          <a-date-picker placeholder="Fecha de fin" format="DD/MM/YYYY" @change="cambioFechaFin"/>
        </a-col>
        <a-col :span="5">
          Cliente
          <a-select
              v-model:value="cliente"
              placeholder="Cliente"
              style="width: 200px"
              :options="opcionesClientes"
          >
          </a-select>
        </a-col>
        <a-col :span="4">
          Departamento
          <a-select
              v-model:value="departamento"
              placeholder="Departamento"
              style="width: 200px"
              :options="opcionesDepartamento"
          >
          </a-select>
        </a-col>
        <a-col :span="5" style="margin-left: 2rem;">
          Indicadores
          <a-button style="color:#82868B;" @click="mostrarGraficos">
            Generar Indicadores
          </a-button>
        </a-col>
      </a-row>
      <a-row type="flex" justify="center" v-if="mostrarGrafico">
        <a-col :span="10">
          <p class="donut-chart">Porcentaje de incidencias</p>
          <apexchart
              style="padding-top: 40px"
              width="350"
              type="donut"
              :options="optionsDonut"
              :series="seriesDonut"
              @dataPointSelection="mostrarTipoIncidencia"
          ></apexchart>
        </a-col>
        <a-col :span="14">
          <p class="bar-chart">Cantidad de incidencias</p>
          <apexchart
              style="padding-top: 40px"
              width="550"
              type="bar"
              :options="optionsBar"
              :series="seriesBar"
          ></apexchart>
        </a-col>
      </a-row>
    </a-breadcrumb>
  </a-card>
</template>

<script>
import { HomeOutlined } from '@ant-design/icons-vue';
import { func } from 'vue-types';
import {getCantidadIncidencias, getIncidenciasMensual} from '../services/index';

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
      opcionesDepartamento:[{value:'Depa 1',label:'Depa 1'},{value:'Depa 2',label:'Depa 2'},{value:'Depa 3',label:'Depa 3'}],
      opcionesClientes:[{value:'Cliente 1',label:'Cliente 1'},{value:'Cliente 2',label:'Cliente 2'},{value:'Cliente 3',label:'Cliente 3'}],

      mostrarGrafico:false,

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
      optionsBar: {
        labels: ['Enero', 'Febrero', 'Marzo', 'Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'],
        chart: {
          stacked: false,
          toolbar: {
            show: true
          },
          zoom: {
            enabled: true
          }
        },
        plotOptions: {
          pie: {
            donut: {
              labels: {
                show: true,
              }
            }
          }
        }
      },
      seriesBar: [
        { name: 'Incidencias', data: [44,1,1,1,1,2,3,4,5,6,7,8] },
      ],
    }
  },
  methods: {
    async mostrarGraficos(){
      try{
        let data=await getCantidadIncidencias(this.fechaInicio,this.fechaFin,this.cliente,this.departamento);
        let data1=await getIncidenciasMensual();
        console.log(data);
        console.log(data1);
        /*let data={
          cantidadIncidencias:123,
          CantidadOK:34,
        };
        let data1={
          enero:12,
          febrero:13,
          marzo:53,
          abril:12,
          mayo:5,
          junio:7,
          julio:11,
          agosto:0,
          septiembre:0,
          octubre:12,
          noviembre:0,
          diciembre:10,
        }*/
        if(true){//data.status=="success"
          this.seriesDonut[0]=data.cantidadIncidencias-data.CantidadOK;
          this.seriesDonut[1]=data.CantidadOK;
          this.seriesBar[0].data[0]=data1.enero;
          this.seriesBar[0].data[1]=data1.febrero;
          this.seriesBar[0].data[2]=data1.marzo;
          this.seriesBar[0].data[3]=data1.abril;
          this.seriesBar[0].data[4]=data1.mayo;
          this.seriesBar[0].data[5]=data1.junio;
          this.seriesBar[0].data[6]=data1.julio;
          this.seriesBar[0].data[7]=data1.agosto;
          this.seriesBar[0].data[8]=data1.septiembre;
          this.seriesBar[0].data[9]=data1.octubre;
          this.seriesBar[0].data[10]=data1.noviembre;
          this.seriesBar[0].data[11]=data1.diciembre;
        }else{
          
        }
        this.mostrarGrafico=true;
      }catch(err){
        console.log(err);
      }
    },
    mostrarTipoIncidencia(event, chartContext, config){
      console.log("click donutchart");
      console.log(config);//config.dataPointIndex tiene el index de cual dato se presiono
      console.log(this.cliente);
      sessionStorage.setItem('fechaInicioIncidencia',this.fechaInicio);
      sessionStorage.setItem('fechaFinIncidencia',this.fechaFin);
      sessionStorage.setItem('clienteIncidencia',this.cliente);
      sessionStorage.setItem('departamentoIncidencia',this.departamento);
      this.$router.push({
        name:"incidenciasTipo",
        /*params:{
          fechaInicio:this.fechaInicio,
          fechaFin:this.fechaFin,
          cliente:this.cliente,
          departamento:this.departamento,
        }*/
      });
    },
    cambioFechaInicio(fechaDate, fechaString){
      this.fechaInicio=fechaString;
    },
    cambioFechaFin(fechaDate, fechaString){
      this.fechaFin=fechaString;
      console.log(this.fechaInicio);
      console.log(this.fechaFin);
    },
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