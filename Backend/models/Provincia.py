from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime
from config.db import meta, engine
from datetime import datetime

from models.Departamento import departamento as departamentoModel


provincia = Table(
    "Provincia",
    meta,
    Column("id", Integer, primary_key=True),
    Column("nombreProvincia", String(100)),
    Column("idDepartamento", Integer, ForeignKey(departamentoModel.c.id))
)

meta.create_all(engine)