from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime
from config.db import meta, engine
from datetime import datetime



departamento = Table(
    "Departamento",
    meta,
    Column("id", Integer, primary_key=True),
    Column("nombreDepartamento", String(50))
)

meta.create_all(engine)