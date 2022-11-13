from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime, Float
from config.db import meta, engine
from datetime import datetime

from models.Distrito import distrito as distritoOrigenModel
from models.Distrito import distrito as distritoDestinoModel
from models.Proveedor import proveedor as proveedorModel
from models.Cliente import cliente as clienteModel

solicitud = Table(
    "Solicitud",
    meta,
    Column("id", Integer, primary_key=True),
    Column("guia", String(25)),
    Column("estado", String(100)),
    Column("fechaEntrega", DateTime),
    Column("servicio", String(50)),
    Column("idDistritoOrigen", Integer, ForeignKey(distritoOrigenModel.c.id)),
    Column("numeroPaquete", Integer),
    Column("contadorVisitas", Integer),
    Column("idDistritoDestino", Integer, ForeignKey(distritoDestinoModel.c.id)),
    Column("razonNombreDestinatario", String(100)),
    Column("primeraDireccion", String(100)),
    Column("segundaDireccion", String(100)),
    Column("fechaEmbarque", DateTime),
    Column("fechaSalidaProyectada", DateTime),
    Column("fechaLlegadaProyectada", DateTime),
    Column("fechaLlegadaReal", DateTime),
    Column("via", String(10)),
    Column("idCliente", Integer,ForeignKey(clienteModel.c.id)),
    Column("idProveedor", Integer,ForeignKey(proveedorModel.c.id)),
    Column("fechaManifiesto", DateTime),
    Column("estadoManifiesto", String(50)),
    Column("incidenciaManifiesto", String(100)),
    Column("fechaManifiestoRecogido", DateTime),
    Column("fechaManifiestoInformado", DateTime),
    Column("fechaManifiestoVerificado", DateTime),
    Column("fechaReparto", DateTime),
    Column("tipoIncidenciaReparto", String(100)),
    Column("fechaIncidenciaReparto", DateTime),
    Column("fechaCompromiso", DateTime),
    Column("clima", String(50)),
    Column("temperatura", Float),
    Column("humedad", Float),
    Column("indiceCriminalidad", Float),
    Column("cantAccidentesTransito", Integer),
    Column("cantPEA", Integer),
    Column("cantFenoNatural", Integer),
    Column("sugerencia", String(400))
)

meta.create_all(engine)