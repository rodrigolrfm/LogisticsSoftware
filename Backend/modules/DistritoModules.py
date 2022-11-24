from config.db import conn, SECRET
from models.Distrito import distrito as distritoModel
from schemas.DistritoSchema import Distrito
from fastapi import Response
from sqlalchemy import null, select
from starlette.status import HTTP_200_OK
from cryptography.fernet import Fernet
from hashlib import pbkdf2_hmac
from datetime import datetime



def registrarDistritoModule(distrito:Distrito):
    nuevoDistrito = distrito.dict()
    resultado = conn.execute(distritoModel.insert().values(nuevoDistrito))
    return resultado.lastrowid

def listarDistritoModule(nombre):
    distrito = conn.execute(distritoModel.select().where(distritoModel.c.nombreDistrito == nombre)).fetchone()
    if(distrito == None): 
        return registrarDistritoModule(distrito=Distrito(nombreDistrito=nombre))
    else: 
        return distrito._mapping['id']