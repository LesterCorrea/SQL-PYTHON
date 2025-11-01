import oracledb
from tabulate import tabulate
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
import os
import time

console = Console()

oracledb.init_oracle_client(lib_dir=r"C:\oraclexe\app\oracle\product\11.2.0\server\BIN")

def conectar_bd():
    try:
        connection = oracledb.connect(
            user="lester",
            password="12345",
            dsn="localhost:1521/XE"
        )
        return connection
    except Exception as e:
        console.print(f"[bold red]Error al conectar:[/bold red] {e}")
        return None

def obtener_tablas(cursor):
    cursor.execute("SELECT table_name FROM user_tables ORDER BY table_name")
    return [t[0] for t in cursor.fetchall()]

def mostrar_tablas(tablas):
    if not tablas:
        console.print("\n[bold yellow]No se encontraron tablas en el usuario actual.[/bold yellow]\n")
    else:
        table = Table(title="Tablas disponibles", box=box.DOUBLE_EDGE, style="cyan", header_style="bold magenta")
        table.add_column("N°", justify="center")
        table.add_column("Nombre de la tabla", justify="center")

        for i, t in enumerate(tablas, start=1):
            table.add_row(str(i), t)

        console.print(table)

def mostrar_datos(cursor, tablas):
    if not tablas:
        console.print("\n[bold yellow]No hay tablas para mostrar.[/bold yellow]\n")
        return

    mostrar_tablas(tablas)

    try:
        opcion = int(console.input("\n [bold cyan]Ingresa el número de la tabla que deseas visualizar:[/bold cyan] "))
        if opcion < 1 or opcion > len(tablas):
            console.print("[bold yellow]Opción inválida.[/bold yellow]")
            return

        nombre_tabla = tablas[opcion - 1]
        os.system("cls")
        console.print(Panel.fit(f"Mostrando datos de la tabla: [bold magenta]{nombre_tabla}[/bold magenta]", style="bold blue"))

        cursor.execute(f"SELECT * FROM {nombre_tabla}")
        columnas = [col[0] for col in cursor.description]
        filas = cursor.fetchall()

        if filas:
            console.print(tabulate(filas, headers=columnas, tablefmt="fancy_grid", showindex="always"))
        else:
            console.print("[bold yellow]La tabla está vacía.[/bold yellow]")
    except ValueError:
        console.print("[bold yellow]Ingresa un número válido.[/bold yellow]")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

def ejecutar_consulta(cursor, connection):
    while True:
        os.system("cls")
        console.print(Panel.fit("[bold white]CONSULTAS SQL PERSONALIZADAS[/bold white]", style="bold blue"))

        console.print("[bold cyan]Escribe tu consulta SQL completa abajo.[/bold cyan]")
        console.print("[dim]Ejemplo: SELECT * FROM ALUMNOS[/dim]")
        console.print("[dim]Escribe 'volver' para regresar al menú principal.[/dim]\n")

        sql = console.input("[green]SQL> [/green]")

        if sql.lower().strip() == "volver":
            break

        try:
            cursor.execute(sql)
            
            if cursor.description:
                columnas = [col[0] for col in cursor.description]
                filas = cursor.fetchall()
                if filas:
                    console.print(tabulate(filas, headers=columnas, tablefmt="fancy_grid", showindex="always"))
                else:
                    console.print("[yellow]La consulta no devolvió resultados.[/yellow]")
            else:
                connection.commit()
                console.print(f"[bold green]Consulta ejecutada correctamente.[/bold green]")
        except Exception as e:
            console.print(f"[bold red]Error al ejecutar la consulta:[/bold red] {e}")

        console.input("\n[green]Presiona Enter para continuar...[/green]")

def menu():
    os.system("cls")
    titulo = Panel.fit("[bold white]MENÚ PRINCIPAL[/bold white]\n[cyan]Conexión a Oracle XE - Python[/cyan]", 
                        title="SISTEMA DE BASE DE DATOS", 
                        style="bold blue", 
                        border_style="bright_blue")
    console.print(titulo)

    opciones = Table(show_header=False, box=box.SQUARE, style="bright_black")
    opciones.add_row("1️", "[bold cyan]Ver tablas[/bold cyan]")
    opciones.add_row("2️", "[bold cyan]Ver datos de una tabla[/bold cyan]")
    opciones.add_row("3️", "[bold cyan]Ejecutar consulta SQL personalizada[/bold cyan]")
    opciones.add_row("4️", "[bold blue]Salir[/bold blue]")

    console.print(opciones)


connection = conectar_bd()

if connection:
    cursor = connection.cursor()
    
    while True:
        menu()
        opcion = console.input("\n [bold white]Selecciona una opción:[/bold white] ")
        if opcion == "1":
            os.system("cls")
            tablas = obtener_tablas(cursor)
            mostrar_tablas(tablas)
            console.input("\n[green]Presiona Enter para volver...[/green]")
            
        elif opcion == "2":
            os.system("cls")
            tablas = obtener_tablas(cursor)
            mostrar_datos(cursor, tablas)
            console.input("\n[green]Presiona Enter para volver...[/green]")

        elif opcion == "3":
            ejecutar_consulta(cursor, connection)

        elif opcion == "4":
            console.print("\n [bold green]Cerrando conexión y saliendo del programa...[/bold green]")
            time.sleep(0.05)
            break

        else:
            console.print("[bold yellow]Opción inválida. Intenta nuevamente.[/bold yellow]")
            time.sleep(0.5)

    cursor.close()
    connection.close()
else:
    console.print("[bold red]No se pudo establecer la conexión con la base de datos.[/bold red]")
