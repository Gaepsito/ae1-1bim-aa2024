<<<<<<< HEAD
### Paso 1: Creacion de la BDD y las tablas

#### Script para crear la base de datos y las tablas en SQLite

import sqlite3

# Conectar a la base de datos (se crea si no existe)
conexion = sqlite3.connect('base_datos_entidades.db')
cursor = conexion.cursor()

# Crear tabla para Clínicas Privadas
cursor.execute('''
CREATE TABLE IF NOT EXISTS ClinicasPrivadas (
    id_clinica INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_clinica TEXT,
    direccion_clinica TEXT,
    telefono_clinica TEXT,
    email_clinica TEXT,
    especialidades_clinica TEXT,
    doctores_clinica INTEGER,
    enfermeras_clinica INTEGER
)
''')

# Crear tabla para Parques de Recreo
cursor.execute('''
CREATE TABLE IF NOT EXISTS ParquesRecreo (
    id_parque INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_parque TEXT,
    ubicacion_parque TEXT,
    apertura_parque TEXT,
    cierre_parque TEXT,
    actividades_parque TEXT
)
''')

# Confirmar cambios y cerrar conexión
conexion.commit()
print("Exito!!")
conexion.close()
### Paso 2: Insertar datos en las tablas

#### Script para insertar datos en las tablas

import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect('base_datos_entidades.db')
cursor = conexion.cursor()

# Insertar datos en Clínicas Privadas
cursor.execute('''
INSERT INTO ClinicasPrivadas (nombre_clinica, direccion_clinica, telefono_clinica, email_clinica, especialidades_clinica, doctores_clinica, enfermeras_clinica)
VALUES ('Clinica Salud', 'Avenida Principal 456', '987-654-3210', 'info@clinicasalud.com', 'Dermatología, Neurología', 15, 25)
''')

# Insertar datos en Parques de Recreo
cursor.execute('''
INSERT INTO ParquesRecreo (nombre_parque, ubicacion_parque, apertura_parque, cierre_parque, actividades_parque)
VALUES ('Parque Verde', 'Calle Verde 789', '07:00', '19:00', 'Senderismo, Ciclismo')
''')

# Confirmar cambios y cerrar conexión
conexion.commit()
conexion.close()


### Paso 3: Consultar datos de las tablas

#### Script para consultar datos de las tablas
import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect('base_datos_entidades.db')
cursor = conexion.cursor()

# Consultar datos de Clínicas Privadas
cursor.execute('SELECT * FROM ClinicasPrivadas')
clinicas = cursor.fetchall()
print("Clínicas Privadas:")
for clinica in clinicas:
    print(clinica)

# Consultar datos de Parques de Recreo
cursor.execute('SELECT * FROM ParquesRecreo')
parques = cursor.fetchall()
print("\nParques de Recreo:")
for parque in parques:
    print(parque)

# Cerrar conexión
conexion.commit()
=======
### Paso 1: Creacion de la BDD y las tablas

#### Script para crear la base de datos y las tablas en SQLite

import sqlite3

# Conectar a la base de datos (se crea si no existe)
conexion = sqlite3.connect('base_datos_entidades.db')
cursor = conexion.cursor()

# Crear tabla para Clínicas Privadas
cursor.execute('''
CREATE TABLE IF NOT EXISTS ClinicasPrivadas (
    id_clinica INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_clinica TEXT,
    direccion_clinica TEXT,
    telefono_clinica TEXT,
    email_clinica TEXT,
    especialidades_clinica TEXT,
    doctores_clinica INTEGER,
    enfermeras_clinica INTEGER
)
''')

# Crear tabla para Parques de Recreo
cursor.execute('''
CREATE TABLE IF NOT EXISTS ParquesRecreo (
    id_parque INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_parque TEXT,
    ubicacion_parque TEXT,
    apertura_parque TEXT,
    cierre_parque TEXT,
    actividades_parque TEXT
)
''')

# Confirmar cambios y cerrar conexión
conexion.commit()
print("Exito!!")
conexion.close()
### Paso 2: Insertar datos en las tablas

#### Script para insertar datos en las tablas

import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect('base_datos_entidades.db')
cursor = conexion.cursor()

# Insertar datos en Clínicas Privadas
cursor.execute('''
INSERT INTO ClinicasPrivadas (nombre_clinica, direccion_clinica, telefono_clinica, email_clinica, especialidades_clinica, doctores_clinica, enfermeras_clinica)
VALUES ('Clinica Salud', 'Avenida Principal 456', '987-654-3210', 'info@clinicasalud.com', 'Dermatología, Neurología', 15, 25)
''')

# Insertar datos en Parques de Recreo
cursor.execute('''
INSERT INTO ParquesRecreo (nombre_parque, ubicacion_parque, apertura_parque, cierre_parque, actividades_parque)
VALUES ('Parque Verde', 'Calle Verde 789', '07:00', '19:00', 'Senderismo, Ciclismo')
''')

# Confirmar cambios y cerrar conexión
conexion.commit()
conexion.close()


### Paso 3: Consultar datos de las tablas

#### Script para consultar datos de las tablas
import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect('base_datos_entidades.db')
cursor = conexion.cursor()

# Consultar datos de Clínicas Privadas
cursor.execute('SELECT * FROM ClinicasPrivadas')
clinicas = cursor.fetchall()
print("Clínicas Privadas:")
for clinica in clinicas:
    print(clinica)

# Consultar datos de Parques de Recreo
cursor.execute('SELECT * FROM ParquesRecreo')
parques = cursor.fetchall()
print("\nParques de Recreo:")
for parque in parques:
    print(parque)

# Cerrar conexión
conexion.commit()
>>>>>>> 16b8412604c0b410ead7d814a64b489d5212ebff
conexion.close()