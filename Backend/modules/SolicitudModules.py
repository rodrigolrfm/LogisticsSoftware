from config.db import conn, SECRET
from models.Solicitud import solicitud as solicitudModel
from models.Solicitud import solicitud as solicitudModelSelect
from schemas.SolicitudSchema import Solicitud
from schemas.SolicitudSchema import SolicitudUnica

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
    
    cliente = clienteRes['razonSocial']
    proveedor  = proveedorRes['razonSocial']

    solicitudNuevaUnica = SolicitudUnica(
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
        razonNombreDestinatario=" "
    )    
    
    return solicitudNuevaUnica
