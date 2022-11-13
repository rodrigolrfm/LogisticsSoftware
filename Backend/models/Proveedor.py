from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime
from config.db import meta, engine
from datetime import datetime

from models.Distrito import distrito as distritoModel


proveedor = Table(
    "Proveedor",
    meta,
    Column("id", Integer, primary_key=True),
    Column("razonSocial", String(100)),
    Column("idDistrito", Integer, ForeignKey(distritoModel.c.id))
)

meta.create_all(engine)