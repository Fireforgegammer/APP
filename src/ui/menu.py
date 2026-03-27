# ui/menu.py

def obtener_menu():
    """
    Devuelve la estructura del menú principal.
    Cada opción es un diccionario con:
        - id: número de opción
        - titulo: texto para mostrar en la UI
        - descripcion: opcional, más información
    """
    menu = [
        {"id": 1, "titulo": "Generar contraseñas", "descripcion": "Contraseña aleatoria o propia"},
        {"id": 2, "titulo": "Ver contraseñas", "descripcion": "Ver todas, últimas, sin asignar o usadas"},
        {"id": 3, "titulo": "Añadir sitio", "descripcion": "Asignar un sitio a una contraseña"},
        {"id": 4, "titulo": "Eliminar contraseña", "descripcion": "Eliminar contraseña seleccionada"},
        {"id": 5, "titulo": "Buscar contraseña", "descripcion": "Buscar por nombre de sitio"},
        {"id": 6, "titulo": "Salir", "descripcion": "Cerrar la aplicación"}
    ]
    return menu

def obtener_submenu_generar():
    """
    Devuelve el submenú de la opción 1 (Generar contraseñas)
    """
    submenu = [
        {"id": 1, "titulo": "Contraseña aleatoria"},
        {"id": 2, "titulo": "Contraseña propia (manual)"}
    ]
    return submenu