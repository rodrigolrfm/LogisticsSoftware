from config.db import conn, SECRET
from models.Usuario import usuario as usuarioModel
from schemas.UsuarioSchema import Usuario
from fastapi import Response
from sqlalchemy import null, select
from starlette.status import HTTP_200_OK
from cryptography.fernet import Fernet
from hashlib import pbkdf2_hmac
from datetime import datetime



def registrarUsuarioModule(usuario:Usuario):
    nuevoUsuario = usuario.dict()
    resultado = conn.execute(usuarioModel.insert().values(nuevoUsuario))
    return resultado.lastrowid