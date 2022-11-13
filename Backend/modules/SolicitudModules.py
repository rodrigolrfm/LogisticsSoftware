from config.db import conn, SECRET
from models.Solicitud import solicitud as solicitudModel
from schemas.SolicitudSchema import Solicitud
from fastapi import Response
from sqlalchemy import null, select
from starlette.status import HTTP_200_OK
from cryptography.fernet import Fernet
from hashlib import pbkdf2_hmac
from datetime import datetime



def registrarSolicitudModule(solicitud:Solicitud):
    nuevoSolicitud = solicitud.dict()
    resultado = conn.execute(solicitudModel.insert().values(nuevoSolicitud))
    return resultado.lastrowid