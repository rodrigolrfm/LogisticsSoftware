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
       
        <a-card :style="{  background: '#fff', minHeight: '360px' }" v-if="valPantalla">
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
          <p v-if="clienteTexto != ' - '">{{clienteTexto}}</p>
          <a-select
            v-else
            v-model:value="cliente"
            placeholder="Cliente"
            style="width: 200px"
            :options="opcionesClientes"
          >
        </a-select>
        </a-col>
        <a-col :span="4">
          <p>Departamento:</p>
          <p v-if="departamentoTexto!= ' - '">{{departamentoTexto}}</p>
          <a-select
            v-else
            v-model:value="departamento"
            placeholder="Departamento"
            style="width: 200px"
            :options="opcionesDepartamento"
          >
        </a-select>
        </a-col>
        <a-col :span="5" style="margin-left: 2rem;" v-if="!datosLlenos">
          <p style="color:#FFFFFF"> _ </p>
          <a-button style="background-color:#BF0909; color:#FFFFFF;margin-left: 10px;" @click="mostrarGraficos">
            Generar Indicadores
          </a-button>
        </a-col>
      </a-row>
      <a-row type="flex" justify="center" v-if="mostrarGraficosIncidencia">
        <a-col :span="10">
          <p class="donut-chart">Porcentaje de incidencias</p>
          <apexchart
              style="padding-top: 40px"
              width="500"
              type="donut"
              :options="optionsDonut"
              :series="seriesDonut"
              @dataPointSelection="mostrarDatosTipoIncidencia"
          ></apexchart>
        </a-col>
        <a-col>
          <p class="donut-chart">Proveedor</p>
          <span style="margin-left:100px"><a-select
            v-model:value="proveedor"
            placeholder="Proveedor"
            style="width: 200px"
            :options="opcionesProveedores"
            @change="cambioProveedor"
          >
          </a-select>
          <a-input disabled :value="porcentajeProveedor" style="width: 5rem;margin-left: 10px;"></a-input></span>
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
import {getIncidenciasPorTipo, getPorcentajeProveedor, getProveedores} from '../services/index';

export default {
  components: {
    HomeOutlined,
  },
  name: "index",
  data() {
    return {
      cliente: 'Cliente',
      clienteTexto: '',
      departamento: 'Departamento',
      departamentoTexto: '',
      fechaInicio: '',
      fechaFin: '',
      proveedor:null,

      datosLlenos:false,
      
      valPantalla: false,

      opcionesProveedores:[],
      opcionesTipoIncidencia:{},

      opcionesDepartamento:[{
        value:1,
        label:'Departamento'
      }],
      opcionesClientes:[{
        value:1,
        label:'Cliente'
      }],

      mostrarGraficosIncidencia:false,
      porcentajeProveedor:"%",

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
    obtenerNombreProveedorPorID(id){
        for(let i=0;i<this.opcionesProveedores.length;i++){
          if(this.opcionesProveedores[i].value===id){
            return this.opcionesProveedores[i].label;
          }
        }
        return ' - ';
      },
    async mostrarGraficos(){
      let depaTexto=this.obtenerNombreDepartamentoPorID(this.departamento);
      let cliTexto=this.obtenerNombreClientePorID(this.cliente);
      //this.departamentoTexto=this.obtenerNombreDepartamentoPorID(this.departamento);
      //this.clienteTexto=this.obtenerNombreClientePorID(this.cliente);
      sessionStorage.setItem('clienteIncidenciaID',this.cliente);
      sessionStorage.setItem('departamentoIncidenciaID',this.departamento);
      sessionStorage.setItem('clienteIncidenciaTexto',cliTexto);
      sessionStorage.setItem('departamentoIncidenciaTexto',depaTexto);
      let clienteTextoAux='';
      if(cliTexto!=' - '){
          clienteTextoAux=cliTexto;
      }
      let departamentoTextoAux='';
      if(depaTexto!=' - '){
        departamentoTextoAux=depaTexto;
      }
      let data= await getIncidenciasPorTipo(this.fechaInicio,this.fechaFin,clienteTextoAux,departamentoTextoAux);
      //let data=await getIncidenciasPorTipo(this.fechaInicio,this.fechaFin,this.clienteTexto,this.departamentoTexto);
      console.log(data);
      if(true){//data.status==success
        this.optionsDonut.labels=[];
        this.seriesDonut=[];
        this.opcionesTipoIncidencia=data.data.listaIncidencias;
        for(let i=0;i<data.data.listaIncidencias.length;i++){
          this.optionsDonut.labels.push(data.data.listaIncidencias[i].nombre + ": " + data.data.listaIncidencias[i].cant.toString() + " casos.");
          this.seriesDonut.push(data.data.listaIncidencias[i].cant);
        }

        setTimeout(()=>{
          this.mostrarGraficosIncidencia=true;
        },500);
      }
    },
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
      let nombreProveedor=this.obtenerNombreProveedorPorID(this.proveedor);
      let data=await getPorcentajeProveedor(this.fechaInicio,this.fechaFin,this.clienteTexto,this.departamentoTexto,nombreProveedor);
      //let data=await getPorcentajeProveedor(this.fechaInicio,this.fechaFin,this.clienteTexto,this.departamentoTexto,this.proveedor);
      console.log(data);
      /*let data1={
        porcentaje:11,
      }*/
      if(true){//data.data.status=="success"
        this.porcentajeProveedor=(data.data.porcentaje*100).toString()+"%";
      }
    },
  },
  async created(){
    this.fechaInicio=sessionStorage.fechaInicioIncidencia;
    this.fechaFin=sessionStorage.fechaFinIncidencia;
    //this.cliente=sessionStorage.clienteIncidenciaID;
    //this.departamento=sessionStorage.departamentoIncidenciaID;
    this.clienteTexto=sessionStorage.clienteIncidenciaTexto;
    this.departamentoTexto=sessionStorage.departamentoIncidenciaTexto;
    this.opcionesClientes=JSON.parse(sessionStorage.opcionesClientes);
    this.opcionesDepartamento=JSON.parse(sessionStorage.opcionesDepartamentos);
    this.datosLlenos= (this.clienteTexto!= ' - ' && this.departamentoTexto != ' - ') ? true : false;
    //this.cliente=sessionStorage.clienteIncidenciaID;
    //this.departamento=sessionStorage.departamentoIncidenciaID;
    setTimeout(()=>{
      this.valPantalla=true;
    },1000);

    try{
      let data2=await getProveedores();
      console.log(data2);
      if(true){//data2.data.status=="sucess"
        for(let j=0;j<data2.data.length;j++){
          this.opcionesProveedores.push({
            value:data2.data[j].id,
            label:data2.data[j].razonSocial,
          });
        }
      }
      if(this.datosLlenos){
        let data=await getIncidenciasPorTipo(this.fechaInicio,this.fechaFin,this.clienteTexto,this.departamentoTexto);
        console.log(data);
        if(true){//data.status==success
          this.optionsDonut.labels=[];
          this.seriesDonut=[];
          this.opcionesTipoIncidencia=data.data.listaIncidencias;
          for(let i=0;i<data.data.listaIncidencias.length;i++){
            this.optionsDonut.labels.push(data.data.listaIncidencias[i].nombre + ": " + data.data.listaIncidencias[i].cant.toString() + " casos.");
            this.seriesDonut.push(data.data.listaIncidencias[i].cant);
          }

          setTimeout(()=>{
            this.mostrarGraficosIncidencia=true;
          },500);
        }
      }
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
  margin-left: 0px;
  font-size: 24px;
  text-decoration: underline;
}
.bar-chart {
  padding-top: 60px;
  font-weight: 600;
  text-align: center;
  margin-right: 80px;
}
</style>