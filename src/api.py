from fastapi import FastAPI, Query
from src.core.generador import generar_password

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando 🚀"}

@app.get("/generar")
def generar(
    longitud: int = Query(16, ge=8, le=128, description="Longitud de la contraseña"),
    incluir_mayus: bool = Query(True, description="Incluir mayúsculas"),
    incluir_minus: bool = Query(True, description="Incluir minúsculas"),
    incluir_numeros: bool = Query(True, description="Incluir números"),
    incluir_simbolos: bool = Query(True, description="Incluir símbolos"),
    usuario: str = Query("", description="Nombre del usuario para evitarlo en la contraseña")
):
    password = generar_password(
        longitud=longitud,
        incluir_mayus=incluir_mayus,
        incluir_minus=incluir_minus,
        incluir_numeros=incluir_numeros,
        incluir_simbolos=incluir_simbolos,
        usuario=usuario
    )
    return {"password": password}