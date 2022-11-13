from config.db import conn, SECRET
from models.Provincia import provincia as provinciaModel
from schemas.ProvinciaSchema import Provincia
from fastapi import Response
from sqlalchemy import null, select
from starlette.status import HTTP_200_OK
from cryptography.fernet import Fernet
from hashlib import pbkdf2_hmac
from datetime import datetime



def registrarProvinciaModule(provincia:Provincia):
    nuevoProvincia = provincia.dict()
    resultado = conn.execute(provinciaModel.insert().values(nuevoProvincia))
    return resultado.lastrowid