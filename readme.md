<div align="center">

<h1>🔐 Gestor de Contraseñas Profesional</h1>

**Generador, evaluador y gestor seguro de contraseñas con API REST y CLI interactivo**

<!-- Badges -->
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Tests](https://img.shields.io/badge/Tests-pytest-0A9EDC?style=for-the-badge&logo=pytest)](tests/)

</div>

---

## 📋 Tabla de Contenidos

1. [Descripción](#-descripción)
2. [Características](#-características)
3. [Requisitos](#-requisitos)
4. [Instalación](#-instalación)
5. [Uso](#-uso)
6. [Estructura del Proyecto](#-estructura-del-proyecto)
7. [Documentación](#-documentación)
8. [Testing](#-testing)
9. [Contribuciones](#-contribuciones)
10. [Licencia](#-licencia)
11. [Autor](#-autor)

---

## 📖 Descripción

**Gestor de Contraseñas Profesional** es una aplicación completa y robusta diseñada para generar, evaluar y gestionar contraseñas seguras. Combina un generador criptográfico de contraseñas, un evaluador de fortaleza inteligente y un sistema de almacenamiento persistente. Proporciona dos interfaces: una REST API con FastAPI y una CLI interactiva con menú de usuario.

Está construido con patrones de arquitectura profesionales, testing completo e implementación de seguridad de clase empresarial.

---

## ✨ Características

### 🔐 Generación Segura de Contraseñas
- **Criptografía de nivel militar**: Utiliza `secrets` para aleatoriedad criptográficamente segura
- **Configuración granular**: Control total sobre caracteres (mayúsculas, minúsculas, números, símbolos)
- **Garantías de composición**: Asegura al menos un carácter de cada tipo seleccionado
- **Generación por lotes**: Crear múltiples contraseñas simultáneamente
- **Exclusión de patrones**: Evita información sensible del usuario en la contraseña

### 🧮 Evaluación Inteligente
- **Sistema de puntuación**: Análisis completo de fortaleza basado en composición
- **Evaluación de longitud**: Criterios diferenciados por rango de caracteres
- **Clasificación multinivel**: Débil → Media → Fuerte → Muy Fuerte
- **Indicadores visuales**: Emojis intuitivos para rápida identificación

### 💾 Almacenamiento Seguro
- **Persistencia en JSON**: Almacenamiento local eficiente
- **Tolerancia a fallos**: Manejo elegante de archivos corruptos o inexistentes
- **Asignación de sitios**: Mapeo de contraseñas a aplicaciones/servicios
- **Gestión flexible**: Crear, leer, actualizar, eliminar contraseñas

### 🌐 REST API
- **FastAPI moderno**: Framework asincrónico y tipado
- **Documentación automática**: Swagger UI integrado
- **Endpoint `/generar`**: Generación bajo demanda con parámetros personalizados
- **Endpoint `/`**: Health check de la API

### 💻 CLI Interactivo
- **Menú intuitivo**: Interfaz de usuario amigable
- **6 opciones principales**: Generar, ver, asignar, eliminar, buscar, salir
- **Validación robusta**: Manejo de errores y entradas inválidas
- **Feedback visual**: Mensajes claros con emojis

---

## 📦 Requisitos

- **Python**: >= 3.9
- **pip**: gestor de paquetes de Python
- **Sistema Operativo**: Windows, macOS, Linux

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/fireforgegammer/APP.git
cd APP
```

### 2. Crear entorno virtual (recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 💡 Uso

### Opción 1: CLI Interactivo (Recomendado para usuarios)

```bash
# Desde el directorio raíz del proyecto
python main.py
```

**Menú disponible:**

```
🔓 GESTOR DE CONTRASEÑAS
1. Generar contraseñas      → Crea 1+ contraseñas con config personalizada
2. Ver contraseñas          → Lista todas con evaluación de fortaleza
3. Añadir sitio             → Asigna una contraseña a una aplicación
4. Eliminar contraseña      → Elimina de forma segura
5. Buscar contraseña        → Búsqueda por sitio
6. Salir                    → Cierra la aplicación
```

**Ejemplo de flujo:**
```
1. Selecciona "1" para generar contraseñas
2. Configura: longitud, caracteres, cantidad
3. Las contraseñas se guardan automáticamente
4. Selecciona "3" para asignar un sitio (ej: github.com)
5. Selecciona "2" para ver todas con niveles de seguridad
```

### Opción 2: REST API

#### Iniciar servidor

```bash
uvicorn src.api:app --reload
```

La API est™ disponible en: `http://localhost:8000`

**Documentación Swagger**: `http://localhost:8000/docs`

#### Endpoints

##### GET `/`
Health check - verifica que el servidor está funcionando

```bash
curl http://localhost:8000/
```

**Respuesta:**
```json
{
  "mensaje": "API funcionando 🚀"
}
```

##### GET `/generar`
Genera una contraseña con parámetros personalizados

**Parámetros Query:**
- `longitud` (int, default: 16): Longitud de 8 a 128 caracteres
- `incluir_mayus` (bool, default: true): Incluir mayúsculas
- `incluir_minus` (bool, default: true): Incluir minúsculas
- `incluir_numeros` (bool, default: true): Incluir dígitos
- `incluir_simbolos` (bool, default: true): Incluir símbolos especiales
- `usuario` (str, default: ""): Nombre a evitar en la contraseña

**Ejemplo:**
```bash
curl "http://localhost:8000/generar?longitud=20&incluir_simbolos=true&usuario=admin"
```

**Respuesta:**
```json
{
  "password": "K7#mPq2$nL9!xR4@wT5"
}
```

---

## 📁 Estructura del Proyecto

```
APP/
├── src/                          # Código fuente principal
│   ├── core/                     # Lógica de negocio
│   │   ├── generador.py          # Generación de contraseñas
│   │   ├── evaluador.py          # Evaluación de fortaleza
│   │   └── storage.py            # Persistencia de datos
│   ├── ui/                       # Interfaz de usuario
│   │   ├── menu.py               # Menú principal
│   │   └── acciones.py           # Acciones disponibles
│   └── api.py                    # REST API con FastAPI
├── tests/                        # Suite de testing
│   ├── unitarios/                # Tests unitarios
│   │   ├── test_generador.py
│   │   ├── test_evaluador.py
│   │   ├── test_storage.py
│   │   └── test_acciones.py
│   └── integration/              # Tests de integración
│       ├── test_core_integration.py
│       └── test_app_integration.py
├── docs/                         # Documentación detallada
│   ├── main.md                   # Punto de entrada
│   ├── generador.md              # Documentación de generador
│   ├── evaluador.md              # Documentación de evaluador
│   ├── storage.md                # Documentación de storage
│   ├── menu.md                   # Documentación de menú
│   ├── acciones.md               # Documentación de acciones
│   ├── asistencia_ia.md          # Guía de asistencia IA
│   ├── errores.md                # Registro de errores
│   ├── tests.md                  # Documentación de tests
│   └── nomeclatura.md            # Estándares de nomenclatura
├── main.py                       # Punto de entrada CLI
├── requirements.txt              # Dependencias de Python
├── conftest.py                   # Configuración de pytest
├── LICENSE                       # Licencia MIT
└── README.md                     # Este archivo
```

---

## 📚 Documentación

Para documentación detallada sobre cada módulo, consulta los archivos en la carpeta `/docs`:

| Archivo | Contenido |
|---------|-----------|
| [`docs/generador.md`](docs/generador.md) | API y funcionamiento del generador de contraseñas |
| [`docs/evaluador.md`](docs/evaluador.md) | Sistema de puntuación y niveles de fortaleza |
| [`docs/storage.md`](docs/storage.md) | Persistencia de datos y formato JSON |
| [`docs/menu.md`](docs/menu.md) | Interfaz CLI y flujo de usuarios |
| [`docs/acciones.md`](docs/acciones.md) | Acciones disponibles en la aplicación |
| [`docs/main.md`](docs/main.md) | Punto de entrada y distribución de tareas |
| [`docs/tests.md`](docs/tests.md) | Estrategia de testing y cobertura |

---

## 🧪 Testing

El proyecto incluye una suite completa de tests unitarios e integración con **pytest**.

### Ejecutar todos los tests

```bash
pytest
```

### Ejecutar tests específicos

```bash
# Solo tests unitarios
pytest tests/unitarios/

# Solo tests de integración
pytest tests/integration/

# Test específico
pytest tests/unitarios/test_generador.py -v
```

### Ejecutar con cobertura

```bash
pytest --cov=src --cov-report=html
```

### Estructura de tests

```
tests/
├── unitarios/                    # Tests por componente
│   ├── test_generador.py         # Validar generación segura
│   ├── test_evaluador.py         # Validar puntuación
│   ├── test_storage.py           # Validar persistencia
│   └── test_acciones.py          # Validar acciones de CLI
└── integration/                  # Tests end-to-end
    ├── test_core_integration.py
    └── test_app_integration.py
```

---

## 👥 Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes:

1. **Fork** el repositorio
2. **Crea una rama** para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. **Abre un Pull Request**

---

## 📄 Licencia

Este proyecto está licenciado bajo la **MIT License**. Consulta el archivo [`LICENSE`](LICENSE) para más detalles.

La licencia MIT permite:
- ✅ Uso comercial
- ✅ Modificación
- ✅ Distribución
- ✅ Uso privado

Con la única condición de incluir la licencia y aviso de copyright.

---
<div align="center">

## 👤 Autor


[![GitHub: fireforgegammer](https://img.shields.io/badge/GitHub-fireforgegammer-181717?style=for-the-badge&logo=github)](https://github.com/Fireforgegammer)

---

**Hecho por 💀 [fireforgegammer](https://github.com/Fireforgegammer)**

⭐ Si te resultó útil, considera dar una estrella al repositorio

</div>
