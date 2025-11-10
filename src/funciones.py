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


def insertar_registro(cursor, connection, tablas):
    mostrar_tablas(tablas)
    try:
        opcion = int(console.input("\n[cyan]Selecciona la tabla donde deseas insertar datos:[/cyan] "))
        if opcion < 1 or opcion > len(tablas):
            console.print("[bold yellow]Opción inválida.[/bold yellow]")
            return
        tabla = tablas[opcion - 1]
        cursor.execute(f"SELECT column_name FROM user_tab_columns WHERE table_name = '{tabla}' ORDER BY column_id")
        columnas = [col[0] for col in cursor.fetchall()]

        console.print(Panel.fit(f"Insertando en [bold magenta]{tabla}[/bold magenta]", style="bold blue"))
        valores = []
        for col in columnas:
            val = console.input(f" ➤ [cyan]Ingrese valor para {col}[/cyan]: ")
            if "FECHA" in col.upper():
                val = f"TO_DATE('{val}', 'DD-MM-YYYY')"
            else:
                val = f"'{val}'"
            valores.append(val)

        sql = f"INSERT INTO {tabla} VALUES ({', '.join(valores)})"
        cursor.execute(sql)
        connection.commit()
        console.print("[bold green]Registro insertado correctamente.[/bold green]")

    except Exception as e:
        console.print(f"[bold red]Error al insertar:[/bold red] {e}")


def actualizar_registro(cursor, connection, tablas):
    mostrar_tablas(tablas)
    try:
        opcion = int(console.input("\n[cyan]Selecciona la tabla a actualizar:[/cyan] "))
        if opcion < 1 or opcion > len(tablas):
            console.print("[bold yellow]Opción inválida.[/bold yellow]")
            return
        tabla = tablas[opcion - 1]
        cursor.execute(f"SELECT column_name FROM user_tab_columns WHERE table_name = '{tabla}' ORDER BY column_id")
        columnas = [col[0] for col in cursor.fetchall()]

        console.print(Panel.fit(f"Actualizando [bold magenta]{tabla}[/bold magenta]", style="bold blue"))
        console.print(f"[cyan]Columnas disponibles:[/cyan] {', '.join(columnas)}")

        col_set = console.input("[cyan]Columna a actualizar:[/cyan] ")
        nuevo_valor = console.input("[cyan]Nuevo valor:[/cyan] ")
        col_cond = console.input("[cyan]Columna para condición (WHERE):[/cyan] ")
        val_cond = console.input("[cyan]Valor de condición:[/cyan] ")

        if "FECHA" in col_set.upper():
            sql = f"UPDATE {tabla} SET {col_set} = TO_DATE('{nuevo_valor}', 'DD-MM-YYYY') WHERE {col_cond} = '{val_cond}'"
        else:
            sql = f"UPDATE {tabla} SET {col_set} = '{nuevo_valor}' WHERE {col_cond} = '{val_cond}'"

        cursor.execute(sql)
        connection.commit()
        console.print("[bold green]Registro actualizado correctamente.[/bold green]")

    except Exception as e:
        console.print(f"[bold red]Error al actualizar:[/bold red] {e}")


def eliminar_registro(cursor, connection, tablas):
    mostrar_tablas(tablas)
    try:
        opcion = int(console.input("\n[cyan]Selecciona la tabla de donde eliminar datos:[/cyan] "))
        if opcion < 1 or opcion > len(tablas):
            console.print("[bold yellow]Opción inválida.[/bold yellow]")
            return
        tabla = tablas[opcion - 1]
        cursor.execute(f"SELECT column_name FROM user_tab_columns WHERE table_name = '{tabla}' ORDER BY column_id")
        columnas = [col[0] for col in cursor.fetchall()]

        console.print(Panel.fit(f"Eliminando de [bold magenta]{tabla}[/bold magenta]", style="bold blue"))
        console.print(f"[cyan]Columnas disponibles:[/cyan] {', '.join(columnas)}")

        col_cond = console.input("[cyan]Columna para condición (WHERE):[/cyan] ")
        val_cond = console.input("[cyan]Valor de condición:[/cyan] ")

        sql = f"DELETE FROM {tabla} WHERE {col_cond} = '{val_cond}'"
        cursor.execute(sql)
        connection.commit()
        console.print("[bold green]Registro eliminado correctamente.[/bold green]")

    except Exception as e:
        console.print(f"[bold red]Error al eliminar:[/bold red] {e}")
