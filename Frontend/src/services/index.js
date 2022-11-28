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

    if (cliente == ' - ' && departamento == ' - '){
        return axios.post(URL+"/general/incidencias",{
            "fechaInicio":fechaInicio,
            "fechaFin":fechaFin,
        });
    }
    else if (departamento == ' - ' &&  cliente != ' - '){
        return axios.post(URL+"/general/incidencias",{
            "fechaInicio":fechaInicio,
            "fechaFin":fechaFin,
            "cliente":cliente,
        });
    }
    else if (departamento != ' - ' &&  cliente == ' - '){
        return axios.post(URL+"/general/incidencias",{
            "fechaInicio":fechaInicio,
            "fechaFin":fechaFin,
            "departamento":departamento,
        });
    }
    else if (departamento != ' - ' &&  cliente != ' - '){
        return axios.post(URL+"/general/incidencias",{
            "fechaInicio":fechaInicio,
            "fechaFin":fechaFin,
            "cliente":cliente,
            "departamento":departamento,
        });
    }

}

export function getIncidenciasPorTipo(fechaInicio,fechaFin,cliente,departamento){
    console.log("Así se manda al servicio");
    console.log(fechaInicio);
    console.log(fechaFin);
    console.log(cliente);
    console.log(departamento);
    if (cliente == '' && departamento == ''){
        return axios.post(URL+"/general/incidencias/tipoIncidencia",{
            "fechaInicio":fechaInicio,
            "fechaFin":fechaFin,
        });
    }
    if (departamento == '' &&  cliente != ''){
        return axios.post(URL+"/general/incidencias/tipoIncidencia",{
            "fechaInicio":fechaInicio,
            "fechaFin":fechaFin,
            "cliente":cliente,
        });
    }
    if (departamento != '' &&  cliente == ''){
        return axios.post(URL+"/general/incidencias/tipoIncidencia",{
            "fechaInicio":fechaInicio,
            "fechaFin":fechaFin,
            "departamento":departamento,
        });
    }
    if (departamento != '' &&  cliente != ''){
        return axios.post(URL+"/general/incidencias/tipoIncidencia",{
            "fechaInicio":fechaInicio,
            "fechaFin":fechaFin,
            "cliente":cliente,
            "departamento":departamento,
        });
    }
}

export function getIncidenciasMensual(){
    return axios.post(URL+"/general/incidencias/mensual",{

    });
}

export function getPorcentajeProveedor(fechaInicio,fechaFin,cliente,departamento,proveedor){
    console.log(proveedor)
    if (cliente == ' - ' && departamento == ' - '){
        return axios.post(URL+"/general/incidencias/tipoIncidencia/proveedor",{
            "fechaInicio":fechaInicio,
            "fechaFin":fechaFin,
            "proveedor":proveedor,
        });
    }
    else if (departamento == ' - ' &&  cliente != ' - '){
        return axios.post(URL+"/general/incidencias/tipoIncidencia/proveedor",{
            "fechaInicio":fechaInicio,
            "fechaFin":fechaFin,
            "cliente":cliente,
            "proveedor":proveedor,
        });
    }
    else if (departamento != ' - ' &&  cliente == ' - '){
        return axios.post(URL+"/general/incidencias/tipoIncidencia/proveedor",{
            "fechaInicio":fechaInicio,
            "fechaFin":fechaFin,
            "departamento":departamento,
            "proveedor":proveedor,
        });
    }
    else if (departamento != ' - ' &&  cliente != ' - '){
        return axios.post(URL+"/general/incidencias/tipoIncidencia/proveedor",{
            "fechaInicio":fechaInicio,
            "fechaFin":fechaFin,
            "cliente":cliente,
            "departamento":departamento,
            "proveedor":proveedor,
        });
    }
}

export function getListaSolicitud(fechaInicio,fechaFin,tipoIncidencia,cliente,departamento){
    return axios.post(URL+"/general/obtenerListaSolicitud",{
        "fechaInicio":fechaInicio,
        "fechaFin":fechaFin,
        "cliente":cliente,
        "departamento":departamento,
        "tipoIncidencia":tipoIncidencia,
        "numGuia":"",
    });
}

export function getDetalleSolicitud(guia){
    return axios.post(URL+"/general/obtenerSolicitud",{
        "guia":guia,
    });
}

export function getDepartamentos(){
    return axios.post(URL+"/general/departamentos",{

    });
}

export function getClientes(){
    return axios.post(URL+"/general/clientes",{

    });
}

export function getProveedores(){
    return axios.post(URL+"/general/listarProveedores",{

    });
}

export function getLogin(usuario,contrasena){
    return axios.post(URL+"/general/login",{
        "nombreUsuario":usuario,
        "password":contrasena,
    });
}