from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime
from config.db import meta, engine
from datetime import datetime

usuario = Table(
    "Usuario",
    meta,
    Column("id", Integer, primary_key=True),
    Column("nombreUsuario", String(50)),
    Column("nombres", String(100)),
    Column("apellidos", String(100))
)

meta.create_all(engine)