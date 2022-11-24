INSERT INTO Cliente (id, razonSocial) VALUES ('1', 'SWISSJUST LATINOAMERICA S.A. SUCURSAL PERU');
INSERT INTO Cliente (id, razonSocial) VALUES ('2', 'DINET S.A.');
INSERT INTO Cliente (id, razonSocial) VALUES ('3', 'HINODE PERU S.A.C.');
INSERT INTO Cliente (id, razonSocial) VALUES ('4', 'NATURA COSMETICOS S.A.');

INSERT INTO Departamento (id, nombreDepartamento) VALUES ('1', 'CAJAMARCA');
INSERT INTO Departamento (id, nombreDepartamento) VALUES ('2', 'LA LIBERTAD');
INSERT INTO Departamento (id, nombreDepartamento) VALUES ('3', 'JUNIN');
INSERT INTO Departamento (id, nombreDepartamento) VALUES ('4', 'UCAYALI');
INSERT INTO Departamento (id, nombreDepartamento) VALUES ('5', 'SAN MARTIN');

INSERT INTO Provincia (id, nombreProvincia, idDepartamento) VALUES ('1', 'JAEN', '1');
INSERT INTO Provincia (id, nombreProvincia, idDepartamento) VALUES ('2', 'TRUJILLO', '2');
INSERT INTO Provincia (id, nombreProvincia, idDepartamento) VALUES ('3', 'HUANCAYO', '3');
INSERT INTO Provincia (id, nombreProvincia, idDepartamento) VALUES ('4', 'CORONEL PORTILLO', '4');
INSERT INTO Provincia (id, nombreProvincia, idDepartamento) VALUES ('5', 'TOCACHE', '5');

INSERT INTO Distrito (id, nombreDistrito, idProvincia) VALUES ('1', 'JAEN', '1');
INSERT INTO Distrito (id, nombreDistrito, idProvincia) VALUES ('2', 'TRUJILLO', '2');
INSERT INTO Distrito (id, nombreDistrito, idProvincia) VALUES ('3', 'HUANCAYO', '3');
INSERT INTO Distrito (id, nombreDistrito, idProvincia) VALUES ('4', 'CALLERIA', '4');
INSERT INTO Distrito (id, nombreDistrito, idProvincia) VALUES ('5', 'UCHIZA', '5');

INSERT INTO Proveedor (id, razonSocial, idDistrito) VALUES ('1', 'MOVIL BUS S.A.C', '1');
INSERT INTO Proveedor (id, razonSocial, idDistrito) VALUES ('2', 'ANDES EXPRESS S.A.C.', '2');
INSERT INTO Proveedor (id, razonSocial, idDistrito) VALUES ('3', 'MARYFER CARGO S.A.C', '3');
INSERT INTO Proveedor (id, razonSocial, idDistrito) VALUES ('4', 'TRANSPORTE HUGAMOR EIRL', '4');
INSERT INTO Proveedor (id, razonSocial, idDistrito) VALUES ('5', 'EMPRESA DE TRANSPORTES TURISMO LAS BRIZAS SOCIEDAD ANONIMA', '5');