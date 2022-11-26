from config.db import conn, SECRET
from models.Solicitud import solicitud as solicitudModel
from models.Solicitud import solicitud as solicitudModelSelect
from schemas.SolicitudSchema import Solicitud
from schemas.SolicitudSchema import SolicitudUnica
from schemas.SolicitudSchema import ListarCantidadIncidenciasIn
from schemas.SolicitudSchema import ListarCantidadIncidenciasOut
from schemas.SolicitudSchema import ListarIncidenciasPorTipoIn
from schemas.SolicitudSchema import IncidenciaPorTipoOut, ListarIncidenciasPorTipoOut
from schemas.SolicitudSchema import ListarIncidenciasProveedorIn
from schemas.SolicitudSchema import ListarIncidenciasProveedorOut
from schemas.SolicitudSchema import IncidenciaMensualOut
from schemas.SolicitudSchema import SolicitudUnicaRespuesta
from models.Distrito import distrito as distritoModel
from models.Provincia import provincia as provinciaModel
from models.Departamento import departamento as departamentoModel
from models.Cliente import cliente as clienteModel
from models.Proveedor import proveedor as proveedorModel
from utils.queries_sql import QUERY_LISTAR_CANTIDAD_INCIDENCIAS,QUERY_LISTAR_CANTIDAD_INCIDENCIAS_POR_TIPO

from fastapi import Response
from sqlalchemy import null, select
from starlette.status import HTTP_200_OK
from cryptography.fernet import Fernet
from hashlib import pbkdf2_hmac
import datetime



def registrarSolicitudModule(solicitud:Solicitud):
    nuevoSolicitud = solicitud.dict()
    resultado = conn.execute(solicitudModel.insert().values(nuevoSolicitud))
    return resultado.lastrowid


def obtenerSolicitud(solicitud:SolicitudUnica):
    nuevoSolicitud = solicitud.dict()
    solicitud = conn.execute(solicitudModelSelect.select().where(solicitudModelSelect.c.guia == str(nuevoSolicitud['guia']))).fetchone()
    guia = solicitud['guia']
    estado = solicitud['estado']
    fechaEntrega = solicitud['fechaEntrega']
    servicio = solicitud['servicio']
    numeroPaquete = solicitud['numeroPaquete']
    contadorVisitas = solicitud['contadorVisitas']
    primeraDireccion = solicitud['primeraDireccion']
    segundaDireccion = solicitud['segundaDireccion']
    fechaEmbarque = solicitud['fechaEmbarque']
    fechaSalidaProyectada  = solicitud['fechaSalidaProyectada']
    fechaLlegadaProyectada = solicitud['fechaLlegadaProyectada']
    fechaLlegadaReal = solicitud['fechaLlegadaReal']
    via = solicitud['via']
    fechaManifiesto = solicitud['fechaManifiesto']
    estadoManifiesto = solicitud['estadoManifiesto']
    incidenciaManifiesto = solicitud['incidenciaManifiesto']
    fechaManifiestoRecogido = solicitud['fechaManifiestoRecogido']
    fechaManifiestoInformado = solicitud['fechaManifiestoInformado']
    fechaManifiestoVerificado = solicitud['fechaManifiestoVerificado']
    fechaReparto = solicitud['fechaReparto']
    tipoIncidenciaReparto = solicitud['tipoIncidenciaReparto']
    fechaIncidenciaReparto = solicitud['fechaIncidenciaReparto']
    fechaCompromiso = solicitud['fechaCompromiso']
    sugerencia = solicitud['sugerencia']
    
    idDistritoDestino = int(solicitud['idDistritoDestino'])
    idProveedor = int(solicitud['idProveedor'])
    idCliente = int(solicitud['idCliente'])
    
    distritoRes = conn.execute(distritoModel.select().where(distritoModel.c.id == idDistritoDestino)).fetchone()
    idProvinciaDis = int(distritoRes['idProvincia'])
    provinciaRes = conn.execute(provinciaModel.select().where(provinciaModel.c.id == idProvinciaDis)).fetchone()
    idDepartamentoProv = int(provinciaRes['idDepartamento'])
    departamentoRes = conn.execute(departamentoModel.select().where(departamentoModel.c.id == idDepartamentoProv)).fetchone()

    distritoDestino = str(distritoRes['nombreDistrito'])
    provinciaDestino = str(provinciaRes['nombreProvincia'])
    departamentoDestino = str(departamentoRes['nombreDepartamento'])
    
    clienteRes = conn.execute(clienteModel.select().where(clienteModel.c.id == idCliente)).fetchone()
    proveedorRes = conn.execute(proveedorModel.select().where(proveedorModel.c.id == idProveedor)).fetchone()
    
    cliente = str(clienteRes['razonSocial'])
    proveedor  = str(proveedorRes['razonSocial'])

    solicitudNuevaUnica = SolicitudUnicaRespuesta(
        guia=guia,
        estado=estado,
        fechaEntrega=fechaEntrega,
        servicio=servicio,
        numeroPaquete=numeroPaquete,
        contadorVisitas=contadorVisitas,
        primeraDireccion=primeraDireccion,
        segundaDireccion=segundaDireccion,
        fechaEmbarque=fechaEmbarque,
        fechaSalidaProyectada=fechaSalidaProyectada,
        fechaLlegadaProyectada=fechaLlegadaProyectada,
        fechaLlegadaReal=fechaLlegadaReal,
        via=via,
        fechaManifiesto=fechaManifiesto,
        estadoManifiesto=estadoManifiesto,
        incidenciaManifiesto=incidenciaManifiesto,
        fechaManifiestoRecogido=fechaManifiestoRecogido,
        fechaManifiestoInformado=fechaManifiestoInformado,
        fechaManifiestoVerificado=fechaManifiestoVerificado,
        fechaReparto=fechaReparto,
        fechaIncidenciaReparto=fechaIncidenciaReparto,
        fechaCompromiso=fechaCompromiso,
        sugerencia=sugerencia,
        cliente=cliente,
        proveedor=proveedor,
        distritoDestino=distritoDestino,
        provinciaDestino=provinciaDestino,
        departamentoDestino=departamentoDestino,
        tipoIncidenciaReparto=tipoIncidenciaReparto,
    )    
    
    return solicitudNuevaUnica


def listarCantidadIncidencias(filtro: ListarCantidadIncidenciasIn):
    filtro_dict = filtro.dict()
    fecha_inicio_str = "'" +  datetime.datetime.strptime(filtro_dict['fechaInicio'], "%d/%m/%Y").strftime("%Y-%m-%d") + "'" if filtro_dict['fechaInicio'] is not None else "NULL"
    fecha_fin_str = "'" +  datetime.datetime.strptime(filtro_dict['fechaFin'], "%d/%m/%Y").strftime("%Y-%m-%d") + "'" if filtro_dict['fechaFin'] is not None else "NULL" 
    cliente = "'" +  filtro_dict['cliente'] + "'" if filtro_dict['cliente'] is not None else "NULL"
    departamento = "'" +  filtro_dict['departamento'] + "'" if filtro_dict['departamento'] is not None else "NULL" 
    query_cantidades_text = QUERY_LISTAR_CANTIDAD_INCIDENCIAS.format(fecha_inicio = fecha_inicio_str, fecha_fin = fecha_fin_str, cliente = cliente,
                                                                        departamento = departamento)
    resultado = conn.execute(query_cantidades_text).fetchone()
    return ListarCantidadIncidenciasOut(cantidadIncidencias=resultado["cantidadIncidencias"] if resultado["cantidadIncidencias"] is not None else 0, 
                                        cantidadOK=resultado["cantidadOK"]if resultado["cantidadOK"] is not None else 0)


def listarCantidadIncidenciasPorTipo(filtro: ListarIncidenciasPorTipoIn):
    filtro_dict = filtro.dict()
    fecha_inicio_str = "'" +  datetime.datetime.strptime(filtro_dict['fechaInicio'], "%d/%m/%Y").strftime("%Y-%m-%d") + "'" if filtro_dict['fechaInicio'] is not None else "NULL"
    fecha_fin_str = "'" +  datetime.datetime.strptime(filtro_dict['fechaFin'], "%d/%m/%Y").strftime("%Y-%m-%d") + "'" if filtro_dict['fechaFin'] is not None else "NULL" 
    cliente = "'" +  filtro_dict['cliente'] + "'" if filtro_dict['cliente'] is not None else "NULL"
    departamento = "'" +  filtro_dict['departamento'] + "'" if filtro_dict['departamento'] is not None else "NULL" 
    query_cantidades_text = QUERY_LISTAR_CANTIDAD_INCIDENCIAS_POR_TIPO.format(fecha_inicio = fecha_inicio_str, fecha_fin = fecha_fin_str, cliente = cliente,
                                                                        departamento = departamento)
    resultados = conn.execute(query_cantidades_text).fetchall()
    lista_incidencias = [] 
    for resultado in resultados: 
        lista_incidencias.append(IncidenciaPorTipoOut(nombre=resultado["nombre"], cant=int(resultado["cant"])))
    return ListarIncidenciasPorTipoOut(listaIncidencias=lista_incidencias)