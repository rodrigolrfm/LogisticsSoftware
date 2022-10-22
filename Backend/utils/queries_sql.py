QUERY_INSERT_INSCRIPCION = '''
    INSERT INTO Inscripcion (idSolicitante, idSede, idPropietario, idEstadoSolicitud, fechaRegistro, activo)
    VALUES ('{id_solicitante}', '{id_sede}', '{id_propietario}', '{id_estado_solicitud}', '{fecha_registro}', 1)
'''

QUERY_UPDATE_INSCRIPCION = '''
    UPDATE Inscripcion 
    SET idSolicitante='{id_solicitante}',
        idSede='{id_sede}',
        idPropietario='{id_propietario}',
        idEstadoSolicitud='{id_estado_solicitud}',
        observacionesUrl={observaciones_url}
    WHERE id={id_inscripcion}
'''

QUERY_INSERT_BIEN = '''
    INSERT INTO Bien (idInscripcion, nombre, sumilla, descripcion,
                    idClasificacionBien, idUbicacion, idTipoBien, idEstadoBien, titulo,
                    fabricante, modelo, marca, idMaterial, nombreCientifico,
                    idDivision, idCultura, filiacionCultural, autoria,
                    estilo, serie, procedencia, idPeriodoHistorico, datacion,
                    idEpocaGeologica, materialSoporte, materialSecundario,
                    tecnicasManufactura, tecnicasDecoracion,
                    tecnicasAcabado, 
                    idTipoFosilizacion, tipoMuestra, idEstadoIntegridad,
                    idEstadoConservacion, descripcionTecnica, detalleConservacion,
                    unidad, alto, largo, ancho, diametro, espesor,
                    fondo, bibliografia, observacionesTecnicas,
                    idAreaGeografica, capa, sector,
                    elementosAdicionales, materialesAdicionales, 
                    informacionComplementaria,informacionTecnicaComp,excavado, idUnidadDimensiones, activo)
    VALUES ({id_inscripcion}, {nombre_bien}, {sumilla_bien}, {descripcion_bien},
            {id_clasificacion_bien}, {id_ubicacion}, {id_tipo_bien}, {id_estado_bien},
            {titulo}, {fabricante}, {modelo}, {marca},
            {id_material}, {nombre_cientifico}, {id_division}, 
            {id_cultura}, {filiacion_cultural}, {autoria},
            {estilo}, {serie}, {procedencia}, {id_periodo_historico},
            {datacion}, {id_epoca_gelogica}, {material_soporte},
            {material_secundario}, {tecnicas_manufactura}, {tecnicas_decoracion},
            {tecnicas_acabado}, {id_tipo_fosilizacion},
            {tipo_muestra}, {id_estado_integridad}, {id_estado_conservacion},
            {descripcion_tecnica}, {detalle_conservacion}, {unidad},
            {alto}, {largo}, {ancho}, {diametro}, {espesor},
            {fondo}, {bibliografia}, {obs_tecnicas}, {id_area_geografica},
            {capa}, {sector}, {elementos_adicionales},
            {materiales_adicionales}, {info_complementaria}, {info_tecnica_comp}, {excavado}, {id_unidad_dim}, 1)
'''

QUERY_UPDATE_BIEN = '''
    UPDATE Bien
    SET nombre={nombre_bien}, 
        descripcion={descripcion_bien},
        sumilla={sumilla_bien}, 
        idClasificacionBien={id_clasificacion_bien}, 
        idUbicacion={id_ubicacion},
        idTipoBien={id_tipo_bien}, 
        titulo={titulo}, 
        fabricante={fabricante},
        modelo={modelo}, 
        marca={marca}, 
        idMaterial={id_material}, 
        nombreCientifico={nombre_cientifico},
        idDivision={id_division},
        idCultura={id_cultura}, 
        filiacionCultural={filiacion_cultural},
        autoria={autoria}, 
        estilo={estilo}, 
        serie={serie}, 
        procedencia={procedencia},
        idPeriodoHistorico={id_periodo_historico}, 
        datacion={datacion},
        idEpocaGeologica={id_epoca_gelogica}, 
        materialSoporte={material_soporte},
        materialSecundario={material_secundario}, 
        tecnicasManufactura={tecnicas_manufactura},
        tecnicasDecoracion={tecnicas_decoracion}, 
        tecnicasAcabado={tecnicas_acabado},
        idTipoFosilizacion={id_tipo_fosilizacion},
        tipoMuestra={tipo_muestra}, 
        idEstadoIntegridad={id_estado_integridad},
        idEstadoConservacion={id_estado_conservacion}, 
        descripcionTecnica={descripcion_tecnica},
        detalleConservacion={detalle_conservacion}, 
        idUnidadDimensiones={id_unidad_dim},
        alto={alto}, 
        largo={largo}, 
        ancho={ancho}, 
        diametro={diametro},
        espesor={espesor}, 
        fondo={fondo},
        bibliografia={bibliografia},
        observacionesTecnicas={obs_tecnicas},
        idAreaGeografica={id_area_geografica}, 
        capa={capa}, 
        unidad={unidad},
        sector={sector},
        elementosAdicionales={elementos_adicionales}, 
        materialesAdicionales={materiales_adicionales},
        informacionComplementaria={informacion_complementaria},
        informacionTecnicaComp={informacion_tecnica_complementaria}, 
        excavado={excavado},
        idEstadoBien={id_estado_bien}
    WHERE id={id_bien}
'''

QUERY_DELETE_BIENES = '''
    UPDATE Bien
    SET activo=0 
    WHERE id not in {id_bienes} AND idInscripcion='{id_inscripcion}'
'''

QUERY_DELETE_BIEN = '''
    UPDATE Bien
    SET activo=0
    WHERE id={id_bien}
'''

QUERY_LISTAR_BIENES_BY_QUERY = '''
    SELECT B.*, 
            I.fechaRegistro,
            EB.nombre as estadoNombre,
            CB.nombre as clasificacionNombre,
            TB.nombre as tipoBienNombre
    FROM Bien B
    LEFT JOIN Inscripcion I ON I.id=B.idInscripcion
    LEFT JOIN EstadoBien EB ON EB.id=B.idEstadoBien
    LEFT JOIN ClasificacionBien CB ON CB.id=B.idClasificacionBien
    LEFT JOIN TipoBien TB ON TB.id=B.idTipoBien
    WHERE (B.nombre LIKE '%%{nombre_bien}%%' OR {nombre_bien_null} IS NULL) AND
            (B.idEstadoBien={id_estado_bien} OR {id_estado_bien} IS NULL) AND
            (B.idClasificacionBien={id_clasificacion_bien} OR {id_clasificacion_bien} IS NULL) AND
            (B.idTipoBien={id_tipo_bien} OR {id_tipo_bien} IS NULL) AND
            (I.fechaRegistro > {fecha_inicio} OR {fecha_inicio} IS NULL) AND
            (I.fechaRegistro < {fecha_fin} OR {fecha_fin} IS NULL) AND 
            (B.activo=1) AND (I.activo=1 OR B.idInscripcion IS NULL)
'''

QUERY_INSERT_ARCHIVO = '''
    INSERT INTO Archivo (idBien, nombre, url, idOrientacion, activo)
    VALUES ('{id_bien}', '{nombre_archivo}', '{url_archivo}', '{id_orientacion}', 1)
'''

QUERY_UPDATE_ARCHIVO = '''
    UPDATE Archivo
    SET nombre='{nombre_archivo}', url='{url_archivo}',
        idOrientacion='{id_orientacion}'
    WHERE id={id_archivo}
'''

QUERY_UPDATE_ARCHIVO_NOT_IMAGE = '''
    UPDATE Archivo
    SET idOrientacion='{id_orientacion}'
    WHERE id={id_archivo}
'''

QUERY_DELETE_ARCHIVOS = '''
    UPDATE Archivo
    SET activo=0 
    WHERE id not in {id_archivos} AND idBien='{id_bien}'
'''

QUERY_DELETE_ARCHIVO_BY_BIEN = '''
    UPDATE Archivo
    SET activo=0
    WHERE idBien={id_bien}
'''
