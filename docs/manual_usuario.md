# Manual de Usuario
**Proyecto:** Conexión y visualización de datos en Oracle con Python

---

## 1. Descripción general
Este programa permite conectarse a una base de datos Oracle desde Python, visualizar las tablas existentes y consultar su contenido de forma interactiva mediante un menú en consola.
Su objetivo principal es ofrecer una herramienta sencilla para explorar los datos almacenados en una base Oracle XE.

---

## 2. Requisitos del sistema

### Software necesario
- **Python 3.11 o superior**
- **Oracle Database XE 11g o superior**
- **Biblioteca `oracledb`** instalada con:
  ```bash
  pip install oracledb
  ```

### 🔹 Configuración del cliente Oracle
Antes de ejecutar el programa, asegúrate de tener instalado el cliente de Oracle y configurada la ruta correctamente en tu código:
```python
oracledb.init_oracle_client(lib_dir=r"C:\oraclexe\app\oracle\product\11.2.0\server\BIN")
```

---

## 🧩 3. Estructura del proyecto
```
proyecto_oracle/
│
├── data/
│   ├── scripts_sql/   
│   │   ├── crear_tablas.sql
│   │   └── insertar_datos.sql      
│   └── README.md                
│
├── docs/
│   ├── diagrama_ER.png            
│   └── manual_usuario.md  
│
├── src/
│   ├── conexion.py                 
│   ├── funciones.py                
│   ├── main.py                     
│   └── __init__.py                
│
└── requirements.txt                    
```

---

## 4. Uso del programa

1. **Ejecuta el archivo principal:**
   ```bash
   python src/main.py
   ```

2. **Selecciona una opción del menú:**

   | Opción | Descripción |
   |--------:|-------------|
   | 1 | Ver las tablas disponibles en la base de datos |
   | 2 | Ver los datos de una tabla específica |
   | 3 | Salir del programa |

3. Si eliges la opción **2**, el sistema mostrará las tablas disponibles y te pedirá que escribas el nombre de una.
   Después, mostrará su contenido en formato tabular y legible.

---

##  5. Base de datos de ejemplo

El archivo `data/crear_tabla.sql` incluye la creación de varias tablas con sus relaciones:
- **ALUMNOS**
- **CURSOS**
- **PROFESORES**
- **MATRICULAS**
- **NOTAS**
- **DEPARTAMENTOS**

Cada tabla contiene registros de ejemplo que permiten probar el sistema sin necesidad de ingresar nuevos datos manualmente.

---


## Créditos
Proyecto desarrollado por **Grupo 1** como práctica de conexión y manipulación de datos en Oracle usando Python.
