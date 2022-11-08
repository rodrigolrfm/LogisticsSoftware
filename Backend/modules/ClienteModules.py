from config.db import conn, SECRET
from models.Cliente import cliente as clienteModel
from schemas.ClienteSchema import Cliente
from fastapi import Response
from sqlalchemy import null, select
from starlette.status import HTTP_200_OK
from cryptography.fernet import Fernet
from hashlib import pbkdf2_hmac
from datetime import datetime

key = Fernet.generate_key()
f = Fernet(key)

def registrarCliente(cliente:Cliente):
    nuevoCliente = cliente.dict()
    resultado = conn.execute(clienteModel.insert().values(nuevoCliente))
    return resultado.lastrowid