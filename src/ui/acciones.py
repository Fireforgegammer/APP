from core.storage import cargar_passwords, agregar_password, eliminar_password_por_valor
from core.evaluador import evaluar_password
from core.generador import generar_passwords

# -------------------------
# Funciones de lectura
# -------------------------
def obtener_passwords(tipo: str = "todo", cantidad: int = 5):
    """
    Devuelve contraseñas filtradas:
    - 'ultimas': últimas N contraseñas
    - 'sin_sitio': sin sitio asignado
    - 'usadas': con sitio asignado
    - 'todo': todas
    """
    passwords = cargar_passwords()

    if tipo == "ultimas":
        lista = passwords[-cantidad:]
    elif tipo == "sin_sitio":
        lista = [p for p in passwords if p.get("sitio") is None]
    elif tipo == "usadas":
        lista = [p for p in passwords if p.get("sitio") is not None]
    else:
        lista = passwords

    return [
        {
            "sitio": p.get("sitio") or "Sin asignar",
            "password": p["password"],
            "nivel": evaluar_password(p["password"])
        } for p in lista
    ]

# -------------------------
# Funciones de modificación
# -------------------------
def anadir_sitio(sitio: str, index: int):
    """
    Asigna un sitio a una contraseña sin asignar por índice.
    """
    passwords = cargar_passwords()
    sin_sitio = [p for p in passwords if p.get("sitio") is None]

    if not sin_sitio or index < 0 or index >= len(sin_sitio):
        return False

    seleccionada = sin_sitio[index]
    for p in passwords:
        if p == seleccionada:
            p["sitio"] = sitio
            break

    # Guardamos actualizando MongoDB individualmente
    for p in passwords:
        agregar_password(p)  # insertará solo nuevas, duplicadas son ignoradas
    return True

def eliminar_password(index: int):
    """
    Elimina contraseña por índice de la lista completa.
    """
    passwords = cargar_passwords()
    if index < 0 or index >= len(passwords):
        return None

    eliminada = passwords.pop(index)
    eliminar_password_por_valor(eliminada["password"])
    return eliminada

def buscar_password(query: str):
    """
    Busca contraseñas que contengan el texto en el sitio.
    """
    passwords = cargar_passwords()
    encontrados = [
        p for p in passwords
        if p.get("sitio") and query.lower() in p["sitio"].lower()
    ]
    return [
        {
            "sitio": p.get("sitio") or "Sin asignar",
            "password": p["password"],
            "nivel": evaluar_password(p["password"])
        } for p in encontrados
    ]

# -------------------------
# Funciones de generación
# -------------------------
def generar_passwords_backend(config, longitud: int, cantidad: int):
    """
    Genera contraseñas y las guarda en MongoDB de forma incremental.
    """
    nuevas_passwords = generar_passwords(config, longitud, cantidad)
    for p in nuevas_passwords:
        agregar_password(p)
    return nuevas_passwords

def guardar_password_manual(password: str):
    """
    Guarda contraseña proporcionada manualmente por el usuario.
    """
    obj = {"sitio": None, "password": password}
    agregar_password(obj)
    return obj

# -------------------------
# Funciones de ayuda
# -------------------------
def evaluar_lista_passwords(passwords):
    """
    Devuelve la lista con nivel de seguridad agregado.
    """
    return [
        {
            "sitio": p.get("sitio") or "Sin asignar",
            "password": p["password"],
            "nivel": evaluar_password(p["password"])
        } for p in passwords
    ]