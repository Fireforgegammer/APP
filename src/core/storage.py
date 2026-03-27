# core/storage.py
from .db import collection
from pymongo.errors import DuplicateKeyError

def cargar_passwords():
    """
    Devuelve todas las contraseñas desde MongoDB.
    """
    docs = list(collection.find({}, {"_id": 0}))  # omitimos _id
    return docs

def guardar_passwords(passwords):
    """
    Sobrescribe todas las contraseñas en MongoDB.
    Útil si quieres reiniciar la colección.
    """
    # Borramos todas
    collection.delete_many({})
    # Insertamos las nuevas
    if passwords:
        try:
            collection.insert_many(passwords, ordered=False)
        except DuplicateKeyError:
            # Ignoramos duplicados si existen
            pass

def agregar_password(password_obj):
    """
    Agrega una sola contraseña a la colección.
    password_obj = {"sitio": ..., "password": ...}
    """
    try:
        collection.insert_one(password_obj)
        return True
    except DuplicateKeyError:
        return False

def eliminar_password_por_valor(password):
    """
    Elimina una contraseña específica por valor.
    """
    result = collection.delete_one({"password": password})
    return result.deleted_count > 0