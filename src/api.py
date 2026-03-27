from fastapi import FastAPI, Query
from ui import acciones, menu

app = FastAPI(title="Gestor de Contraseñas Multiplataforma 🚀")

# -------------------------
# Menú
# -------------------------
@app.get("/menu")
def obtener_menu_api():
    """
    Devuelve el menú principal.
    """
    return {
        "menu_principal": menu.obtener_menu(),
        "submenu_generar": menu.obtener_submenu_generar()
    }

# -------------------------
# Generación de contraseñas
# -------------------------
@app.post("/generar/aleatoria")
def generar_aleatoria(
    longitud: int = Query(..., ge=4, le=108),
    incluir_mayus: bool = Query(True),
    incluir_minus: bool = Query(True),
    incluir_numeros: bool = Query(True),
    incluir_simbolos: bool = Query(True),
    cantidad: int = Query(1, ge=1)
):
    config = {
        "minus": incluir_minus,
        "mayus": incluir_mayus,
        "numeros": incluir_numeros,
        "simbolos": incluir_simbolos
    }
    nuevas = acciones.generar_passwords_backend(config, longitud, cantidad)
    return {"contraseñas": nuevas}

@app.post("/generar/manual")
def generar_manual(password: str):
    """
    Guarda contraseña proporcionada por el usuario.
    """
    guardada = acciones.guardar_password_manual(password)
    return {"contraseña_guardada": guardada}

# -------------------------
# Ver contraseñas
# -------------------------
@app.get("/ver")
def ver_passwords(tipo: str = Query("todo"), cantidad: int = Query(5)):
    """
    Devuelve contraseñas filtradas:
    - todo
    - ultimas
    - sin_sitio
    - usadas
    """
    lista = acciones.obtener_passwords(tipo=tipo, cantidad=cantidad)
    return {"contraseñas": lista}

# -------------------------
# Añadir sitio
# -------------------------
@app.post("/anadir_sitio")
def anadir_sitio(sitio: str, index: int):
    """
    Asigna un sitio a una contraseña sin asignar.
    """
    exito = acciones.anadir_sitio(sitio, index)
    return {"exito": exito}

# -------------------------
# Eliminar contraseña
# -------------------------
@app.delete("/eliminar")
def eliminar(index: int):
    """
    Elimina contraseña por índice.
    """
    eliminada = acciones.eliminar_password(index)
    if eliminada:
        return {"eliminada": eliminada}
    return {"error": "Índice inválido"}

# -------------------------
# Buscar contraseña
# -------------------------
@app.get("/buscar")
def buscar(query: str):
    """
    Busca contraseñas por sitio.
    """
    encontrados = acciones.buscar_password(query)
    return {"resultados": encontrados}