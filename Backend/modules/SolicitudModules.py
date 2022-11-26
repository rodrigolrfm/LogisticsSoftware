from config.db import conn, SECRET
from models.Solicitud import solicitud as solicitudModel
from models.Solicitud import solicitud as solicitudModelSelect
from schemas.SolicitudSchema import Solicitud
from schemas.SolicitudSchema import SolicitudUnica
from schemas.SolicitudSchema import SolicitudUnicaRespuesta
from schemas.SolicitudSchema import *
from models.Distrito import distrito as distritoModel
from models.Provincia import provincia as provinciaModel
from models.Departamento import departamento as departamentoModel
from models.Cliente import cliente as clienteModel
from models.Proveedor import proveedor as proveedorModel


from fastapi import Response
from sqlalchemy import null, select
from starlette.status import HTTP_200_OK
from cryptography.fernet import Fernet
from hashlib import pbkdf2_hmac
from datetime import datetime



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


def obtenerListaSolicitudModule(solicitud:SolicitudListarIncidentesIN):
    
    nuevoSolicitud = solicitud.dict()
    
    nomCliente = str(nuevoSolicitud['cliente'])
    idClienteSoli = None
    if nomCliente is None:
        clienteRes = conn.execute(clienteModel.select().where(clienteModel.c.razonSocial == nomCliente)).fetchone()
        idClienteSoli = int(clienteRes['id'])
    
    id_cliente_str = idClienteSoli if idClienteSoli is not None else "NULL"
    
    
    nomDepar = nuevoSolicitud['departamento']
    
    
    #Fechas
    fechaInicio = nuevoSolicitud['fechaInicio']
    fechaFin = nuevoSolicitud['fechaFin']
    
    nombreTipoIncidencia = nuevoSolicitud['tipoIncidencia']
    solicitudGuia = nuevoSolicitud['numGuia']
    
    datetime_object_inicio = datetime.strptime(fechaInicio, '%d/%m/%Y')
    datetime_object_fin = datetime.strptime(fechaFin, '%d/%m/%Y')
    
    num_guia = solicitudGuia if solicitudGuia is not None else "NULL"
    num_guia_null = "'" + solicitudGuia + "'" if solicitudGuia is not None else "NULL"
    
    nom_dep_str = nomDepar if nomDepar is not None else "NULL"
    nom_dep_null_str = "'" + nomDepar + "'" if nomDepar is not None else "NULL"
    
    tipo_incidencia = nombreTipoIncidencia if nombreTipoIncidencia is not None else "NULL"
    tipo_incidencia_null = "'" + nombreTipoIncidencia + "'" if nombreTipoIncidencia is not None else "NULL"   
    
    
    stringVal = '''select *
                from Solicitud s
                inner join Distrito d
                on s.idDistritoDestino = d.id
                inner join Provincia p
                on d.idProvincia = p.id
                inner join Departamento dep
                on dep.id = p.idDepartamento
                where (fechaEntrega >= '{fechaInicio}' and fechaEntrega <= '{fechaFin}') and
                (guia like '%%{num_guia}%%' or {num_guia_null} is NULL) and 
                (tipoIncidenciaReparto like '%%{tipo_incidencia}%%' or {tipo_incidencia_null} is NULL) and 
                (idCliente={id_cliente} or {id_cliente} is NULL) and 
                (dep.nombreDepartamento LIKE '%%{nom_dep}%%' or {nom_dep_null} is NULL)
                '''
    
    query_soliciutd_text = stringVal.format(
                            fechaInicio=datetime_object_inicio,
                            fechaFin=datetime_object_fin,
                            num_guia=num_guia,
                            num_guia_null=num_guia_null,
                            tipo_incidencia=tipo_incidencia,
                            tipo_incidencia_null=tipo_incidencia_null,
                            id_cliente=id_cliente_str,
                            nom_dep=nom_dep_str,
                            nom_dep_null=nom_dep_null_str
                        )
    
    solicitudes_bd = conn.execute(query_soliciutd_text).fetchall()
    
    response = []
    for solicitud_un in solicitudes_bd:
        guia_str = solicitud_un['guia']
        fechaCompromiso_str = solicitud_un['fechaCompromiso']
        fechaEntrega_str = solicitud_un['fechaEntrega']
        numeroPaquete_str = int(solicitud_un['numeroPaquete'])
        cliente_id = solicitud_un['idCliente']
        clienteResSoli = conn.execute(clienteModel.select().where(clienteModel.c.id == cliente_id)).fetchone()
        cliente_str_soli = str(clienteResSoli['razonSocial'])
        estado_str = solicitud_un['estado']
        obj = SolicitudListarIncidentesOUT(
            guia=guia_str,
            fechaCompromiso=fechaCompromiso_str,
            fechaEntrega=fechaEntrega_str,
            numeroPaquete=numeroPaquete_str,
            cliente=cliente_str_soli,
            estado=estado_str
        )
        response.append(obj.__dict__)
    
    return response
