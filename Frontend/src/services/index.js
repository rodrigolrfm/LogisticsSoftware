import axios from 'axios';

const URL="http://localhost:8000";
axios.defaults.withCredentials=true;

export function getSugerencia(file){
    console.log(file)
    return axios.post(URL+"/general/uploadfile/",{
        "file":file,
    });
}

export function getCantidadIncidencias(fechaInicio,fechaFin,cliente,departamento){
    console.log("Así se manda al servicio");
    console.log(fechaInicio);
    console.log(fechaFin);
    console.log(cliente);
    console.log(departamento);
    return axios.post(URL+"/incidencias",{
        "fechaInicio":fechaInicio,
        "fechaFin":fechaFin,
        "cliente":cliente,
        "departamento":departamento,
    });
}

export function getIncidenciasPorTipo(fechaInicio,fechaFin,cliente,departamento){
    console.log("Así se manda al servicio");
    console.log(fechaInicio);
    console.log(fechaFin);
    console.log(cliente);
    console.log(departamento);
    return axios.post(URL+"/incidencias/tipoIncidencia",{
        "fechaInicio":fechaInicio,
        "fechaFin":fechaFin,
        "cliente":cliente,
        "departamento":departamento,
    });
}

export function getIncidenciasMensual(){
    return axios.post(URL+"/incidencias/mensual",{

    });
}

export function getPorcentajeProveedor(fechaInicio,fechaFin){
    return axios.post(URL+"/incidencias/tipoIncidencia/proveedor",{
        "fechaInicio":fechaInicio,
        "fechaFin":fechaFin,
    });
}