# core/db.py
from pymongo import MongoClient
import os

# URI de conexión (puedes usar la de MongoDB Atlas o local)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# Cliente y base de datos
client = MongoClient(MONGO_URI)
db = client["gestor_passwords"]          # Nombre de la base de datos
collection = db["passwords"]             # Nombre de la colección

# Crear índice único en 'password' para evitar duplicados (opcional)
collection.create_index("password", unique=True)