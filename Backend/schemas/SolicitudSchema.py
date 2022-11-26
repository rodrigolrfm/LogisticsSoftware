#Python
from typing import Optional, List
from enum import Enum
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

class Solicitud(BaseModel):
    id:Optional[int] = Field(default=None, example=1)
    guia: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=25,
        example="Lima"
    )
    estado: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Lima"
    )
    fechaEntrega: datetime = Field(default=None, example='2032-04-23T10:20:30.400+02:30')
    servicio: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Lima"
    )
    idDistritoOrigen:Optional[int] = Field(default=None, example=1)
    numeroPaquete:Optional[int] = Field(default=None, example=1)
    contadorVisitas:Optional[int] = Field(default=None, example=1)
    idDistritoDestino:Optional[int] = Field(default=None, example=1)
    razonNombreDestinatario: Optional[str] = Field(
        ...,
        max_length=100,
        example="Lima"
    )
    primeraDireccion: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Lima"
    )
    segundaDireccion: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Lima"
    )
    fechaEmbarque: datetime = Field(default=None, example='2032-04-23T10:20:30.400+02:30')
    fechaSalidaProyectada : datetime = Field(default=None, example='2032-04-23T10:20:30.400+02:30')
    fechaLlegadaProyectada: datetime = Field(default=None, example='2032-04-23T10:20:30.400+02:30')
    fechaLlegadaReal: datetime = Field(default=None, example='2032-04-23T10:20:30.400+02:30')
    via: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=10,
        example="Lima"
    )
    idCliente :Optional[int] = Field(default=None, example=1)
    idProveedor :Optional[int] = Field(default=None, example=1)
    fechaManifiesto: datetime = Field(default=None, example='2032-04-23T10:20:30.400+02:30')
    estadoManifiesto: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Lima"
    )
    incidenciaManifiesto: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Lima"
    )
    fechaManifiestoRecogido: datetime = Field(default=None, example='2032-04-23T10:20:30.400+02:30')
    fechaManifiestoInformado : datetime = Field(default=None, example='2032-04-23T10:20:30.400+02:30')
    fechaManifiestoVerificado: datetime = Field(default=None, example='2032-04-23T10:20:30.400+02:30')
    fechaReparto: datetime = Field(default=None, example='2032-04-23T10:20:30.400+02:30')
    tipoIncidenciaReparto: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Lima"
    )
    fechaIncidenciaReparto: datetime = Field(default=None, example='2032-04-23T10:20:30.400+02:30')
    fechaCompromiso: datetime = Field(default=None, example='2032-04-23T10:20:30.400+02:30')
    clima: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Lima"
    )
    temperatura: Optional[float]
    humedad: Optional[float]
    indiceCriminalidad: Optional[float]
    cantAccidentesTransito :Optional[int] = Field(default=None, example=1)
    cantPEA :Optional[int] = Field(default=None, example=1)
    cantFenoNatural :Optional[int] = Field(default=None, example=1)
    sugerencia: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=400,
        example="Lima"
    )
    
class SolicitudUnica(BaseModel):
    guia: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=25,
        example="Lima"
    )
    
class SolicitudUnicaRespuesta(BaseModel):
    guia: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=25,
        example="Lima"
    )
    estado: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Lima"
    )
    fechaEntrega: datetime = Field(default=None, example='2032-04-23T10:20:30.400+02:30')
    servicio: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Lima"
    )
    #idDistritoOrigen:Optional[int] = Field(default=None, example=1)
    numeroPaquete:Optional[int] = Field(default=None, example=1)
    contadorVisitas:Optional[int] = Field(default=None, example=1)
    distritoDestino:Optional[str] = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Lima"
    )
    provinciaDestino:Optional[str] = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Lima"
    )
    departamentoDestino:Optional[str] = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Lima"
    )
    primeraDireccion: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Lima"
    )
    segundaDireccion: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Lima"
    )
    fechaEmbarque: datetime = Field(default=None, example='2032-04-23T10:20:30.400+02:30')
    fechaSalidaProyectada : datetime = Field(default=None, example='2032-04-23T10:20:30.400+02:30')
    fechaLlegadaProyectada: datetime = Field(default=None, example='2032-04-23T10:20:30.400+02:30')
    fechaLlegadaReal: datetime = Field(default=None, example='2032-04-23T10:20:30.400+02:30')
    via: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=10,
        example="Lima"
    )
    cliente : Optional[str] = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Lima"
    )
    proveedor :Optional[str] = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Lima"
    )
    fechaManifiesto: datetime = Field(default=None, example='2032-04-23T10:20:30.400+02:30')
    estadoManifiesto: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Lima"
    )
    incidenciaManifiesto: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Lima"
    )
    fechaManifiestoRecogido: datetime = Field(default=None, example='2032-04-23T10:20:30.400+02:30')
    fechaManifiestoInformado : datetime = Field(default=None, example='2032-04-23T10:20:30.400+02:30')
    fechaManifiestoVerificado: datetime = Field(default=None, example='2032-04-23T10:20:30.400+02:30')
    fechaReparto: datetime = Field(default=None, example='2032-04-23T10:20:30.400+02:30')
    tipoIncidenciaReparto: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Lima"
    )
    fechaIncidenciaReparto: datetime = Field(default=None, example='2032-04-23T10:20:30.400+02:30')
    fechaCompromiso: datetime = Field(default=None, example='2032-04-23T10:20:30.400+02:30')
    sugerencia: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=400,
        example="Lima"
    )

class ListarCantidadIncidenciasIn(BaseModel):
    fechaInicio: Optional[str] = Field(default=None, example='21/01/2022')
    fechaFin: Optional[str] = Field(default=None, example='21/01/2022')
    cliente: Optional[str] = Field(default=None, example="Lima")
    departamento: Optional[str] = Field(default=None, example="Lima")

class ListarCantidadIncidenciasOut(BaseModel):
    cantidadIncidencias:int = Field(default=None, example=1)
    cantidadOK:int = Field(default=None, example=1)

class ListarIncidenciasPorTipoIn(BaseModel):
    fechaInicio: Optional[str] = Field(default=None, example='21/01/2022')
    fechaFin: Optional[str] = Field(default=None, example='21/01/2022')
    cliente: Optional[str] = Field(default=None, example="Lima")
    departamento: Optional[str] = Field(default=None, example="Lima")

class IncidenciaPorTipoOut(BaseModel): 
    nombre: str = Field(default=None, example="Lima")
    cant: int = Field(default=None, example=1) 

class ListarIncidenciasPorTipoOut(BaseModel):
    listaIncidencias:List[IncidenciaPorTipoOut] = Field(default=None, example=1)

class ListarIncidenciasProveedorIn(BaseModel):
    fechaInicio: Optional[str] = Field(default=None, example='21/01/2022')
    fechaFin: Optional[str] = Field(default=None, example='21/01/2022')
    cliente: Optional[str] = Field(default=None, example="Lima")
    departamento: Optional[str] = Field(default=None, example="Lima")
    proveedor: Optional[str] = Field(default=None, example="Lima")

class ListarIncidenciasProveedorOut(BaseModel):
    porcentaje:float

class IncidenciaMensualOut(BaseModel): 
    enero: str = Field(default=None, example="Lima")
    febrero: str = Field(default=None, example="Lima")
    marzo: str = Field(default=None, example="Lima")
    abril: str = Field(default=None, example="Lima")
    mayo: str = Field(default=None, example="Lima")
    junio: str = Field(default=None, example="Lima")
    julio: str = Field(default=None, example="Lima")
    agosto: str = Field(default=None, example="Lima")
    septiembre: str = Field(default=None, example="Lima")
    octubre: str = Field(default=None, example="Lima")
    noviembre: str = Field(default=None, example="Lima")
    diciembre: str = Field(default=None, example="Lima")