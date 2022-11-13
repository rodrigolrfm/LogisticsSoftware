from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime
from config.db import meta, engine
from datetime import datetime

from models.Provincia import provincia as provinciaModel


distrito = Table(
    "Distrito",
    meta,
    Column("id", Integer, primary_key=True),
    Column("nombreDistrito", String(100)),
    Column("idProvincia", Integer, ForeignKey(provinciaModel.c.id))
)

meta.create_all(engine)