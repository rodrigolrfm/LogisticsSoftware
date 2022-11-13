from config.db import conn, SECRET
from models.Departamento import departamento as departamentoModel
from schemas.DepartamentoSchema import Departamento
from fastapi import Response
from sqlalchemy import null, select
from starlette.status import HTTP_200_OK
from cryptography.fernet import Fernet
from hashlib import pbkdf2_hmac
from datetime import datetime



def registrarDepartamentoModule(departamento:Departamento):
    nuevoDepartamento = departamento.dict()
    resultado = conn.execute(departamentoModel.insert().values(nuevoDepartamento))
    return resultado.lastrowid