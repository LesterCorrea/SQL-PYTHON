from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from tabulate import tabulate
import os

console = Console()

def crear_procedimiento_almacenado(cursor, connection):
    console.print(Panel.fit("[bold white]CREAR PROCEDIMIENTO ALMACENADO[/bold white]", style="bold blue"))
    
    console.print("\n[cyan]Ejemplos de procedimientos:[/cyan]")
    console.print("1. Procedimiento para insertar datos")
    console.print("2. Procedimiento para actualizar datos")
    console.print("3. Procedimiento personalizado\n")
    
    opcion = console.input("[cyan]Selecciona el tipo de procedimiento (1-3):[/cyan] ")
    
    try:
        if opcion == "1":
            nombre_proc = console.input("[cyan]Nombre del procedimiento:[/cyan] ")
            tabla = console.input("[cyan]Nombre de la tabla:[/cyan] ")
            
            cursor.execute(f"SELECT column_name, data_type FROM user_tab_columns WHERE table_name = '{tabla.upper()}' ORDER BY column_id")
            columnas = cursor.fetchall()
            
            parametros = []
            for col, tipo in columnas:
                parametros.append(f"p_{col.lower()} IN {tipo}")
            
            valores = [f"p_{col[0].lower()}" for col in columnas]
            
            sql = f"""
CREATE OR REPLACE PROCEDURE {nombre_proc} (
    {', '.join(parametros)}
)
IS
BEGIN
    INSERT INTO {tabla} VALUES ({', '.join(valores)});
    COMMIT;
    DBMS_OUTPUT.PUT_LINE('Registro insertado correctamente');
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
        ROLLBACK;
END;
"""
        elif opcion == "2":
            nombre_proc = console.input("[cyan]Nombre del procedimiento:[/cyan] ")
            tabla = console.input("[cyan]Nombre de la tabla:[/cyan] ")
            col_clave = console.input("[cyan]Columna clave (ID):[/cyan] ")
            col_actualizar = console.input("[cyan]Columna a actualizar:[/cyan] ")
            
            sql = f"""
CREATE OR REPLACE PROCEDURE {nombre_proc} (
    p_id IN NUMBER,
    p_nuevo_valor IN VARCHAR2
)
IS
BEGIN
    UPDATE {tabla} 
    SET {col_actualizar} = p_nuevo_valor 
    WHERE {col_clave} = p_id;
    COMMIT;
    DBMS_OUTPUT.PUT_LINE('Registro actualizado correctamente');
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
        ROLLBACK;
END;
"""
        else:
            console.print("[cyan]Ingresa el código SQL del procedimiento:[/cyan]")
            sql = console.input("[dim](CREATE OR REPLACE PROCEDURE...):[/dim]\n")
        
        cursor.execute(sql)
        connection.commit()
        console.print(f"[bold green] Procedimiento '{nombre_proc}' creado exitosamente.[/bold green]")
        
    except Exception as e:
        console.print(f"[bold red]Error al crear procedimiento:[/bold red] {e}")


def listar_procedimientos(cursor):
    try:
        cursor.execute("""
            SELECT object_name, created, last_ddl_time, status 
            FROM user_objects 
            WHERE object_type = 'PROCEDURE' 
            ORDER BY object_name
        """)
        procedimientos = cursor.fetchall()
        
        if not procedimientos:
            console.print("\n[bold yellow]No se encontraron procedimientos almacenados.[/bold yellow]\n")
            return []
        
        table = Table(title="Procedimientos Almacenados", box=box.DOUBLE_EDGE, style="cyan", header_style="bold magenta")
        table.add_column("N°", justify="center")
        table.add_column("Nombre", justify="center")
        table.add_column("Fecha Creación", justify="center")
        table.add_column("Última Modificación", justify="center")
        table.add_column("Estado", justify="center")
        
        for i, (nombre, created, modified, status) in enumerate(procedimientos, start=1):
            estado_color = "[green]" if status == "VALID" else "[red]"
            table.add_row(str(i), nombre, str(created), str(modified), f"{estado_color}{status}[/]")
        
        console.print(table)
        return [p[0] for p in procedimientos]
        
    except Exception as e:
        console.print(f"[bold red]Error al listar procedimientos:[/bold red] {e}")
        return []


def ejecutar_procedimiento(cursor, connection):
    procedimientos = listar_procedimientos(cursor)
    
    if not procedimientos:
        return
    
    try:
        opcion = int(console.input("\n[cyan]Selecciona el procedimiento a ejecutar:[/cyan] "))
        if opcion < 1 or opcion > len(procedimientos):
            console.print("[bold yellow]Opción inválida.[/bold yellow]")
            return
        
        nombre_proc = procedimientos[opcion - 1]
        
        cursor.execute(f"""
            SELECT argument_name, data_type, in_out 
            FROM user_arguments 
            WHERE object_name = '{nombre_proc}' 
            ORDER BY position
        """)
        parametros = cursor.fetchall()
        
        valores = []
        if parametros:
            console.print(f"\n[cyan]Parámetros del procedimiento '{nombre_proc}':[/cyan]")
            for param_name, data_type, in_out in parametros:
                if param_name:  
                    valor = console.input(f" ➤ {param_name} ({data_type}, {in_out}): ")
                    valores.append(valor)
            
            params_str = ', '.join([f":{i+1}" for i in range(len(valores))])
            cursor.execute(f"BEGIN {nombre_proc}({params_str}); END;", valores)
        else:
            cursor.execute(f"BEGIN {nombre_proc}; END;")
        
        connection.commit()
        console.print(f"[bold green]✓ Procedimiento '{nombre_proc}' ejecutado correctamente.[/bold green]")
        
    except ValueError:
        console.print("[bold yellow]Ingresa un número válido.[/bold yellow]")
    except Exception as e:
        console.print(f"[bold red]Error al ejecutar procedimiento:[/bold red] {e}")


def eliminar_procedimiento(cursor, connection):
    procedimientos = listar_procedimientos(cursor)
    
    if not procedimientos:
        return
    
    try:
        opcion = int(console.input("\n[cyan]Selecciona el procedimiento a eliminar:[/cyan] "))
        if opcion < 1 or opcion > len(procedimientos):
            console.print("[bold yellow]Opción inválida.[/bold yellow]")
            return
        
        nombre_proc = procedimientos[opcion - 1]
        
        confirmacion = console.input(f"\n[yellow]¿Estás seguro de eliminar el procedimiento '{nombre_proc}'? (S/N):[/yellow] ")
        
        if confirmacion.upper() == 'S':
            cursor.execute(f"DROP PROCEDURE {nombre_proc}")
            connection.commit()
            console.print(f"[bold green]✓ Procedimiento '{nombre_proc}' eliminado correctamente.[/bold green]")
        else:
            console.print("[bold yellow]Operación cancelada.[/bold yellow]")
        
    except ValueError:
        console.print("[bold yellow]Ingresa un número válido.[/bold yellow]")
    except Exception as e:
        console.print(f"[bold red]Error al eliminar procedimiento:[/bold red] {e}")

def crear_trigger(cursor, connection):
    console.print(Panel.fit("[bold white]CREAR TRIGGER[/bold white]", style="bold blue"))
    
    console.print("\n[cyan]Tipos de triggers:[/cyan]")
    console.print("1. BEFORE INSERT - Auditoría de inserción")
    console.print("2. AFTER UPDATE - Auditoría de actualización")
    console.print("3. BEFORE DELETE - Prevenir eliminación")
    console.print("4. Trigger personalizado\n")
    
    opcion = console.input("[cyan]Selecciona el tipo de trigger (1-4):[/cyan] ")
    
    try:
        if opcion == "1":
            nombre_trigger = console.input("[cyan]Nombre del trigger:[/cyan] ")
            tabla = console.input("[cyan]Tabla a monitorear:[/cyan] ")
            
            sql = f"""
CREATE OR REPLACE TRIGGER {nombre_trigger}
BEFORE INSERT ON {tabla}
FOR EACH ROW
BEGIN
    DBMS_OUTPUT.PUT_LINE('Insertando nuevo registro en {tabla}');
    DBMS_OUTPUT.PUT_LINE('Fecha: ' || SYSDATE);
END;
"""
        elif opcion == "2":
            nombre_trigger = console.input("[cyan]Nombre del trigger:[/cyan] ")
            tabla = console.input("[cyan]Tabla a monitorear:[/cyan] ")
            
            sql = f"""
CREATE OR REPLACE TRIGGER {nombre_trigger}
AFTER UPDATE ON {tabla}
FOR EACH ROW
BEGIN
    DBMS_OUTPUT.PUT_LINE('Registro actualizado en {tabla}');
    DBMS_OUTPUT.PUT_LINE('Usuario: ' || USER);
    DBMS_OUTPUT.PUT_LINE('Fecha: ' || SYSDATE);
END;
"""
        elif opcion == "3":
            nombre_trigger = console.input("[cyan]Nombre del trigger:[/cyan] ")
            tabla = console.input("[cyan]Tabla a proteger:[/cyan] ")
            
            sql = f"""
CREATE OR REPLACE TRIGGER {nombre_trigger}
BEFORE DELETE ON {tabla}
FOR EACH ROW
BEGIN
    RAISE_APPLICATION_ERROR(-20001, 'No se permite eliminar registros de {tabla}');
END;
"""
        else:
            console.print("[cyan]Ingresa el código SQL del trigger:[/cyan]")
            sql = console.input("[dim](CREATE OR REPLACE TRIGGER...):[/dim]\n")
        
        cursor.execute(sql)
        connection.commit()
        console.print(f"[bold green]✓ Trigger '{nombre_trigger}' creado exitosamente.[/bold green]")
        
    except Exception as e:
        console.print(f"[bold red]Error al crear trigger:[/bold red] {e}")


def listar_triggers(cursor):
    try:
        cursor.execute("""
            SELECT trigger_name, table_name, triggering_event, status 
            FROM user_triggers 
            ORDER BY trigger_name
        """)
        triggers = cursor.fetchall()
        
        if not triggers:
            console.print("\n[bold yellow]No se encontraron triggers.[/bold yellow]\n")
            return []
        
        table = Table(title="Triggers Básicos", box=box.DOUBLE_EDGE, style="cyan", header_style="bold magenta")
        table.add_column("N°", justify="center")
        table.add_column("Nombre", justify="center")
        table.add_column("Tabla", justify="center")
        table.add_column("Evento", justify="center")
        table.add_column("Estado", justify="center")
        
        for i, (nombre, tabla, evento, status) in enumerate(triggers, start=1):
            estado_color = "[green]" if status == "ENABLED" else "[red]"
            table.add_row(str(i), nombre, tabla, evento, f"{estado_color}{status}[/]")
        
        console.print(table)
        return [t[0] for t in triggers]
        
    except Exception as e:
        console.print(f"[bold red]Error al listar triggers:[/bold red] {e}")
        return []


def eliminar_trigger(cursor, connection):
    triggers = listar_triggers(cursor)
    
    if not triggers:
        return
    
    try:
        opcion = int(console.input("\n[cyan]Selecciona el trigger a eliminar:[/cyan] "))
        if opcion < 1 or opcion > len(triggers):
            console.print("[bold yellow]Opción inválida.[/bold yellow]")
            return
        
        nombre_trigger = triggers[opcion - 1]
        
        confirmacion = console.input(f"\n[yellow]¿Estás seguro de eliminar el trigger '{nombre_trigger}'? (S/N):[/yellow] ")
        
        if confirmacion.upper() == 'S':
            cursor.execute(f"DROP TRIGGER {nombre_trigger}")
            connection.commit()
            console.print(f"[bold green] Trigger '{nombre_trigger}' eliminado correctamente.[/bold green]")
        else:
            console.print("[bold yellow]Operación cancelada.[/bold yellow]")
        
    except ValueError:
        console.print("[bold yellow]Ingresa un número válido.[/bold yellow]")
    except Exception as e:
        console.print(f"[bold red]Error al eliminar trigger:[/bold red] {e}")


def crear_vista(cursor, connection):
    console.print(Panel.fit("[bold white]CREAR VISTA[/bold white]", style="bold blue"))
    
    nombre_vista = console.input("\n[cyan]Nombre de la vista:[/cyan] ")
    console.print("[cyan]Ingresa la consulta SELECT para la vista:[/cyan]")
    consulta = console.input("[dim](SELECT ...):[/dim] ")
    
    try:
        sql = f"CREATE OR REPLACE VIEW {nombre_vista} AS {consulta}"
        cursor.execute(sql)
        connection.commit()
        console.print(f"[bold green] Vista '{nombre_vista}' creada exitosamente.[/bold green]")
        
    except Exception as e:
        console.print(f"[bold red]Error al crear vista:[/bold red] {e}")


def listar_vistas(cursor):
    try:
        cursor.execute("""
            SELECT view_name, text 
            FROM user_views 
            ORDER BY view_name
        """)
        vistas = cursor.fetchall()
        
        if not vistas:
            console.print("\n[bold yellow]No se encontraron vistas.[/bold yellow]\n")
            return []
        
        table = Table(title="Vistas", box=box.DOUBLE_EDGE, style="cyan", header_style="bold magenta")
        table.add_column("N°", justify="center")
        table.add_column("Nombre", justify="center")
        table.add_column("Definición", justify="left", max_width=60)
        
        for i, (nombre, texto) in enumerate(vistas, start=1):
            texto_corto = (texto[:57] + "...") if len(texto) > 60 else texto
            table.add_row(str(i), nombre, texto_corto)
        
        console.print(table)
        return [v[0] for v in vistas]
        
    except Exception as e:
        console.print(f"[bold red]Error al listar vistas:[/bold red] {e}")
        return []


def mostrar_resultados_vista(cursor):
    vistas = listar_vistas(cursor)
    
    if not vistas:
        return
    
    try:
        opcion = int(console.input("\n[cyan]Selecciona la vista a consultar:[/cyan] "))
        if opcion < 1 or opcion > len(vistas):
            console.print("[bold yellow]Opción inválida.[/bold yellow]")
            return
        
        nombre_vista = vistas[opcion - 1]
        
        os.system("cls")
        console.print(Panel.fit(f"Resultados de la vista: [bold magenta]{nombre_vista}[/bold magenta]", style="bold blue"))
        
        cursor.execute(f"SELECT * FROM {nombre_vista}")
        columnas = [col[0] for col in cursor.description]
        filas = cursor.fetchall()
        
        if filas:
            console.print(tabulate(filas, headers=columnas, tablefmt="fancy_grid", showindex="always"))
        else:
            console.print("[bold yellow]La vista no devuelve resultados.[/bold yellow]")
        
    except ValueError:
        console.print("[bold yellow]Ingresa un número válido.[/bold yellow]")
    except Exception as e:
        console.print(f"[bold red]Error al consultar vista:[/bold red] {e}")


def eliminar_vista(cursor, connection):
    vistas = listar_vistas(cursor)
    
    if not vistas:
        return
    
    try:
        opcion = int(console.input("\n[cyan]Selecciona la vista a eliminar:[/cyan] "))
        if opcion < 1 or opcion > len(vistas):
            console.print("[bold yellow]Opción inválida.[/bold yellow]")
            return
        
        nombre_vista = vistas[opcion - 1]
        
        confirmacion = console.input(f"\n[yellow]¿Estás seguro de eliminar la vista '{nombre_vista}'? (S/N):[/yellow] ")
        
        if confirmacion.upper() == 'S':
            cursor.execute(f"DROP VIEW {nombre_vista}")
            connection.commit()
            console.print(f"[bold green]✓ Vista '{nombre_vista}' eliminada correctamente.[/bold green]")
        else:
            console.print("[bold yellow]Operación cancelada.[/bold yellow]")
        
    except ValueError:
        console.print("[bold yellow]Ingresa un número válido.[/bold yellow]")
    except Exception as e:
        console.print(f"[bold red]Error al eliminar vista:[/bold red] {e}")