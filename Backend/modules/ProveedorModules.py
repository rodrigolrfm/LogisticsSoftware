from config.db import conn, SECRET
from models.Proveedor import proveedor as proveedorModel
from schemas.ProveedorSchema import Proveedor
from fastapi import Response
from sqlalchemy import null, select
from starlette.status import HTTP_200_OK
from cryptography.fernet import Fernet
from hashlib import pbkdf2_hmac
from datetime import datetime



def registrarProveedorModule(proveedor:Proveedor):
    nuevoProveedor = proveedor.dict()
    resultado = conn.execute(proveedorModel.insert().values(nuevoProveedor))
    return resultado.lastrowid


def listarProveedorModule(razonSocial):
    proveedor = conn.execute(proveedorModel.select().where(proveedorModel.c.razonSocial == razonSocial)).fetchone()
    if(proveedor == None): 
        return registrarProveedorModule(proveedor=Proveedor(razonSocial=razonSocial))
    else: 
        return proveedor._mapping['id']   