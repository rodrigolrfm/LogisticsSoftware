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
          <a-col>
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
          <a-col>
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
    </a-layout-content>
    </a-layout>
    </a-layout>
  </template>
  
  <script>
  import { HomeOutlined } from '@ant-design/icons-vue';
  import {getCantidadIncidencias, getIncidenciasMensual, getDepartamentos, getClientes} from '../../services/index';
  
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
  
        opcionesDepartamento:[],
        opcionesClientes:[],
  
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
        sessionStorage.setItem("aaaa",123);
        try{
          console.log(this.fechaInicio,this.fechaFin,this.cliente,this.departamento);
          this.departamentoTexto=this.obtenerNombreDepartamentoPorID(this.departamento);
          this.clienteTexto=this.obtenerNombreClientePorID(this.cliente);
          console.log(this.departamentoTexto,this.clienteTexto);
          let data=await getCantidadIncidencias(this.fechaInicio,this.fechaFin,this.clienteTexto,this.departamentoTexto);
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
            this.seriesDonut[0]=data.data.cantidadIncidencias-data.data.cantidadOK;
            this.seriesDonut[1]=data.data.cantidadOK;
            this.seriesBar[0].data[0]=data1.data.enero;
            this.seriesBar[0].data[1]=data1.data.febrero;
            this.seriesBar[0].data[2]=data1.data.marzo;
            this.seriesBar[0].data[3]=data1.data.abril;
            this.seriesBar[0].data[4]=data1.data.mayo;
            this.seriesBar[0].data[5]=data1.data.junio;
            this.seriesBar[0].data[6]=data1.data.julio;
            this.seriesBar[0].data[7]=data1.data.agosto;
            this.seriesBar[0].data[8]=data1.data.septiembre;
            this.seriesBar[0].data[9]=data1.data.octubre;
            this.seriesBar[0].data[10]=data1.data.noviembre;
            this.seriesBar[0].data[11]=data1.data.diciembre;
          }else{
            
          }
          this.mostrarGrafico=true;
        }catch(err){
          console.log(err);
        }
      },
      obtenerNombreClientePorID(id){
        for(let i=0;i<this.opcionesClientes.length;i++){
          if(this.opcionesClientes[i].value===id){
            return this.opcionesClientes[i].label;
          }
        }
        return ' - ';
      },
      obtenerNombreDepartamentoPorID(id){
        for(let i=0;i<this.opcionesDepartamento.length;i++){
          if(this.opcionesDepartamento[i].value===id){
            return this.opcionesDepartamento[i].label;
          }
        }
        return ' - ';
      },
      mostrarTipoIncidencia(event, chartContext, config){
        console.log("click donutchart");
        console.log(config);//config.dataPointIndex tiene el index de cual dato se presiono
        console.log(this.cliente);
        sessionStorage.setItem('fechaInicioIncidencia',this.fechaInicio);
        sessionStorage.setItem('fechaFinIncidencia',this.fechaFin);
        sessionStorage.setItem('clienteIncidenciaID',this.cliente);
        sessionStorage.setItem('departamentoIncidenciaID',this.departamento);
        sessionStorage.setItem('clienteIncidenciaTexto',this.clienteTexto);
        sessionStorage.setItem('departamentoIncidenciaTexto',this.departamentoTexto);
        sessionStorage.setItem('opcionesClientes',JSON.stringify(this.opcionesClientes));
        sessionStorage.setItem('opcionesDepartamentos',JSON.stringify(this.opcionesDepartamento));
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
      async obtenerDepartamentos(){
        try{
          let data=await getDepartamentos();
          console.log(data);
          /*let data=[
            {
              id:1,
              nombreDepartamento:"CAJAMARCA",
            },
            {
              id:2,
              nombreDepartamento:"LA LIBERTAD",
            },
          ];*/
          if(true){//data.data.status=="success"
            for(let i=0;i<data.data.length;i++){
              this.opcionesDepartamento.push({
                value:data.data[i].id,
                label:data.data[i].nombreDepartamento,
              });
            }
          }
        }catch(err){
          console.log(err);
        }
      },
      async obtenerClientes(){
        try{
          let data=await getClientes();
          console.log(data)
          /*let data=[
            {
              id:1,
              razonSocial:"SWISSJUST LATINOAMERICA S.A. SUCURSAL PERU",
            },
            {
              id:2,
              razonSocial:"DINET S.A.",
            },
          ];*/
          if(true){//data.data.status=="success"
            for(let i=0;i<data.data.length;i++){
              console.log(data.data)
              console.log(data.data[0].id)
              this.opcionesClientes.push({
                value:data.data[i].id,
                label:data.data[i].razonSocial,
              });
            }
          }
        }catch(err){
          console.log(err);
        }
      },
    },
    async created(){
      /*if(false){
  
      }else{
        this.$router.push('/login');
      }*/
      await this.obtenerDepartamentos();
      await this.obtenerClientes();
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