# Trabajo Práctico Integrador 2 - Matemática

TPI 2 de Matemática, UTN TUPaD

---

## 📚 Estructura del proyecto

```
tp-2-integrador-matematica/
│
├── main.py
├── modules/
│   ├── login.py          # Unidad 1 - Simulación de login
│   ├── resumen.py        # Unidad 3 - Estadística descriptiva
│   ├── mapa.py           # Unidad 6 - Algoritmos de ruta (grafos)
│   └── datos.py          # Fuente de datos utilizada por los módulos
│
└── README.md
```

---

## 🧩 Parte Teórica

### Unidad 1 – Lógica y Validaciones
Se trabaja el concepto de **expresiones lógicas y condicionales** a través de una **simulación de inicio de sesión**.  
El programa solicita un **correo electrónico y contraseña**, verificando su validez mediante comparaciones lógicas.

**Conceptos aplicados:**
- Estructuras condicionales (`if`, `else`)
- Expresiones booleanas
- Control de flujo y mensajes de error

**Ejemplo simplificado del código:**
```python
def iniciar_sesion():
    usuario = "usuario@ejemplo.com"
    password = "1234"

    email = input("Ingrese su correo: ")
    clave = input("Ingrese su contraseña: ")

    if email == usuario and clave == password:
        print("✅ Bienvenido al sistema.")
    else:
        print("❌ Credenciales inválidas.")
```

---

### Unidad 3 – Estadística Descriptiva
Se desarrolla un módulo para **analizar un conjunto de datos numéricos**, calculando medidas estadísticas como **promedio, máximo, mínimo y desviación estándar**.  
La información proviene del archivo `datos.py`.

**Conceptos aplicados:**
- Listas y recorrido con bucles
- Funciones matemáticas básicas
- Cálculo de promedio, varianza y desviación estándar

**Ejemplo simplificado:**
```python
from modules.datos import valores

def resumen_datos():
    promedio = sum(valores) / len(valores)
    print(f"Promedio: {promedio}")
```

---

### Unidad 6 – Algoritmos de Rutas y Grafos
Se simula un sistema de **recomendación de rutas** similar a los utilizados por Google Maps.  
El algoritmo analiza las conexiones entre nodos (lugares) y determina el camino más corto disponible.

**Conceptos aplicados:**
- Representación de grafos mediante diccionarios
- Búsqueda de rutas (BFS/DFS o Dijkstra)
- Validación de rutas y manejo de errores

**Ejemplo simplificado:**
```python
def generar_ruta(origen, destino, mapa):
    if origen not in mapa or destino not in mapa:
        print("Ruta no válida.")
        return
    print(f"Ruta desde {origen} hasta {destino}: {' -> '.join(mapa[origen])}")
```

---

## 🧠 Parte Práctica

El programa principal (`main.py`) guía al usuario paso a paso desde la terminal.

**Ejemplo de flujo:**
1. Inicio del programa  
2. Simulación de login  
3. Acceso al menú principal  
4. Elección entre:
   - Ver resumen estadístico
   - Generar ruta recomendada
   - Salir del sistema

**Ejemplo de ejecución:**
```bash
$ python main.py

=== BIENVENIDO AL SISTEMA ===
Ingrese su correo: usuario@ejemplo.com
Ingrese su contraseña: 1234
✅ Bienvenido al sistema.

Seleccione una opción:
1. Ver resumen estadístico
2. Recomendación de ruta
3. Salir
```

---

## 🧮 Dependencias

- Python 3.10+

---

## 🚀 Ejecución

```bash
python main.py
```
