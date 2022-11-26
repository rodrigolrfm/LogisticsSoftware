from config.db import conn, SECRET
from models.Usuario import usuario as usuarioModel
from schemas.UsuarioSchema import Usuario
from schemas.UsuarioSchema import *
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


def loguearse(usuarioIniciarSesionIN:UsuarioIniciarSesionIN):
    
    userLog = usuarioIniciarSesionIN.dict()
    userBD = conn.execute(usuarioModel.select().where((usuarioModel.c.nombreUsuario == str(userLog['nombreUsuario'])) & 
                                                      (usuarioModel.c.password == str(userLog['password'])))).fetchone()
    usuarioResponse = UsuarioOUT(
        id=int(userBD['id']),
        nombreUsuario=str(userBD['nombreUsuario']),
        nombres=str(userBD['nombres']),
        apellidos=str(userBD['apellidos'])   
    )
    
    return usuarioResponse