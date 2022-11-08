# -*- codificación: utf-8 -*-
from fastapi import APIRouter, Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from config.db import conn, SECRET
from hashlib import pbkdf2_hmac
from modules.ClienteModules import *
import numpy as np
from fastapi import FastAPI, File, UploadFile
from geopy.geocoders import Nominatim
from modules import *
from xgboost import XGBClassifier
from schemas.ClienteSchema import Cliente
import requests
import csv
import pandas as pd 
import io
import datetime
from config.db import conn
from datetime import timezone
import dateutil.parser
import json
from sqlalchemy import select
from fastapi import Body, Query, Path, Form, Header, Cookie, UploadFile, File
router = APIRouter()

"""
listaProblemasGeograficoDatos = [0]*25
listaDatosAdultosMayores = [0]*25
listaDatosAccTransito = [0]*25
listaDepartamentos = list()
"""

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

dictionaryServicios = {'PROVINCIA': 0,
 'PEDIDO': 1,
 'DOMICILIO': 2,
 'NORMAL': 3,
 'RUNASTORE PROVINCIA': 4,
 'H&M PROVINCIA': 5,
 'E COMMERCE': 6,
 'SERVICIO PAGADO PROVINCIA': 7,
 'RIPLEY MP PROVINCIA': 8,
 'MARKETPLACE CONECTA': 9,
 'VENTA ONLINE': 10,
 'RIPLEY MP URBANO': 11,
 'MINISO PROVINCIA': 12,
 'SAC': 13,
 'SONY PROVINCIA': 14,
 'TOTTUS PROVINCIA': 15,
 'LOGISTICA INVERSA LIMA': 16,
 'ENLACE MASTER 5': 17,
 'RIPLEY MP ALEJADO': 18,
 'E-SELLER PROVINCIA': 19,
 'SERVICIO COOLBOX': 20,
 'ENVIO PREMIOS': 21,
 'REQUERIMIENTOS': 22,
 'ESSEN NORTE Y SUR CHICO URBANO': 23,
 'RIPLEY MP PERIFERICO': 24,
 'SERVICIO PAGO CONTRAENTREGA PROV': 25,
 'ESSEN EXTREMO URBANO': 26,
 'DISTRIBUCIÓN INTEGRAL': 27,
 'COURIER': 28,
 'BIG- TICKET PROVINCIA': 29,
 'ESSEN RURAL': 30,
 'REPARTO PROVINCIA': 31,
 'ESSEN LOCAL URBANO': 32,
 'NUSKIN PROVINCIA': 33,
 'ENLACE MASTER 4': 34,
 'FLASH MOBILE ENROLLMENT LIMA': 35,
 'GOTTA PROVINCIA': 36,
 'SMART BRANDS PROVINCIA': 37,
 'RECOJO HIPERSALE': 38,
 'REPARTO NACIONAL': 39,
 'FESTO': 40,
 'MIO PROVINCIA': 41,
 'KUKULI PROVINCIA': 42,
 'PICK UP POINT PROVINCIA': 43,
 'SERVICIO CARGA ASPERSUR': 44,
 'CREDITEX PROVINCIA': 45,
 'MAYORISTA': 46,
 'DEVOLUCION': 47,
 'ESSEN NORTE Y SUR URBANO': 48,
 'GAMARRA CLICK PROVINCIA': 49,
 'ESSEN NORTE Y SUR CHICO PERIFERI': 50,
 'PROPAGANDA': 51,
 'CAMBIO MANO A MANO': 52,
 'ESSEN NORTE Y SUR PERIFERICO': 53,
 'DEVOLUCION RIPLEY': 54,
 'RECOJO ADIDAS': 55,
 'KAYSER PROVINCIA': 56,
 'ESSEN EXTREMO PERIFERICO': 57,
 'SERVICIO CD RIPLEY': 58,
 'VANS PROVINCIA': 59,
 'ESSEN LOCAL PERIFERICO': 60,
 'LOGISTICA INVERSA PROVINCIA': 61,
 'SERVICIO PRIME': 62,
 'AMPHORA PROVINCIA': 63,
 'LOG INVERSA LIMA1P': 64,
 'CARGOS': 65,
 'SERVICIO PARA ALTOS ANDES': 66,
 'REPARTO MARXIAL': 67,
 'DEVOLUCION CONECTA': 68,
 'ILAHUI  LIMA': 69,
 'REEMBARQUE': 70,
 'ILAHUI PROVINCIA': 71,
 'SERVICIO PSP': 72,
 'H&M DEVOLUCION': 73,
 'FACTURAS': 74,
 'LOG INVERSA PROV3P': 75,
 'NHT JUDAMIL': 76,
 'DEVOLUCIONES': 77,
 'DESPACHO A DOMICILIO RIPLEY': 78,
 'LOG INVERSA PROV1P': 79,
 'DEVOLUCIÓN DE CAJAS': 80,
 'REQUERIMIENTO NATURA': 81,
 'ADICIONAL MOVILIDAD DIARIA': 82,
 'SOBRE': 83,
 'RECOJO ESSEN': 84,
 'REGULAR ': 85,
 'H&M RECOJO': 86,
 'GRUPO TABERNERO': 87,
 'ILARIA PROVINCIA': 88,
 'BITEL PAGO CONTRAENTREGA': 89,
 'REPARTO VALIJAS': 90,
 'DISTRIBUCIÓN INTEGRAL ': 91,
 'RECOJO COOLBOX': 92,
 'L’OCCITANE PROVINCIA': 93,
 'MODELLA GROUP PROVINCIA': 94,
 'RECOJO AMPHORA': 95,
 'FLASH MOBILE SHOPP CART LIMA': 96,
 'FLASH MOBILE SHOPP CAT PROV': 97,
 'INCIDENCIAS': 98,
 'RECOJO GOTTA': 99,
 ' SERV. EXPRESS URBANO': 100,
 'WECOOL PROVINCIA': 101,
 'NORMAL ': 102,
 'ENTREGA Y RECOJO PROVINCIA': 103}

dictionaryDepartamentos = {'CAJAMARCA': 0,
 'SAN MARTIN': 1,
 'HUANUCO': 2,
 'LIMA': 3,
 'AMAZONAS': 4,
 'PIURA': 5,
 'UCAYALI': 6,
 'LORETO': 7,
 'CUSCO': 8,
 'HUANCAVELICA': 9,
 'PUNO': 10,
 'LA LIBERTAD': 11,
 'AREQUIPA': 12,
 'AYACUCHO': 13,
 'JUNIN': 14,
 'TACNA': 15,
 'ICA': 16,
 'LAMBAYEQUE': 17,
 'MOQUEGUA': 18,
 'TUMBES': 19,
 'ANCASH': 20,
 'PASCO': 21,
 'MADRE DE DIOS': 22,
 'APURIMAC': 23,
 'CALLAO': 24}

dictionaryClimas = {'Rain': 0, 'Clouds': 1, 'Clear': 2, 'Fog': 3, 'Mist': 4}


dictionaryTipoIncidencia =  {'DIRECCION INCOMPLETA': 0,
 'REEMBARQUE COLECTIVO': 1,
 'ES OTRA ZONA': 2,
 'SOCIAL': 3,
 'AUSENTE': 4,
 'CLIMATICO': 5,
 'DE VIAJE': 6,
 'DIRECCION ERRADA': 7,
 'SE MUDO': 8,
 'DIRECCIÓN NO ACCESIBLE': 9,
 'MERCADERIA SINIESTRADA (ROBO)': 10,
 'FALLAS MECANICAS EN REPARTO': 11,
 'ZONA PELIGROSA': 12,
 'NUEVA ZONA': 13,
 'OK': 14,
 'DIRECCION INEXACTA': 15}

dictionaryIncidenciaMan =  {'OK': 0,
 'RECOJO CON INCIDENCIAS': 1,
 'RECOJO NO LLEGO': 2,
 'RECOJO RETRASADO': 3,
 'VERIFICACION VARIOS': 4,
 'PEDIDO NO LLEGO': 5}
 


dictionarySugerencias = {'REGISTRAR CORRECTAMENTE LA DIRECCION DE DESTINO': 0,
 'ENTREGAR NUMERO DE REFERENCIA DE LOS INTERMEDIARIOS': 1,
 'AUMENTAR LA CANTIDAD DE DIAS DE ENTREGA PARA ESTAS FECHAS': 2,
 'COORDINAR PREEVIAMENTE CON EL DESTINATARIO LA FECHA Y HORA DE ENTREGA': 3,
 'COORDINAR CON EL DESTINATARIO/REPORTAR AL CLIENTE': 4,
 'COORDINAR CON EL DESTINATARIO PARA EL RECOJO EN LA AGENCIA': 5,
 'REALIZAR MANTENIMIENTO DE TRANSPORTE O HABLAR CON PROVEEDOR': 6,
 'OK': 7}

dictionaryVias = {'TT': 0, 'TA': 1}

@router.post("/registrarCliente/")
async def registrarCliente(cliente: Cliente = Body(...)):
    return registrarCliente(cliente)



@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile | None = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        dataset = pd.read_csv(file.file,sep=";")
        
        # Se crean agregan los parámetros de la longitud y longitud de los departamentos
        dataset["Latitud"]=0
        dataset["Longitud"]=0
        print(type(dataset))
        print(dataset.columns)
        loc = Nominatim(user_agent="GetLoc") 
        departamento = dataset.loc[0,"DEPARTAMENTO"]
        distrito = dataset.loc[0,"DISTRITO"]
        provincia = dataset.loc[0,"PROVINCIA"]
        cliente = dataset.loc[0,"CLIENTE"]
        incidente = dataset.loc[0,"TIPO_INCIDENCIA_REPARTO"]
        proveedor = dataset.loc[0,"PROVEEDOR DE TRANSPORTE"]
        print(departamento)
        getLoc = loc.geocode(departamento) 
        longitud =  getLoc.longitude
        latitud = getLoc.latitude
        dataset.loc[0,"Latitud"] = latitud
        dataset.loc[0,"Longitud"] = longitud
        
        dataset["TEMPERATURA"]=0
        dataset["HUMEDAD"]=0
        dataset["CLIMA"]= ""
        
        
        fechaReparto = dataset.loc[0,"FECHA REPARTO"]
        my_ts = fechaReparto.split("/")
        dt = datetime.datetime(int(my_ts[2]), int(my_ts[1]), int(my_ts[0]))
        timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
        dateInit = str(timestamp+64800)
        dateInitUnix = dateInit[0:len(dateInit)-2]
        url = "http://history.openweathermap.org/data/2.5/history/city?lat={}&lon={}&type=hour&start={}&end={}&appid=b9c3fde5b6c1179bccc0b366a4d04fd0&units=metric".format(str(dataset.loc[0,"Latitud"]),str(dataset.loc[0,"Longitud"]),dateInitUnix,dateInitUnix)
        res = requests.get(url)
        data = res.json()
        temperatura = data["list"][0]["main"]["temp"]
        humedad = data["list"][0]["main"]["humidity"]
        clima = data["list"][0]["weather"][0]["main"]
        dataset.loc[0,"TEMPERATURA"] = temperatura
        dataset.loc[0,"HUMEDAD"] = humedad
        dataset.loc[0,"CLIMA"] = clima
        
        
        response = requests.get('http://datacrim.inei.gob.pe/csv_controller/index?desde=tematico&id=40001')
        df = pd.read_csv(io.StringIO(response.text), sep=',', header=None, quoting=csv.QUOTE_ALL)
        df[0] = df[0].astype('string')
        df[1] = df[1].astype('string')
        df[2] = df[2].astype('string')
        dataCrime = df.loc[(df[0]=="2021") & (df[1]!="NACIONAL")]
        val = list(dataCrime.loc[dataCrime[1]=="DEPARTAMENTO DE LIMA 2/"][2])[0]
        dataCrime.drop(dataCrime.loc[dataCrime[1]=="DEPARTAMENTO DE LIMA 2/"].index, inplace=True)
        dataCrime[2] = dataCrime[2].astype('float')
        indiceLima = int(dataCrime.loc[dataCrime[1]=="LIMA METROPOLITANA 1/"].index[0])
        indiceCallao = int(dataCrime.loc[dataCrime[1]=="PROVINCIA CONSTITUCIONAL DEL CALLAO"].index[0])
        dataCrime.loc[indiceCallao,1] = "LIMA"
        dataCrime.loc[indiceLima,1] = "LIMA"
        
        
        print("impresión de datacrime")
        print(dataCrime.columns)
        
        url = 'https://systems.inei.gob.pe/SIRTOD/app/consulta/getTableDataYear?indicador_listado=262432%2C262433%2C262429%2C420794%2C262428%2C420795&tipo_ubigeo=1&desde_anio=2020&hasta_anio=2020&ubigeo_listado=&idioma=ES'
        dataProblemaGeografico = list()
        dataProblemaGeograficoRequest = requests.get(url)
        dataProblemaGeografico = dataProblemaGeograficoRequest.json()
        
        url2 = "https://systems.inei.gob.pe/SIRTOD/app/consulta/getTableDataYear?indicador_listado=516860&tipo_ubigeo=1&desde_anio=2017&hasta_anio=2017&ubigeo_listado=&idioma=ES"
        dataProblemaAdultoMayor = list()
        dataProblemaAdultoMayorRequest = requests.get(url2)
        dataProblemaAdultoMayor = dataProblemaAdultoMayorRequest.json()
        
        url3 = "https://systems.inei.gob.pe/SIRTOD/app/consulta/getTableDataYear?indicador_listado=394842&tipo_ubigeo=1&desde_anio=2021&hasta_anio=2021&ubigeo_listado=&idioma=ES"
        dataAccidentesTransito = list()
        dataAccidentesTransitoRequest = requests.get(url3)
        dataAccidentesTransito = dataAccidentesTransitoRequest.json()
        
        listaDepartamentos = list()
        for i in dataProblemaGeografico:
            if (i["departamento"] not in listaDepartamentos):
                listaDepartamentos.append(i["departamento"])
                
        # Calculo de datos de problemas naturales
        listaProblemasGeograficoDatos = [0]*25
        for i in dataProblemaGeografico:
            if (i["departamento"] in listaDepartamentos):
                index = listaDepartamentos.index(i["departamento"])
                listaProblemasGeograficoDatos[index] = int(listaProblemasGeograficoDatos[index]) + int(i["dato"].replace(" ",""))
        
        # Calculo de datos de adultos mayores
        listaDatosAdultosMayores = [0]*25
        for i in dataProblemaAdultoMayor:
            if (i["departamento"] in listaDepartamentos):
                index = listaDepartamentos.index(i["departamento"])
                listaDatosAdultosMayores[index] = int(listaDatosAdultosMayores[index]) + int(i["dato"].replace(" ",""))
        
        # Calculo de datos de accidentes de transito
        listaDatosAccTransito = [0]*25
        for i in dataAccidentesTransito:
            if (i["departamento"] in listaDepartamentos):
                index = listaDepartamentos.index(i["departamento"])
                listaDatosAccTransito[index] = int(listaDatosAccTransito[index]) + int(i["dato"].replace(" ",""))
        
        listaDepartamentos = list(map(lambda x : normalize(x), listaDepartamentos))
        
        dataCrime.rename(columns = {0:'AÑO', 1:'DEPARTAMENTO',2:'INDICE_DELITOS'}, inplace = True)
        
        dataCrime["CANT_FENO_NAT"]=0
        dataCrime["CANT_ADULTOMAYOR"]=0
        dataCrime["CANT_ACC_TRANSITO"]=0
        
        for i in dataCrime.index:
            departamento = str(dataCrime.loc[i,"DEPARTAMENTO"])
            if (departamento in listaDepartamentos):
                index_departamento = listaDepartamentos.index(departamento)
                val_prob_geo = listaProblemasGeograficoDatos[index_departamento]
                val_cant_adul_mayor = listaDatosAdultosMayores[index_departamento]
                val_cant_acc_transito = listaDatosAccTransito[index_departamento]
                dataCrime.loc[i,"CANT_FENO_NAT"] = val_prob_geo
                dataCrime.loc[i,"CANT_ADULTOMAYOR"] = val_cant_adul_mayor
                dataCrime.loc[i,"CANT_ACC_TRANSITO"] = val_cant_acc_transito
        
        newDataSet = pd.merge(dataset, dataCrime, how='inner', on = 'DEPARTAMENTO')
        dataset = newDataSet
        dataset["DIRECCION1"] = dataset["DIRECCION1"].str.upper()
        dataset["TIENE_AV"] = dataset.DIRECCION1.str.contains("AV|AVENIDA",regex=True,case=False)
        dataset["TIENE_JR"] = dataset.DIRECCION1.str.contains("JR|JIRON",regex=True,case=False)
        dataset["TIENE_CALLE"] = dataset.DIRECCION1.str.contains("CALLE",regex=True,case=False)
        
        dataset = dataset.drop(dataset[dataset.TIPO_INCIDENCIA_REPARTO == "COORDINADO"].index)
        dataset = dataset.drop(dataset[dataset.TIPO_INCIDENCIA_REPARTO == "REPROGRAMACION"].index)
        dataset = dataset.drop(dataset[dataset.TIPO_INCIDENCIA_REPARTO == "REEMBARQUE ENTREGA EN AGENCIA"].index)
        dataset = dataset.drop(dataset[dataset.TIPO_INCIDENCIA_REPARTO == "DESCONOCIDO/NO DA RAZÓN"].index)
        dataset = dataset.drop(dataset[dataset.TIPO_INCIDENCIA_REPARTO == "RECOJO EN OFICINA"].index)
        dataset = dataset.drop(dataset[dataset.TIPO_INCIDENCIA_REPARTO == "RECHAZADO"].index)
        dataset = dataset.drop(dataset[dataset.TIPO_INCIDENCIA_REPARTO == "DESPACHO ERRADO"].index)
        dataset["TIPO_INCIDENCIA_REPARTO"] = np.where(dataset["TIPO_INCIDENCIA_REPARTO"].isna(), 'OK', dataset["TIPO_INCIDENCIA_REPARTO"])
        dataset = dataset.drop(dataset[dataset.ESTADO_MANIFIESTO == "RECOGIDO"].index)
        dataset = dataset.drop(dataset[dataset.ESTADO_MANIFIESTO == "PENDIENTE"].index)
        dataset = dataset.drop(dataset[dataset.ESTADO_MANIFIESTO == "INFORMADO"].index)
        dataset = dataset.drop(dataset[dataset.ESTADO_MANIFIESTO == "DDV"].index)
        dataset = dataset.drop(dataset[dataset.DEPARTAMENTO.isnull()].index)
        
        dataset = dataset.drop(['GUIA'], axis=1)
        dataset = dataset.drop(['AÑO'], axis=1)
        dataset = dataset.drop(['DIRECCION1'], axis=1)
        dataset = dataset.drop(['N_MANIFIESTO'], axis=1)
        dataset = dataset.drop(['PROVINCIA'], axis=1)
        dataset = dataset.drop(['DISTRITO'], axis=1)
        dataset = dataset.drop(['NUMERO REPARTO'], axis=1)
        dataset = dataset.drop(['FECHA MANIFIESTO_VERIFICADO'], axis=1)
        dataset = dataset.drop(['ORIGEN_BASE'], axis=1)
        dataset = dataset.drop(['REMITENTE'], axis=1)
        dataset = dataset.drop(['FECHA_EMBARQUE'], axis=1)
        dataset = dataset.drop(['FORMA_CONF_ENTREGA'], axis=1)
        dataset = dataset.drop(['CONSIGNATARIO'], axis=1)
        dataset = dataset.drop(['DESTINO_BASE'], axis=1)
        dataset = dataset.drop(['REPRESENTANTE'], axis=1)
        dataset = dataset.drop(['DIRECCION2'], axis=1)
        dataset = dataset.drop(['FECHA_LLEGADA_PROYECT'], axis=1)
        dataset = dataset.drop(['FECHA_LLEGADA_REAL'], axis=1)
        dataset = dataset.drop(['FECHA MANIFIESTO_RECOGIDO'], axis=1)
        dataset = dataset.drop(['FECHA MANIFIESTO_INFORMADO'], axis=1)
        dataset = dataset.drop(['FECHA REPARTO'], axis=1)
        dataset = dataset.drop(['DESTINO'], axis=1)
        dataset = dataset.drop(['FECHA_COMPROMISO'], axis=1)
        dataset = dataset.drop(['FECHA_MANIFIESTO'], axis=1)
        dataset = dataset.drop(['RESP_REPARTO'], axis=1)
        dataset = dataset.drop(['FECHA_INCIDENCIA_REPARTO'], axis=1)
        dataset = dataset.drop(['FECHA_SALIDA_PROYECT'], axis=1)
        dataset = dataset.drop(['FECHA_GUIA'], axis=1)
        dataset = dataset.drop(['FECHA_ENTREGA'], axis=1)
        dataset = dataset.drop(['ORIGEN'], axis=1)
        dataset = dataset.drop(['GESTORA_SERVICIO'], axis=1)
        dataset = dataset.drop(['PROVEEDOR DE TRANSPORTE'], axis=1)
        dataset = dataset.drop(['CLIENTE'], axis=1)
        #dataset = dataset.drop(['count'], axis=1)
        dataset = dataset.drop(['ESTADO_MANIFIESTO'], axis=1)
        dataset = dataset.drop(['ESTADO_GUIA'], axis=1)
        dataset = dataset.drop(['TIPO_INCIDENCIA_REPARTO'], axis=1)
        
        moda = dataset['VIA'].mode()[0]
        dataset['VIA'] = dataset['VIA'].fillna(moda)

        moda = dataset['SERVICIO'].mode()[0]
        dataset['SERVICIO'] = dataset['SERVICIO'].fillna(moda)

        moda = dataset['DEPARTAMENTO'].mode()[0]
        dataset['DEPARTAMENTO'] = dataset['DEPARTAMENTO'].fillna(moda)

        dataset['TIENE_AV'] = np.where(dataset['TIENE_AV']==True, 1, dataset['TIENE_AV'])
        dataset['TIENE_AV'] = np.where(dataset['TIENE_AV']==False, 0, dataset['TIENE_AV'])
        dataset['TIENE_AV'] = np.where(dataset['TIENE_AV'].isna()==True, 0, dataset['TIENE_AV'])
        dataset['TIENE_JR'] = np.where(dataset['TIENE_JR']==True, 1, dataset['TIENE_JR'])
        dataset['TIENE_JR'] = np.where(dataset['TIENE_JR']==False, 0, dataset['TIENE_JR'])
        dataset['TIENE_JR'] = np.where(dataset['TIENE_JR'].isna()==True, 0, dataset['TIENE_JR'])
        dataset['TIENE_CALLE'] = np.where(dataset['TIENE_CALLE']==True, 1, dataset['TIENE_CALLE'])
        dataset['TIENE_CALLE'] = np.where(dataset['TIENE_CALLE']==False, 0, dataset['TIENE_CALLE'])
        dataset['TIENE_CALLE'] = np.where(dataset['TIENE_CALLE'].isna()==True, 0, dataset['TIENE_CALLE'])
        dataset['INCIDENCIA_MANIFIESTO'] = np.where(dataset['INCIDENCIA_MANIFIESTO'].isnull()==True, 'OK', dataset['INCIDENCIA_MANIFIESTO'])
        
        dataset['NO_TIENE_REF'] = 0
        dataset['NO_TIENE_REF'] = np.where((dataset['TIENE_AV']==0) & (dataset['TIENE_JR']==0) & (dataset['TIENE_CALLE']==0), 1, dataset['NO_TIENE_REF'])
        dataset["TIENE_AV"] = dataset["TIENE_AV"].astype('int')
        dataset["TIENE_JR"] =dataset["TIENE_JR"].astype('int')
        dataset["TIENE_CALLE"] =dataset["TIENE_CALLE"].astype('int')
        dataset["NO_TIENE_REF"] = dataset["NO_TIENE_REF"].astype('int')
        
        for i in dataset.index:
            departamento = str(dataset.loc[i,"DEPARTAMENTO"])
            servicio = str(dataset.loc[i,"SERVICIO"])
            via = str(dataset.loc[i,"VIA"])
            incidenciaMan = str(dataset.loc[i,"INCIDENCIA_MANIFIESTO"])
            #tipoIncidencia = str(dataset.loc[i,"TIPO_INCIDENCIA_REPARTO"])
            clima = str(dataset.loc[i,"CLIMA"])

            val_departamento = dictionaryDepartamentos[departamento]
            val_servicio = dictionaryServicios[servicio]
            val_via = dictionaryVias[via]
            val_incidenciaMan = dictionaryIncidenciaMan[incidenciaMan]
            #val_tipoIncidencia = dictionaryTipoIncidencia[tipoIncidencia]
            val_clima = dictionaryClimas[clima]

            dataset.loc[i,"SERVICIO"] = val_servicio
            dataset.loc[i,"DEPARTAMENTO"] = val_departamento
            dataset.loc[i,"VIA"] = val_via
            dataset.loc[i,"INCIDENCIA_MANIFIESTO"] = val_incidenciaMan
            #dataset.loc[i,"TIPO_INCIDENCIA_REPARTO"] = val_tipoIncidencia
            dataset.loc[i,"CLIMA"] = val_clima
        
        dataset["SERVICIO"] = dataset["SERVICIO"].astype('int')
        dataset["DEPARTAMENTO"] =dataset["DEPARTAMENTO"].astype('int')
        dataset["VIA"] =dataset["VIA"].astype('int')
        dataset["INCIDENCIA_MANIFIESTO"] = dataset["INCIDENCIA_MANIFIESTO"].astype('int')
        #dataset["TIPO_INCIDENCIA_REPARTO"] =dataset["TIPO_INCIDENCIA_REPARTO"].astype('int')
        dataset["CLIMA"] = dataset["CLIMA"].astype('int')
        
        model = XGBClassifier()
        
        model.load_model('D:\\CICLO12\\Tesis2\\TesisSoftware\\LogisticsSoftware\\Algortimos\\PesoModeloActual\\modelov4.json')
        print(model)
        print("Luego del model")
        print(dataset.columns)
        y_pred = model.predict(dataset)
        predictions = [round(value) for value in y_pred]
        
        valPrediction = predictions[0]
        sugerenciaPred = list(dictionarySugerencias.keys())[list(dictionarySugerencias.values()).index(predictions[0])]
        if (valPrediction==3):
            stringResponse = "PARA LAS PRÓXIMAS SOLICITUDES DEL CLIENTE {} CON DESTINO AL DISTRITO {} DE LA PROVINCIA {} DEL DEPARTAMENTO {} ES NECESARIO {}".format(str(cliente),str(distrito),str(provincia),str(departamento),sugerenciaPred)
        elif (valPrediction==0):
            stringResponse = "JUSTIFICAR INCUMPLIMIENTO. EL CLIENTE {} DEBE REFORZAR LA FUNCIÓN DE {} YA QUE EL INCIDENTE OBSEVADO SE DEBE A {}".format(str(cliente),sugerenciaPred,str(incidente))
        elif (valPrediction==1):
            stringResponse = "{} PARA COMPLEMENTAR LAS SOLICITUDES EN EL DISTRITO {} DE LA PROVINCIA {} DEL DEPARTAMENTO {}".format(sugerenciaPred,str(distrito),str(provincia),str(departamento))
        elif (valPrediction==4):
            stringResponse = "JUSTICIAR INCUMPLIMIENTO. PARA LAS PRÓXIMAS SOLICITUDES SE SUGIERE COORDINAR CON EL DESTINATARIO 'X' POR LA MODIFICACIÓN DE SU DIRECCIÓN"
        elif (valPrediction==2):
            #climas
            stringResponse = "{} EN EL DISTRITO DE {} DE LA PROVINCIA {} DEL DEPARTAMENTO {} POR LOS PROBLEMAS CLIMÁTICOS O SOCIALES".format(sugerenciaPred,str(distrito),str(provincia),str(departamento))
        elif (valPrediction==5):
            stringResponse = "DEBIDO A PROBLEMAS DE ACCESIBILIDAD A LA ZONA O ALTO ÍNDICE DE ROBO SE SUGIERE {} EN EL DISTRITO {} DE LA PROVINCIA {} DEL DEPARTAMENTO {}".format(sugerenciaPred,str(distrito),str(provincia),str(departamento))
        elif (valPrediction==6):
            # Incidencia del proveedor
            stringResponse = sugerenciaPred + " " + proveedor
        elif (valPrediction==7):
            # Caso OK
            stringResponse = sugerenciaPred
        
        file.file.close()
        
        return {"Sugerencia": stringResponse}
    

@router.post("/uploadfileGrupal/")
async def create_upload_file(file: UploadFile | None = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        dataset = pd.read_csv(file.file,sep=";")
        
        # Se crean agregan los parámetros de la longitud y longitud de los departamentos
        dataset["Latitud"]=0
        dataset["Longitud"]=0
        print(type(dataset))
        print(dataset.columns)
        
        departamentosnew = []
        provincias = []
        distritos = []
        clientes = []
        proveedores = []        
        incidencias = []
        
        for i in range(len(dataset)):
            loc = Nominatim(user_agent="GetLoc") 
            departamentosnew.append(dataset.loc[i,"DEPARTAMENTO"])
            distritos.append(dataset.loc[i,"DISTRITO"])
            provincias.append(dataset.loc[i,"PROVINCIA"])
            clientes.append(dataset.loc[i,"CLIENTE"])
            proveedores.append(dataset.loc[i,"PROVEEDOR DE TRANSPORTE"])
            incidencias.append(dataset.loc[i,"TIPO_INCIDENCIA_REPARTO"])
            #print(departamento)
            getLoc = loc.geocode(str(dataset.loc[i,"DEPARTAMENTO"])) 
            longitud =  getLoc.longitude
            latitud = getLoc.latitude
            dataset.loc[i,"Latitud"] = latitud
            dataset.loc[i,"Longitud"] = longitud
        
        dataset["TEMPERATURA"]=0
        dataset["HUMEDAD"]=0
        dataset["CLIMA"]= ""
        
        for i in dataset.index:
            fechaReparto = dataset.loc[i,"FECHA REPARTO"]
            my_ts = fechaReparto.split("/")
            dt = datetime.datetime(int(my_ts[2]), int(my_ts[1]), int(my_ts[0]))
            timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
            dateInit = str(timestamp+64800)
            dateInitUnix = dateInit[0:len(dateInit)-2]
            url = "http://history.openweathermap.org/data/2.5/history/city?lat={}&lon={}&type=hour&start={}&end={}&appid=b9c3fde5b6c1179bccc0b366a4d04fd0&units=metric".format(str(dataset.loc[0,"Latitud"]),str(dataset.loc[0,"Longitud"]),dateInitUnix,dateInitUnix)
            res = requests.get(url)
            data = res.json()
            temperatura = data["list"][0]["main"]["temp"]
            humedad = data["list"][0]["main"]["humidity"]
            clima = data["list"][0]["weather"][0]["main"]
            dataset.loc[i,"TEMPERATURA"] = temperatura
            dataset.loc[i,"HUMEDAD"] = humedad
            dataset.loc[i,"CLIMA"] = clima
        
        
        response = requests.get('http://datacrim.inei.gob.pe/csv_controller/index?desde=tematico&id=40001')
        df = pd.read_csv(io.StringIO(response.text), sep=',', header=None, quoting=csv.QUOTE_ALL)
        df[0] = df[0].astype('string')
        df[1] = df[1].astype('string')
        df[2] = df[2].astype('string')
        dataCrime = df.loc[(df[0]=="2021") & (df[1]!="NACIONAL")]
        val = list(dataCrime.loc[dataCrime[1]=="DEPARTAMENTO DE LIMA 2/"][2])[0]
        dataCrime.drop(dataCrime.loc[dataCrime[1]=="DEPARTAMENTO DE LIMA 2/"].index, inplace=True)
        dataCrime[2] = dataCrime[2].astype('float')
        indiceLima = int(dataCrime.loc[dataCrime[1]=="LIMA METROPOLITANA 1/"].index[0])
        indiceCallao = int(dataCrime.loc[dataCrime[1]=="PROVINCIA CONSTITUCIONAL DEL CALLAO"].index[0])
        dataCrime.loc[indiceCallao,1] = "LIMA"
        dataCrime.loc[indiceLima,1] = "LIMA"
        
        
        print("impresión de datacrime")
        print(dataCrime.columns)
        
        url = 'https://systems.inei.gob.pe/SIRTOD/app/consulta/getTableDataYear?indicador_listado=262432%2C262433%2C262429%2C420794%2C262428%2C420795&tipo_ubigeo=1&desde_anio=2020&hasta_anio=2020&ubigeo_listado=&idioma=ES'
        dataProblemaGeografico = list()
        dataProblemaGeograficoRequest = requests.get(url)
        dataProblemaGeografico = dataProblemaGeograficoRequest.json()
        
        url2 = "https://systems.inei.gob.pe/SIRTOD/app/consulta/getTableDataYear?indicador_listado=516860&tipo_ubigeo=1&desde_anio=2017&hasta_anio=2017&ubigeo_listado=&idioma=ES"
        dataProblemaAdultoMayor = list()
        dataProblemaAdultoMayorRequest = requests.get(url2)
        dataProblemaAdultoMayor = dataProblemaAdultoMayorRequest.json()
        
        url3 = "https://systems.inei.gob.pe/SIRTOD/app/consulta/getTableDataYear?indicador_listado=394842&tipo_ubigeo=1&desde_anio=2021&hasta_anio=2021&ubigeo_listado=&idioma=ES"
        dataAccidentesTransito = list()
        dataAccidentesTransitoRequest = requests.get(url3)
        dataAccidentesTransito = dataAccidentesTransitoRequest.json()
        
        listaDepartamentos = list()
        for i in dataProblemaGeografico:
            if (i["departamento"] not in listaDepartamentos):
                listaDepartamentos.append(i["departamento"])
                
        # Calculo de datos de problemas naturales
        listaProblemasGeograficoDatos = [0]*25
        for i in dataProblemaGeografico:
            if (i["departamento"] in listaDepartamentos):
                index = listaDepartamentos.index(i["departamento"])
                listaProblemasGeograficoDatos[index] = int(listaProblemasGeograficoDatos[index]) + int(i["dato"].replace(" ",""))
        
        # Calculo de datos de adultos mayores
        listaDatosAdultosMayores = [0]*25
        for i in dataProblemaAdultoMayor:
            if (i["departamento"] in listaDepartamentos):
                index = listaDepartamentos.index(i["departamento"])
                listaDatosAdultosMayores[index] = int(listaDatosAdultosMayores[index]) + int(i["dato"].replace(" ",""))
        
        # Calculo de datos de accidentes de transito
        listaDatosAccTransito = [0]*25
        for i in dataAccidentesTransito:
            if (i["departamento"] in listaDepartamentos):
                index = listaDepartamentos.index(i["departamento"])
                listaDatosAccTransito[index] = int(listaDatosAccTransito[index]) + int(i["dato"].replace(" ",""))
        
        listaDepartamentos = list(map(lambda x : normalize(x), listaDepartamentos))
        
        dataCrime.rename(columns = {0:'AÑO', 1:'DEPARTAMENTO',2:'INDICE_DELITOS'}, inplace = True)
        
        dataCrime["CANT_FENO_NAT"]=0
        dataCrime["CANT_ADULTOMAYOR"]=0
        dataCrime["CANT_ACC_TRANSITO"]=0
        
        for i in dataCrime.index:
            departamento = str(dataCrime.loc[i,"DEPARTAMENTO"])
            if (departamento in listaDepartamentos):
                index_departamento = listaDepartamentos.index(departamento)
                val_prob_geo = listaProblemasGeograficoDatos[index_departamento]
                val_cant_adul_mayor = listaDatosAdultosMayores[index_departamento]
                val_cant_acc_transito = listaDatosAccTransito[index_departamento]
                dataCrime.loc[i,"CANT_FENO_NAT"] = val_prob_geo
                dataCrime.loc[i,"CANT_ADULTOMAYOR"] = val_cant_adul_mayor
                dataCrime.loc[i,"CANT_ACC_TRANSITO"] = val_cant_acc_transito
        
        # Se crea nuevo dataframe
        newDataSet = pd.merge(dataset, dataCrime, how='inner', on = 'DEPARTAMENTO')
        
        # Se reemplza por el anterior
        dataset = newDataSet.copy()
        
        dataset["DIRECCION1"] = dataset["DIRECCION1"].str.upper()
        dataset["TIENE_AV"] = dataset.DIRECCION1.str.contains("AV|AVENIDA",regex=True,case=False)
        dataset["TIENE_JR"] = dataset.DIRECCION1.str.contains("JR|JIRON",regex=True,case=False)
        dataset["TIENE_CALLE"] = dataset.DIRECCION1.str.contains("CALLE",regex=True,case=False)
        
        dataset = dataset.drop(dataset[dataset.TIPO_INCIDENCIA_REPARTO == "COORDINADO"].index)
        dataset = dataset.drop(dataset[dataset.TIPO_INCIDENCIA_REPARTO == "REPROGRAMACION"].index)
        dataset = dataset.drop(dataset[dataset.TIPO_INCIDENCIA_REPARTO == "REEMBARQUE ENTREGA EN AGENCIA"].index)
        dataset = dataset.drop(dataset[dataset.TIPO_INCIDENCIA_REPARTO == "DESCONOCIDO/NO DA RAZÓN"].index)
        dataset = dataset.drop(dataset[dataset.TIPO_INCIDENCIA_REPARTO == "RECOJO EN OFICINA"].index)
        dataset = dataset.drop(dataset[dataset.TIPO_INCIDENCIA_REPARTO == "RECHAZADO"].index)
        dataset = dataset.drop(dataset[dataset.TIPO_INCIDENCIA_REPARTO == "DESPACHO ERRADO"].index)
        dataset["TIPO_INCIDENCIA_REPARTO"] = np.where(dataset["TIPO_INCIDENCIA_REPARTO"].isna(), 'OK', dataset["TIPO_INCIDENCIA_REPARTO"])
        dataset = dataset.drop(dataset[dataset.ESTADO_MANIFIESTO == "RECOGIDO"].index)
        dataset = dataset.drop(dataset[dataset.ESTADO_MANIFIESTO == "PENDIENTE"].index)
        dataset = dataset.drop(dataset[dataset.ESTADO_MANIFIESTO == "INFORMADO"].index)
        dataset = dataset.drop(dataset[dataset.ESTADO_MANIFIESTO == "DDV"].index)
        dataset = dataset.drop(dataset[dataset.DEPARTAMENTO.isnull()].index)
        
        dataset = dataset.drop(['GUIA'], axis=1)
        dataset = dataset.drop(['AÑO'], axis=1)
        dataset = dataset.drop(['DIRECCION1'], axis=1)
        dataset = dataset.drop(['N_MANIFIESTO'], axis=1)
        dataset = dataset.drop(['PROVINCIA'], axis=1)
        dataset = dataset.drop(['DISTRITO'], axis=1)
        dataset = dataset.drop(['NUMERO REPARTO'], axis=1)
        dataset = dataset.drop(['FECHA MANIFIESTO_VERIFICADO'], axis=1)
        dataset = dataset.drop(['ORIGEN_BASE'], axis=1)
        dataset = dataset.drop(['REMITENTE'], axis=1)
        dataset = dataset.drop(['FECHA_EMBARQUE'], axis=1)
        dataset = dataset.drop(['FORMA_CONF_ENTREGA'], axis=1)
        dataset = dataset.drop(['CONSIGNATARIO'], axis=1)
        dataset = dataset.drop(['DESTINO_BASE'], axis=1)
        dataset = dataset.drop(['REPRESENTANTE'], axis=1)
        dataset = dataset.drop(['DIRECCION2'], axis=1)
        dataset = dataset.drop(['FECHA_LLEGADA_PROYECT'], axis=1)
        dataset = dataset.drop(['FECHA_LLEGADA_REAL'], axis=1)
        dataset = dataset.drop(['FECHA MANIFIESTO_RECOGIDO'], axis=1)
        dataset = dataset.drop(['FECHA MANIFIESTO_INFORMADO'], axis=1)
        dataset = dataset.drop(['FECHA REPARTO'], axis=1)
        dataset = dataset.drop(['DESTINO'], axis=1)
        dataset = dataset.drop(['FECHA_COMPROMISO'], axis=1)
        dataset = dataset.drop(['FECHA_MANIFIESTO'], axis=1)
        dataset = dataset.drop(['RESP_REPARTO'], axis=1)
        dataset = dataset.drop(['FECHA_INCIDENCIA_REPARTO'], axis=1)
        dataset = dataset.drop(['FECHA_SALIDA_PROYECT'], axis=1)
        dataset = dataset.drop(['FECHA_GUIA'], axis=1)
        dataset = dataset.drop(['FECHA_ENTREGA'], axis=1)
        dataset = dataset.drop(['ORIGEN'], axis=1)
        dataset = dataset.drop(['GESTORA_SERVICIO'], axis=1)
        dataset = dataset.drop(['PROVEEDOR DE TRANSPORTE'], axis=1)
        dataset = dataset.drop(['CLIENTE'], axis=1)
        #dataset = dataset.drop(['count'], axis=1)
        dataset = dataset.drop(['ESTADO_MANIFIESTO'], axis=1)
        dataset = dataset.drop(['ESTADO_GUIA'], axis=1)
        dataset = dataset.drop(['TIPO_INCIDENCIA_REPARTO'], axis=1)
        
        moda = dataset['VIA'].mode()[0]
        dataset['VIA'] = dataset['VIA'].fillna(moda)

        moda = dataset['SERVICIO'].mode()[0]
        dataset['SERVICIO'] = dataset['SERVICIO'].fillna(moda)

        moda = dataset['DEPARTAMENTO'].mode()[0]
        dataset['DEPARTAMENTO'] = dataset['DEPARTAMENTO'].fillna(moda)

        dataset['TIENE_AV'] = np.where(dataset['TIENE_AV']==True, 1, dataset['TIENE_AV'])
        dataset['TIENE_AV'] = np.where(dataset['TIENE_AV']==False, 0, dataset['TIENE_AV'])
        dataset['TIENE_AV'] = np.where(dataset['TIENE_AV'].isna()==True, 0, dataset['TIENE_AV'])
        dataset['TIENE_JR'] = np.where(dataset['TIENE_JR']==True, 1, dataset['TIENE_JR'])
        dataset['TIENE_JR'] = np.where(dataset['TIENE_JR']==False, 0, dataset['TIENE_JR'])
        dataset['TIENE_JR'] = np.where(dataset['TIENE_JR'].isna()==True, 0, dataset['TIENE_JR'])
        dataset['TIENE_CALLE'] = np.where(dataset['TIENE_CALLE']==True, 1, dataset['TIENE_CALLE'])
        dataset['TIENE_CALLE'] = np.where(dataset['TIENE_CALLE']==False, 0, dataset['TIENE_CALLE'])
        dataset['TIENE_CALLE'] = np.where(dataset['TIENE_CALLE'].isna()==True, 0, dataset['TIENE_CALLE'])
        dataset['INCIDENCIA_MANIFIESTO'] = np.where(dataset['INCIDENCIA_MANIFIESTO'].isnull()==True, 'OK', dataset['INCIDENCIA_MANIFIESTO'])
        
        dataset['NO_TIENE_REF'] = 0
        dataset['NO_TIENE_REF'] = np.where((dataset['TIENE_AV']==0) & (dataset['TIENE_JR']==0) & (dataset['TIENE_CALLE']==0), 1, dataset['NO_TIENE_REF'])
        dataset["TIENE_AV"] = dataset["TIENE_AV"].astype('int')
        dataset["TIENE_JR"] =dataset["TIENE_JR"].astype('int')
        dataset["TIENE_CALLE"] =dataset["TIENE_CALLE"].astype('int')
        dataset["NO_TIENE_REF"] = dataset["NO_TIENE_REF"].astype('int')
        
        for i in dataset.index:
            departamento = str(dataset.loc[i,"DEPARTAMENTO"])
            servicio = str(dataset.loc[i,"SERVICIO"])
            via = str(dataset.loc[i,"VIA"])
            incidenciaMan = str(dataset.loc[i,"INCIDENCIA_MANIFIESTO"])
            #tipoIncidencia = str(dataset.loc[i,"TIPO_INCIDENCIA_REPARTO"])
            clima = str(dataset.loc[i,"CLIMA"])

            val_departamento = dictionaryDepartamentos[departamento]
            val_servicio = dictionaryServicios[servicio]
            val_via = dictionaryVias[via]
            val_incidenciaMan = dictionaryIncidenciaMan[incidenciaMan]
            #val_tipoIncidencia = dictionaryTipoIncidencia[tipoIncidencia]
            val_clima = dictionaryClimas[clima]

            dataset.loc[i,"SERVICIO"] = val_servicio
            dataset.loc[i,"DEPARTAMENTO"] = val_departamento
            dataset.loc[i,"VIA"] = val_via
            dataset.loc[i,"INCIDENCIA_MANIFIESTO"] = val_incidenciaMan
            #dataset.loc[i,"TIPO_INCIDENCIA_REPARTO"] = val_tipoIncidencia
            dataset.loc[i,"CLIMA"] = val_clima
        
        dataset["SERVICIO"] = dataset["SERVICIO"].astype('int')
        dataset["DEPARTAMENTO"] =dataset["DEPARTAMENTO"].astype('int')
        dataset["VIA"] =dataset["VIA"].astype('int')
        dataset["INCIDENCIA_MANIFIESTO"] = dataset["INCIDENCIA_MANIFIESTO"].astype('int')
        #dataset["TIPO_INCIDENCIA_REPARTO"] =dataset["TIPO_INCIDENCIA_REPARTO"].astype('int')
        dataset["CLIMA"] = dataset["CLIMA"].astype('int')
        
        model = XGBClassifier()
        
        model.load_model('D:\\CICLO12\\Tesis2\\TesisSoftware\\LogisticsSoftware\\Algortimos\\PesoModeloActual\\modelov4.json')
        print(model)
        print("Luego del model")
        print(dataset.columns)
        y_pred = model.predict(dataset)
        predictions = [round(value) for value in y_pred]
        
        # Se crea json de respuesta:
        dataResponse = newDataSet.copy()
        #departamentosnew = []
        #provincias = []
        #distritos = []
        #clientes = []
        #proveedores = []        
        #incidencias = []
        #dataResponse["SUGERENCIAS_STR"] = ""       
        
        j = 0
        for i in dataResponse.index:
            valPrediction = predictions[j]
            sugerenciaPred = list(dictionarySugerencias.keys())[list(dictionarySugerencias.values()).index(predictions[j])]
            if (valPrediction==3):
                stringResponse = "PARA LAS PRÓXIMAS SOLICITUDES DEL CLIENTE {} CON DESTINO AL DISTRITO {} DE LA PROVINCIA {} DEL DEPARTAMENTO {} ES NECESARIO {}".format(str(clientes[j]),str(distritos[j]),str(provincias[j]),str(departamentosnew[j]),sugerenciaPred)
            elif (valPrediction==0):
                stringResponse = "JUSTIFICAR INCUMPLIMIENTO. EL CLIENTE {} DEBE REFORZAR LA FUNCIÓN DE {} YA QUE EL INCIDENTE OBSEVADO SE DEBE A {}".format(str(clientes[j]),sugerenciaPred,str(incidencias[j]))
            elif (valPrediction==1):
                stringResponse = "{} PARA COMPLEMENTAR LAS SOLICITUDES EN EL DISTRITO {} DE LA PROVINCIA {} DEL DEPARTAMENTO {}".format(sugerenciaPred,str(distritos[j]),str(provincias[j]),str(departamentosnew[j]))
            elif (valPrediction==4):
                stringResponse = "JUSTICIAR INCUMPLIMIENTO. PARA LAS PRÓXIMAS SOLICITUDES SE SUGIERE COORDINAR CON EL DESTINATARIO 'X' POR LA MODIFICACIÓN DE SU DIRECCIÓN"
            elif (valPrediction==2):
                #climas
                stringResponse = "{} EN EL DISTRITO DE {} DE LA PROVINCIA {} DEL DEPARTAMENTO {} POR LOS PROBLEMAS CLIMÁTICOS O SOCIALES".format(sugerenciaPred,str(distritos[j]),str(provincias[j]),str(departamentosnew[j]))
            elif (valPrediction==5):
                stringResponse = "DEBIDO A PROBLEMAS DE ACCESIBILIDAD A LA ZONA O ALTO ÍNDICE DE ROBO SE SUGIERE {} EN EL DISTRITO {} DE LA PROVINCIA {} DEL DEPARTAMENTO {}".format(sugerenciaPred,str(distritos[j]),str(provincias[j]),str(departamentosnew[j]))
            elif (valPrediction==6):
                # Incidencia del proveedor
                stringResponse = sugerenciaPred + " " + str(proveedores[j])
            elif (valPrediction==7):
                # Caso OK
                stringResponse = sugerenciaPred
            j=j+1
            dataResponse.loc[i,"SUGERENCIAS_STR"] = stringResponse
        
        responseJson = dataResponse.to_json(orient='split')
        print(responseJson)
        file.file.close()
        
        return {"Sugerencia": responseJson}
