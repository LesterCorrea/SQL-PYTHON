# Proyecto SQL-PYTHON

Este proyecto demuestra cómo conectar **Python** con una **base de datos Oracle (SQL*Plus / OracleXE)**, permitiendo visualizar las tablas y sus datos mediante un menú interactivo desde consola.  
Está pensado como un ejercicio educativo para comprender la interacción entre un lenguaje de programación y un sistema gestor de bases de datos.

---

## Características principales

- Conexión directa a **Oracle Database XE** usando `python-oracledb`
- Menú interactivo para:
  -  Ver todas las tablas disponibles
  -  Visualizar los datos de cualquier tabla
  -  Salir de la aplicación
- Formato tabular atractivo en consola (con `tabulate`)
- Organización profesional del proyecto en carpetas (scripts SQL, documentación, módulos Python)

---

##  Requisitos

- Python **3.8+**
- Oracle **Database XE (11g o superior)**
- Cliente Oracle configurado (`oracledb.init_oracle_client`)
- Librerías Python:
  ```bash
  pip install oracledb tabulate
  ```

##  Instalación 
 ```bash
git clone https://github.com/usuario/sql-python.git
cd sql-python
```

### ejecutar los scripts SQL en SLQ*Plus
```bash
@data/scripts_sql/crear_tablas.sql 
@data/scripts_sql/insertar_datos.sql
```
## Ejecución
```bash
python main.py
```