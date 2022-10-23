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
          <a-date-picker placeholder="Fecha de inicio"/>
        </a-col>
        <a-col :span="4">
          Fecha fin
          <a-date-picker placeholder="Fecha de fin"/>
        </a-col>
        <a-col :span="5">
          Cliente
          <a-select
              v-model:value="client"
              placeholder="Cliente"
              style="width: 200px"
          >
            <a-select-option value="c1">
              Cliente 1
            </a-select-option>
            <a-select-option value="c2">
              Cliente 2
            </a-select-option>
            <a-select-option value="c3">
              Cliente 3
            </a-select-option>
          </a-select>
        </a-col>
        <a-col :span="4">
          Departamento
          <a-select
              v-model:value="department"
              placeholder="Departamento"
              style="width: 200px"
          >
            <a-select-option value="d1">
              Depa 1
            </a-select-option>
            <a-select-option value="d2">
              Depa 2
            </a-select-option>
            <a-select-option value="d3">
              Depa 3
            </a-select-option>
          </a-select>
        </a-col>
      </a-row>
      <!--<a-row type="flex" justify="center">
        <a-col :span="10">
          <p class="pie-chart">Porcentaje de incidencias</p>
          <apexchart
              style="padding-top: 40px"
              width="350"
              type="donut"
              :options="optionsPie"
              :series="seriesPie"
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
      </a-row>-->
    </a-breadcrumb>
  </a-card>
</template>

<script>
import { HomeOutlined } from '@ant-design/icons-vue';

export default {
  components: {
    HomeOutlined,
  },
  name: "index",
  data() {
    return {
      client: null,
      department: null,
      options: ['cliente1', 'cliente2', 'cliente3', ],
      optionsPie: {
        labels: ['No', 'Sí'],
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
      optionsBar: {
        labels: ['Enero', 'Febrero', 'Abril', 'Mayo'],
        chart: {
          stacked: true,
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
      seriesPie: [44, 55],
      seriesBar: [{
        name: 'Tipo 1',
        data: [44, 55, 41, 67]
      }, {
        name: 'Tipo 2',
        data: [13, 23, 20, 8]
      }, {
        name: 'Tipo 3',
        data: [11, 17, 15, 15]
      }, {
        name: 'Tipo 4',
        data: [21, 10, 25, 13]
      }],
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
.pie-chart {
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