# Trabajo Práctico Integrador 2 - Matemática

TPI 2 de Matemática, UTN TUPaD

---

## 📚 Estructura del proyecto

```
tp-2-integrador-matematica/
│
├── main.py
├── modulos/
│   ├── login.py          # Unidad 1 - Simulación de login
│   ├── resumen.py        # Unidad 3 - Lógica aplicada a rutas
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

### Unidad 3 – Lógica aplicada a rutas

Se aplican **operadores lógicos (AND, OR, NOT)** para validar propiedades de las rutas como si son turísticas, si fueron recorridas, o si pasan por CABA.

**Conceptos aplicados:**

- Operadores lógicos (AND, OR, NOT)
- Expresiones booleanas compuestas
- Validación condicional de datos

**Ejemplo simplificado:**

```python
if datos["turistica"] and not datos["pasa_por_caba"]:
    print("✅ Es una ruta turística que NO pasa por CABA.")
```

---

### Unidad 6 – Algoritmos de Rutas y Grafos

Se simula un sistema de **análisis y recomendación de rutas** usando grafos ponderados.  
El módulo analiza rutas existentes y utiliza el **algoritmo de Dijkstra** para encontrar el camino más rápido entre ciudades.

**Conceptos aplicados:**

- Representación de grafos mediante diccionarios
- Algoritmo de Dijkstra para caminos más cortos
- Análisis de rutas (tiempo, cantidad de lugares, rutas más rápidas)

**Funcionalidades:**

- Calcula tiempos totales de trayectos
- Identifica la ruta más larga y la que visita más lugares
- Encuentra la mejor ruta existente
- Genera nuevas rutas recomendadas usando Dijkstra

---

## 🧠 Parte Práctica

El programa principal (`main.py`) presenta un menú interactivo que requiere iniciar sesión primero.

**Flujo del programa:**

1. Menú principal con opciones
2. **Unidad 1**: Inicio de sesión (requerido para acceder a otras opciones)
3. **Unidad 3**: Validación lógica de rutas
4. **Unidad 6**: Análisis de rutas con grafos y Dijkstra

**Credenciales de acceso:**

- Email: `javier@mate.com`
- Contraseña: `12345abc`

---

## 🧮 Dependencias

- Python 3.10+

---

## 🚀 Ejecución

```bash
python main.py
```
