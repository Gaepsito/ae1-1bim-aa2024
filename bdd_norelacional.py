### Paso 1: Crear la base de datos y las colecciones

#### Script para crear la base de datos y las colecciones en MongoDB

from pymongo import MongoClient

# Conectar a MongoDB (se crea si no existe)
cliente = MongoClient('mongodb://localhost:27017/')
db = cliente['base_datos_entidades']

# Crear colección para Clínicas Particulares
clinicas_particulares = db['clinicas_particulares']

# Crear colección para Parques Recreativos
parques_recreativos = db['parques_recreativos']


### Paso 2: Insertar datos en las colecciones

#### Script para insertar datos en las colecciones
from pymongo import MongoClient

# Conectar a MongoDB
cliente = MongoClient('mongodb://localhost:27017/')
db = cliente['base_datos_entidades']

# Insertar datos en Clínicas Particulares
clinicas_particulares = db['clinicas_particulares']
clinicas_particulares.insert_many([
    {
        "nombre": "Clinica Salud",
        "direccion": "Avenida Principal 456",
        "telefono": "987-654-3210",
        "especialidades": ["Dermatología", "Neurología"]
    },
    {
        "nombre": "Clinica Bienestar",
        "direccion": "Calle Secundaria 789",
        "telefono": "123-456-7890",
        "especialidades": ["Pediatría", "Cardiología"]
    }
])

# Insertar datos en Parques Recreativos
parques_recreativos = db['parques_recreativos']
parques_recreativos.insert_many([
    {
        "nombre": "Parque Verde",
        "ubicacion": "Calle Verde 789",
        "actividades": ["Senderismo", "Ciclismo"]
    },
    {
        "nombre": "Parque Azul",
        "ubicacion": "Avenida Azul 123",
        "actividades": ["Picnic", "Juegos"]
    }
])


### Paso 3: Consultar datos de las colecciones

#### Script para consultar datos de las colecciones

from pymongo import MongoClient

# Conectar a MongoDB
cliente = MongoClient('mongodb://localhost:27017/')
db = cliente['base_datos_entidades']

# Consultar datos de Clínicas Particulares
clinicas_particulares = db['clinicas_particulares']
for clinica in clinicas_particulares.find():
    print("Clínica Particular:", clinica)

# Consultar datos de Parques Recreativos
parques_recreativos = db['parques_recreativos']
for parque in parques_recreativos.find():
    print("Parque Recreativo:", parque)