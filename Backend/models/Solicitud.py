from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime
from config.db import meta, engine
from datetime import datetime

solicitud = Table(
    "Solicitud",
    meta,
    Column("id", Integer, primary_key=True),
    Column("nombre", String(255)),
    Column("numeroDocumento", String(255)),
)

meta.create_all(engine)