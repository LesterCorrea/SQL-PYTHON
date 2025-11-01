from tabulate import tabulate
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
import os

console = Console()

def obtener_tablas(cursor):
    cursor.execute("SELECT table_name FROM user_tables ORDER BY table_name")
    return [t[0] for t in cursor.fetchall()]

def mostrar_tablas(tablas):
    if not tablas:
        console.print("\n[bold yellow]No se encontraron tablas en el usuario actual.[/bold yellow]\n")
        return
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
        opcion = int(console.input("\n[bold cyan]Ingresa el número de la tabla que deseas visualizar:[/bold cyan] "))
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
