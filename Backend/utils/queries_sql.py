
QUERY_LISTAR_CANTIDAD_INCIDENCIAS = '''
    SELECT 
    SUM(case when tipoIncidenciaReparto is null then 1 else 0 end) as cantidadOK,
    SUM(case when tipoIncidenciaReparto is not null then 1 else 0 end) as cantidadIncidencias 
    from Solicitud s 
    LEFT join Cliente c 
    on s.idCliente = c.id 
    LEFT join Distrito di 
    on s.idDistritoDestino = di.id 
    LEFT join Provincia pr 
    on di.idProvincia = pr.id 
    LEFT join Departamento d 
    on pr.idDepartamento = d.id 
    where (s.fechaEntrega > {fecha_inicio} or {fecha_inicio} IS NULL) and 
    (s.fechaEntrega < {fecha_fin} or {fecha_fin} IS NULL) and 
    (c.razonSocial = {cliente} or {cliente} IS NULL) and 
    (d.nombreDepartamento = {departamento} or {departamento} IS NULL) 
'''


QUERY_LISTAR_CANTIDAD_INCIDENCIAS_POR_TIPO = '''
    SELECT 
    s.tipoIncidenciaReparto as nombre,  
    COUNT(*) as cant 
    from Solicitud s 
    LEFT join Cliente c 
    on s.idCliente = c.id 
    LEFT join Distrito di 
    on s.idDistritoDestino = di.id 
    LEFT join Provincia pr 
    on di.idProvincia = pr.id 
    LEFT join Departamento d 
    on pr.idDepartamento = d.id 
    where (s.fechaEntrega > {fecha_inicio} or {fecha_inicio} IS NULL) and 
    (s.fechaEntrega < {fecha_fin} or {fecha_fin} IS NULL) and 
    (c.razonSocial = {cliente} or {cliente} IS NULL) and 
    (d.nombreDepartamento = {departamento} or {departamento} IS NULL) and
    s.tipoIncidenciaReparto IS NOT NULL and s.tipoIncidenciaReparto <> "" 
    GROUP BY s.tipoIncidenciaReparto
'''



QUERY_LISTAR_CANTIDAD_INCIDENCIAS_POR_FALLO_MECANICO = '''
    SELECT 
    COUNT(*) 
    from Solicitud s 
    LEFT join Cliente c 
    on s.idCliente = c.id 
    LEFT join Distrito di 
    on s.idDistritoDestino = di.id 
    LEFT join Provincia pr 
    on di.idProvincia = pr.id 
    LEFT join Departamento d 
    on pr.idDepartamento = d.id 
    where (s.fechaEntrega > {fecha_inicio} or {fecha_inicio} IS NULL) and 
    (s.fechaEntrega < {fecha_fin} or {fecha_fin} IS NULL) and 
    (c.razonSocial = {cliente} or {cliente} IS NULL) and 
    (d.nombreDepartamento = {departamento} or {departamento} IS NULL) and
    s.tipoIncidenciaReparto = "FALLAS MECANICAS EN REPARTO" 
'''

QUERY_LISTAR_CANTIDAD_INCIDENCIAS_POR_FALLO_MECANICO_POR_PROVEEDOR = '''
    SELECT 
    COUNT(*) 
    from Solicitud s 
    LEFT join Cliente c 
    on s.idCliente = c.id 
    LEFT join Distrito di 
    on s.idDistritoDestino = di.id 
    LEFT join Provincia pr 
    on di.idProvincia = pr.id 
    LEFT join Departamento d 
    on pr.idDepartamento = d.id 
    LEFT JOIN Proveedor pro 
    on s.idProveedor = pro.id 
    where (s.fechaEntrega > {fecha_inicio} or {fecha_inicio} IS NULL) and 
    (s.fechaEntrega < {fecha_fin} or {fecha_fin} IS NULL) and 
    (c.razonSocial = {cliente} or {cliente} IS NULL) and 
    (d.nombreDepartamento = {departamento} or {departamento} IS NULL) and 
    s.tipoIncidenciaReparto = "FALLAS MECANICAS EN REPARTO" and 
    (pro.razonSocial = {proveedor} or {proveedor} IS NULL)
'''


QUERY_LISTAR_CANTIDAD_INCIDENCIAS_POR_MES = '''
    SELECT 
    SUM(case when MONTH(s.fechaEntrega) = 1 then 1 else 0 end) as enero, 
    SUM(case when MONTH(s.fechaEntrega) = 2 then 1 else 0 end) as febrero,
    SUM(case when MONTH(s.fechaEntrega) = 3 then 1 else 0 end) as marzo,
    SUM(case when MONTH(s.fechaEntrega) = 4 then 1 else 0 end) as abril, 
    SUM(case when MONTH(s.fechaEntrega) = 5 then 1 else 0 end) as mayo,
    SUM(case when MONTH(s.fechaEntrega) = 6 then 1 else 0 end) as junio, 
    SUM(case when MONTH(s.fechaEntrega) = 7 then 1 else 0 end) as julio, 
    SUM(case when MONTH(s.fechaEntrega) = 8 then 1 else 0 end) as agosto, 
    SUM(case when MONTH(s.fechaEntrega) = 9 then 1 else 0 end) as septiembre, 
    SUM(case when MONTH(s.fechaEntrega) = 10 then 1 else 0 end) as octubre, 
    SUM(case when MONTH(s.fechaEntrega) = 11 then 1 else 0 end) as noviembre, 
    SUM(case when MONTH(s.fechaEntrega) = 12 then 1 else 0 end) as diciembre 
    from Solicitud s 
    where YEAR(s.fechaEntrega) = {anho}
'''