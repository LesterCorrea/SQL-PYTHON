#  Sistema de Gestión de Base de Datos Oracle - Python

Sistema completo de gestión de bases de datos Oracle XE con interfaz de consola enriquecida, que incluye operaciones CRUD y funcionalidades avanzadas como procedimientos almacenados, triggers y vistas.

---

##  Tabla de Contenidos

1. [Características](#características)
2. [Requisitos](#requisitos)
3. [Instalación](#instalación)
4. [Configuración](#configuración)
5. [Estructura del Proyecto](#estructura-del-proyecto)
6. [Uso del Sistema](#uso-del-sistema)
7. [Funcionalidades Detalladas](#funcionalidades-detalladas)
8. [Ejemplos Prácticos](#ejemplos-prácticos)
9. [Solución de Problemas](#solución-de-problemas)
10. [Créditos](#créditos)

---

##  Características

###  Funcionalidades Básicas
-  Conexión segura a Oracle XE
-  Visualización de todas las tablas del usuario
-  Consulta de datos de cualquier tabla
-  Operaciones CRUD completas (Crear, Leer, Actualizar, Eliminar)
-  Interfaz visual atractiva con colores y tablas formateadas

###  Funcionalidades Avanzadas
-  **Procedimientos Almacenados**: Crear, listar, ejecutar y eliminar
-  **Triggers Básicos**: Crear, listar y eliminar triggers de auditoría
-  **Vistas**: Crear, listar, consultar y eliminar vistas
-  Ejecución interactiva de procedimientos con parámetros
-  Templates predefinidos para casos comunes
-  Confirmación de seguridad para operaciones de eliminación

---

##  Requisitos

### Software Necesario
- **Python**: 3.7 o superior
- **Oracle Database XE**: 11g o superior
- **Oracle Client**: Bibliotecas cliente de Oracle

### Librerías Python
```bash
oracledb>=1.0.0
rich>=13.0.0
tabulate>=0.9.0
```

---

##  Instalación

### 1. Clonar o Descargar el Proyecto
```bash
git clone https://github.com/LesterCorrea/SQL-PYTHON.git
cd sistema-oracle-python
```

### 2. Instalar Dependencias
```bash
pip install oracledb rich tabulate
```

### 3. Verificar Oracle Client
Asegúrate de tener instalado Oracle Instant Client o acceso a `ORACLE_HOME`.

**Windows:**
```
C:\oraclexe\app\oracle\product\11.2.0\server\BIN
```

**Linux/Mac:**
```
/opt/oracle/instantclient_XX_X
```

---

##  Configuración

### 1. Configurar Conexión a la Base de Datos

Edita el archivo `conexion.py`:

```python
# Ruta al Oracle Client (ajusta según tu instalación)
oracledb.init_oracle_client(lib_dir=r"C:\oraclexe\app\oracle\product\11.2.0\server\BIN")

# Credenciales de conexión
connection = oracledb.connect(
    user = "tu_usuario",       # Cambia esto
    password = "tu_password",  # Cambia esto
    dsn = "localhost:1521/XE"  # Ajusta si es necesario
)
```

### 2. Verificar Permisos del Usuario

Tu usuario de Oracle debe tener los siguientes privilegios:

```sql
-- Conectarse como SYSTEM o DBA
-- sqlplus / as sysdba

GRANT CONNECT, RESOURCE TO tu_usuario;
GRANT CREATE PROCEDURE TO tu_usuario;
GRANT CREATE TRIGGER TO tu_usuario;
GRANT CREATE VIEW TO tu_usuario;
GRANT UNLIMITED TABLESPACE TO tu_usuario;
```

---

##  Estructura del Proyecto

```
proyecto/
│
├── conexion.py              # Gestión de conexión a Oracle
├── funciones.py             # Funciones CRUD básicas
├── funciones_avanzadas.py   # Procedimientos, triggers y vistas
├── main.py                  # Menú principal y flujo del programa
└── README.md                # Esta documentación
```

### Descripción de Archivos

| Archivo | Descripción |
|---------|-------------|
| `conexion.py` | Maneja la inicialización del cliente Oracle y la conexión a la BD |
| `funciones.py` | Contiene funciones para ver tablas y operaciones CRUD |
| `funciones_avanzadas.py` | Implementa gestión de procedimientos, triggers y vistas |
| `main.py` | Punto de entrada del programa con menús interactivos |

---

##  Uso del Sistema

### Iniciar el Programa

```bash
python main.py
```

### Menú Principal

```
╔════════════════════════════════════════╗
║     SISTEMA DE BASE DE DATOS           ║
║   Conexión a Oracle XE - Python        ║
╚════════════════════════════════════════╝

    1️  Ver tablas
    2️  Ver datos de una tabla
    3️  Gestión de datos (CRUD)
    4️  Procedimientos almacenados
    5  Triggers básicos
    6️  Vistas
    7️  Salir

Selecciona una opción:
```

---

##  Funcionalidades Detalladas

### 1️ Ver Tablas

Muestra todas las tablas del usuario actual en formato de tabla:

```
┏━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃ N° ┃ Nombre de la tabla ┃
┡━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ 1  │ EMPLEADOS          │
│ 2  │ DEPARTAMENTOS      │
│ 3  │ PRODUCTOS          │
└────┴────────────────────┘
```

---

### 2️ Ver Datos de una Tabla

Permite seleccionar una tabla y visualizar todos sus registros en formato grid:

```
╒════╤════════╤══════════════╤═══════════╕
│    │ ID     │ NOMBRE       │ SALARIO   │
╞════╪════════╪══════════════╪═══════════╡
│  0 │ 1      │ Juan Pérez   │ 3500.00   │
│  1 │ 2      │ María López  │ 4200.00   │
╘════╧════════╧══════════════╧═══════════╛
```

---

### 3️ Gestión de Datos (CRUD)

#### **Insertar Registros**
1. Selecciona la tabla
2. Ingresa valores para cada columna
3. El sistema detecta automáticamente columnas de fecha

**Ejemplo:**
```
Insertando en EMPLEADOS
➤ Ingrese valor para ID: 5
➤ Ingrese valor para NOMBRE: Carlos Ruiz
➤ Ingrese valor para SALARIO: 3800
➤ Ingrese valor para FECHA_INGRESO: 15-11-2024

  Registro insertado correctamente.
```

#### **Actualizar Registros**
1. Selecciona la tabla
2. Especifica la columna a actualizar
3. Ingresa el nuevo valor
4. Define la condición WHERE

**Ejemplo:**
```
Actualizando EMPLEADOS
Columnas disponibles: ID, NOMBRE, SALARIO, FECHA_INGRESO
Columna a actualizar: SALARIO
Nuevo valor: 4000
Columna para condición (WHERE): ID
Valor de condición: 5

  Registro actualizado correctamente.
```

#### **Eliminar Registros**
1. Selecciona la tabla
2. Define la condición WHERE

**Ejemplo:**
```
Eliminando de EMPLEADOS
Columnas disponibles: ID, NOMBRE, SALARIO, FECHA_INGRESO
Columna para condición (WHERE): ID
Valor de condición: 5

  Registro eliminado correctamente.
```

---

### 4️ Procedimientos Almacenados

#### **Crear Procedimiento**

**Opción 1: Procedimiento para Insertar**
```sql
-- Generado automáticamente
CREATE OR REPLACE PROCEDURE insertar_empleado (
    p_id IN NUMBER,
    p_nombre IN VARCHAR2,
    p_salario IN NUMBER
)
IS
BEGIN
    INSERT INTO EMPLEADOS VALUES (p_id, p_nombre, p_salario);
    COMMIT;
    DBMS_OUTPUT.PUT_LINE('Registro insertado correctamente');
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
        ROLLBACK;
END;
```

**Opción 2: Procedimiento para Actualizar**
```sql
CREATE OR REPLACE PROCEDURE actualizar_salario (
    p_id IN NUMBER,
    p_nuevo_valor IN VARCHAR2
)
IS
BEGIN
    UPDATE EMPLEADOS 
    SET SALARIO = p_nuevo_valor 
    WHERE ID = p_id;
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
END;
```

**Opción 3: Procedimiento Personalizado**
- Permite ingresar código SQL completo manualmente

#### **Listar Procedimientos**

Muestra todos los procedimientos con su estado:

```
┏━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━┓
┃ N° ┃ Nombre             ┃ Fecha Creación ┃ Estado   ┃
┡━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━┩
│ 1  │ INSERTAR_EMPLEADO  │ 2024-11-30     │ VALID    │
│ 2  │ ACTUALIZAR_SALARIO │ 2024-11-30     │ VALID    │
└────┴────────────────────┴────────────────┴──────────┘
```

#### **Ejecutar Procedimiento**

El sistema detecta automáticamente los parámetros:

```
Parámetros del procedimiento 'insertar_empleado':
➤ P_ID (NUMBER, IN): 10
➤ P_NOMBRE (VARCHAR2, IN): Ana García
➤ P_SALARIO (NUMBER, IN): 4500

  Procedimiento 'insertar_empleado' ejecutado correctamente.
```

#### **Eliminar Procedimiento**

Con confirmación de seguridad:

```
¿Estás seguro de eliminar el procedimiento 'insertar_empleado'? (S/N): S
  Procedimiento 'insertar_empleado' eliminado correctamente.
```

---

### 5️ Triggers Básicos

#### **Crear Trigger**

**Opción 1: BEFORE INSERT - Auditoría**
```sql
CREATE OR REPLACE TRIGGER audit_insert_empleados
BEFORE INSERT ON EMPLEADOS
FOR EACH ROW
BEGIN
    DBMS_OUTPUT.PUT_LINE('Insertando nuevo registro en EMPLEADOS');
    DBMS_OUTPUT.PUT_LINE('Fecha: ' || SYSDATE);
END;
```

**Opción 2: AFTER UPDATE - Auditoría**
```sql
CREATE OR REPLACE TRIGGER audit_update_empleados
AFTER UPDATE ON EMPLEADOS
FOR EACH ROW
BEGIN
    DBMS_OUTPUT.PUT_LINE('Registro actualizado en EMPLEADOS');
    DBMS_OUTPUT.PUT_LINE('Usuario: ' || USER);
    DBMS_OUTPUT.PUT_LINE('Fecha: ' || SYSDATE);
END;
```

**Opción 3: BEFORE DELETE - Prevenir Eliminación**
```sql
CREATE OR REPLACE TRIGGER prevent_delete_empleados
BEFORE DELETE ON EMPLEADOS
FOR EACH ROW
BEGIN
    RAISE_APPLICATION_ERROR(-20001, 'No se permite eliminar registros de EMPLEADOS');
END;
```

**Opción 4: Trigger Personalizado**
- Permite código SQL completo

#### **Listar Triggers**

```
┏━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━┓
┃ N° ┃ Nombre                 ┃ Tabla      ┃ Evento     ┃ Estado   ┃
┡━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━┩
│ 1  │ AUDIT_INSERT_EMPLEADOS │ EMPLEADOS  │ INSERT     │ ENABLED  │
│ 2  │ AUDIT_UPDATE_EMPLEADOS │ EMPLEADOS  │ UPDATE     │ ENABLED  │
└────┴────────────────────────┴────────────┴────────────┴──────────┘
```

#### **Eliminar Trigger**

```
¿Estás seguro de eliminar el trigger 'audit_insert_empleados'? (S/N): S
  Trigger 'audit_insert_empleados' eliminado correctamente.
```

---

### 6️ Vistas

#### **Crear Vista**

```
Nombre de la vista: vista_empleados_senior
Ingresa la consulta SELECT para la vista:
(SELECT ...): SELECT * FROM EMPLEADOS WHERE SALARIO > 4000

  Vista 'vista_empleados_senior' creada exitosamente.
```

**Vista Generada:**
```sql
CREATE OR REPLACE VIEW vista_empleados_senior AS 
SELECT * FROM EMPLEADOS WHERE SALARIO > 4000
```

#### **Listar Vistas**

```
┏━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ N° ┃ Nombre                 ┃ Definición                      ┃
┡━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 1  │ VISTA_EMPLEADOS_SENIOR │ SELECT * FROM EMPLEADOS WHER... │
└────┴────────────────────────┴─────────────────────────────────┘
```

#### **Mostrar Resultados de Vista**

```
Resultados de la vista: VISTA_EMPLEADOS_SENIOR

╒════╤════════╤══════════════╤═══════════╕
│    │ ID     │ NOMBRE       │ SALARIO   │
╞════╪════════╪══════════════╪═══════════╡
│  0 │ 2      │ María López  │ 4200.00   │
│  1 │ 10     │ Ana García   │ 4500.00   │
╘════╧════════╧══════════════╧═══════════╛
```

#### **Eliminar Vista**

```
¿Estás seguro de eliminar la vista 'vista_empleados_senior'? (S/N): S
✓ Vista 'vista_empleados_senior' eliminada correctamente.
```

---

##  Ejemplos Prácticos

### Ejemplo 1: Sistema de Auditoría Completo

#### Paso 1: Crear Tabla de Auditoría
```sql
CREATE TABLE AUDITORIA (
    ID NUMBER PRIMARY KEY,
    TABLA VARCHAR2(50),
    OPERACION VARCHAR2(20),
    USUARIO VARCHAR2(50),
    FECHA DATE
);
```

#### Paso 2: Crear Procedimiento de Auditoría
```sql
CREATE OR REPLACE PROCEDURE registrar_auditoria (
    p_tabla IN VARCHAR2,
    p_operacion IN VARCHAR2
)
IS
BEGIN
    INSERT INTO AUDITORIA VALUES (
        SEQ_AUDITORIA.NEXTVAL,
        p_tabla,
        p_operacion,
        USER,
        SYSDATE
    );
    COMMIT;
END;
```

#### Paso 3: Crear Trigger que Usa el Procedimiento
```sql
CREATE OR REPLACE TRIGGER trg_audit_empleados
AFTER INSERT OR UPDATE OR DELETE ON EMPLEADOS
BEGIN
    IF INSERTING THEN
        registrar_auditoria('EMPLEADOS', 'INSERT');
    ELSIF UPDATING THEN
        registrar_auditoria('EMPLEADOS', 'UPDATE');
    ELSIF DELETING THEN
        registrar_auditoria('EMPLEADOS', 'DELETE');
    END IF;
END;
```

#### Paso 4: Crear Vista de Auditoría
```sql
CREATE OR REPLACE VIEW vista_auditoria_reciente AS
SELECT * FROM AUDITORIA WHERE FECHA > SYSDATE - 7
ORDER BY FECHA DESC;
```

---

### Ejemplo 2: Control de Salarios

#### Procedimiento para Aumentar Salario
```sql
CREATE OR REPLACE PROCEDURE aumentar_salario (
    p_id IN NUMBER,
    p_porcentaje IN NUMBER
)
IS
    v_salario_actual NUMBER;
BEGIN
    SELECT SALARIO INTO v_salario_actual 
    FROM EMPLEADOS WHERE ID = p_id;
    
    UPDATE EMPLEADOS 
    SET SALARIO = v_salario_actual * (1 + p_porcentaje/100)
    WHERE ID = p_id;
    
    COMMIT;
    DBMS_OUTPUT.PUT_LINE('Salario actualizado correctamente');
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Empleado no encontrado');
    WHEN OTHERS THEN
        ROLLBACK;
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
END;
```

#### Trigger de Validación de Salario
```sql
CREATE OR REPLACE TRIGGER validar_salario
BEFORE INSERT OR UPDATE ON EMPLEADOS
FOR EACH ROW
BEGIN
    IF :NEW.SALARIO < 0 THEN
        RAISE_APPLICATION_ERROR(-20002, 'El salario no puede ser negativo');
    END IF;
    
    IF :NEW.SALARIO > 20000 THEN
        RAISE_APPLICATION_ERROR(-20003, 'El salario excede el máximo permitido');
    END IF;
END;
```

#### Vista de Estadísticas Salariales
```sql
CREATE OR REPLACE VIEW vista_estadisticas_salarios AS
SELECT 
    COUNT(*) AS total_empleados,
    AVG(SALARIO) AS salario_promedio,
    MIN(SALARIO) AS salario_minimo,
    MAX(SALARIO) AS salario_maximo
FROM EMPLEADOS;
```

---

##  Solución de Problemas

### Error: "DPI-1047: Cannot locate a 64-bit Oracle Client library"

**Solución:**
1. Descarga Oracle Instant Client de [Oracle Website](https://www.oracle.com/database/technologies/instant-client/downloads.html)
2. Extrae en una carpeta (ej: `C:\oracle\instantclient_19_8`)
3. Actualiza `conexion.py`:
```python
oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient_19_8")
```

---

### Error: "ORA-01017: invalid username/password"

**Solución:**
1. Verifica las credenciales en `conexion.py`
2. Conecta como SYSTEM y verifica el usuario:
```sql
SELECT username, account_status FROM dba_users WHERE username = 'TU_USUARIO';
```
3. Si está bloqueado:
```sql
ALTER USER tu_usuario ACCOUNT UNLOCK;
ALTER USER tu_usuario IDENTIFIED BY nueva_password;
```

---

### Error: "ORA-12154: TNS:could not resolve the connect identifier"

**Solución:**
1. Verifica que Oracle esté corriendo:
```bash
# Windows
lsnrctl status

# Linux
sudo service oracle-xe status
```
2. Revisa el DSN en `conexion.py`:
```python
dsn="localhost:1521/XE"   # Para Oracle XE
dsn="localhost:1521/ORCL" # Para Oracle Standard
```

---

### Error: "ORA-01031: insufficient privileges"

**Solución:**
Conecta como SYSTEM y otorga privilegios:
```sql
GRANT CREATE PROCEDURE TO tu_usuario;
GRANT CREATE TRIGGER TO tu_usuario;
GRANT CREATE VIEW TO tu_usuario;
GRANT CREATE TABLE TO tu_usuario;
GRANT UNLIMITED TABLESPACE TO tu_usuario;
```

---

### Caracteres Extraños en la Consola (Windows)

**Solución:**
1. Configura la codificación de la terminal:
```bash
chcp 65001
```
2. O ejecuta desde PowerShell:
```powershell
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
python main.py
```

---

### El Programa se Cierra Inmediatamente

**Solución:**
1. Ejecuta desde la terminal/cmd, no con doble clic
2. Verifica que tengas todas las dependencias instaladas:
```bash
pip list | findstr "oracledb rich tabulate"
```

---

##  Consultas Útiles para Administración

### Ver Todos los Objetos del Usuario
```sql
SELECT object_type, object_name, status 
FROM user_objects 
ORDER BY object_type, object_name;
```

### Ver Código Fuente de Procedimientos
```sql
SELECT text 
FROM user_source 
WHERE name = 'NOMBRE_PROCEDIMIENTO' 
ORDER BY line;
```

### Ver Dependencias de Triggers
```sql
SELECT trigger_name, table_name, triggering_event, status 
FROM user_triggers;
```

### Ver Definición de Vistas
```sql
SELECT view_name, text 
FROM user_views;
```

### Ver Errores de Compilación
```sql
SELECT name, type, line, position, text 
FROM user_errors 
ORDER BY name, sequence;
```

---

##  Personalización

### Cambiar Colores de la Interfaz

Edita los colores en `funciones.py` y `funciones_avanzadas.py`:

```python
# Colores disponibles en Rich
console.print("[bold red]Texto en rojo[/bold red]")
console.print("[bold green]Texto en verde[/bold green]")
console.print("[bold yellow]Texto en amarillo[/bold yellow]")
console.print("[bold blue]Texto en azul[/bold blue]")
console.print("[bold magenta]Texto en magenta[/bold magenta]")
console.print("[bold cyan]Texto en cyan[/bold cyan]")
```

### Cambiar Formato de Tablas

En `funciones.py`, modifica el parámetro `tablefmt`:

```python
# Opciones: fancy_grid, grid, simple, plain, html, latex
console.print(tabulate(filas, headers=columnas, tablefmt="grid"))
```

---

##  Mejores Prácticas

1. **Nunca hardcodees credenciales** en el código para producción
   - Usa variables de entorno
   - Usa archivos de configuración externos (`.env`)

2. **Valida todas las entradas del usuario** antes de ejecutar SQL
   - Usa parámetros bind (`:1`, `:2`) en lugar de concatenación de strings

3. **Realiza backups** antes de ejecutar procedimientos de eliminación masiva

4. **Prueba los procedimientos** en un ambiente de desarrollo primero

5. **Documenta tus procedimientos y triggers** con comentarios

6. **Usa transacciones** (`COMMIT`/`ROLLBACK`) apropiadamente

---

##  Recursos Adicionales

- [Documentación Oracle Database](https://docs.oracle.com/en/database/)
- [python-oracledb Documentation](https://python-oracledb.readthedocs.io/)
- [Rich Documentation](https://rich.readthedocs.io/)
- [Oracle SQL Language Reference](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/)

---

##  Créditos

**Desarrollado por:** Fernando Correa, Farid Chaves y Jose Contreras  
**Curso:** Base de Datos  
**Institución:** Tecsup  
**Año:** 2025

---

##  Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

---

##  Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NuevaFuncionalidad`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/NuevaFuncionalidad`)
5. Abre un Pull Request

---

##  Soporte

Si encuentras algún problema o tienes preguntas:

1. Revisa la sección de [Solución de Problemas](#-solución-de-problemas)
2. Verifica que Oracle esté corriendo correctamente
3. Confirma que tienes los permisos necesarios
4. Revisa los logs de error de Oracle

---

##  Notas para Estudiantes

Este proyecto cubre los siguientes temas del curso:

-  Conexión a bases de datos Oracle desde Python
-  Operaciones CRUD (Create, Read, Update, Delete)
-  Procedimientos almacenados (Stored Procedures)
-  Triggers (Disparadores)
-  Vistas (Views)
-  Manejo de excepciones en PL/SQL
-  Buenas prácticas de programación
-  Interfaz de usuario en consola

---

**¡Gracias por usar el Sistema de Gestión de Base de Datos Oracle!** 

*Versión 1.3 - Noviembre 2025*
