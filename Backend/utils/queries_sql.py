
QUERY_LISTAR_CANTIDAD_INCIDENCIAS = '''
    SELECT 
    SUM(case when sugerencia LIKE '%%OK%%' then 1 else 0 end) as cantidadOK,
    SUM(case when sugerencia NOT LIKE '%%OK%%' then 1 else 0 end) as cantidadIncidencias 
    from Solicitud s 
    INNER join Cliente c 
    on s.idCliente = c.id 
    INNER join Distrito di 
    on s.idDistritoDestino = di.id 
    INNER join Provincia pr 
    on di.idProvincia = pr.id 
    INNER join Departamento d 
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
    INNER join Cliente c 
    on s.idCliente = c.id 
    INNER join Distrito di 
    on s.idDistritoDestino = di.id 
    INNER join Provincia pr 
    on di.idProvincia = pr.id 
    INNER join Departamento d 
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
    INNER join Cliente c 
    on s.idCliente = c.id 
    INNER join Distrito di 
    on s.idDistritoDestino = di.id 
    INNER join Provincia pr 
    on di.idProvincia = pr.id 
    INNER join Departamento d 
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
    INNER join Cliente c 
    on s.idCliente = c.id 
    INNER join Distrito di 
    on s.idDistritoDestino = di.id 
    INNER join Provincia pr 
    on di.idProvincia = pr.id 
    INNER join Departamento d 
    on pr.idDepartamento = d.id 
    INNER JOIN Proveedor pro 
    on s.idProveedor = pro.id 
    where (s.fechaEntrega > {fecha_inicio} or {fecha_inicio} IS NULL) and 
    (s.fechaEntrega < {fecha_fin} or {fecha_fin} IS NULL) and 
    (c.razonSocial = {cliente} or {cliente} IS NULL) and 
    (d.nombreDepartamento = {departamento} or {departamento} IS NULL) and 
    s.tipoIncidenciaReparto = "FALLAS MECANICAS EN REPARTO" and 
    (pro.razonSocial = {proveedor} or {proveedor} IS NULL)
'''