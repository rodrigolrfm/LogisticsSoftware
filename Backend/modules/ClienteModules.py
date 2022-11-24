from config.db import conn, SECRET
from models.Cliente import cliente as clienteModel
from schemas.ClienteSchema import Cliente
from fastapi import Response
from sqlalchemy import null, select
from starlette.status import HTTP_200_OK
from cryptography.fernet import Fernet
from hashlib import pbkdf2_hmac
from datetime import datetime



def registrarClienteModule(cliente:Cliente):
    nuevoCliente = cliente.dict()
    resultado = conn.execute(clienteModel.insert().values(nuevoCliente))
    return resultado.lastrowid

def listarClienteModule(razonSocial):
    cliente = conn.execute(clienteModel.select().where(clienteModel.c.razonSocial == razonSocial)).fetchone()
    if(cliente == None): 
        return registrarClienteModule(cliente=Cliente(razonSocial=razonSocial))
    else: 
        return cliente._mapping['id']   