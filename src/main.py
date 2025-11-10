from conexion import conectar_bd
from funciones import obtener_tablas, mostrar_tablas, mostrar_datos, insertar_registro, actualizar_registro, eliminar_registro
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
import os, time

console = Console()


def menu_crud(cursor, connection):
    tablas = obtener_tablas(cursor)
    while True:
        os.system("cls")
        console.print(Panel.fit("[bold white]GESTIÓN DE DATOS (CRUD)[/bold white]", style="bold blue"))
        opciones = Table(show_header=False, box=box.SQUARE, style="bright_black")
        opciones.add_row("1️", "[bold cyan]Insertar registros[/bold cyan]")
        opciones.add_row("2️", "[bold cyan]Actualizar registros[/bold cyan]")
        opciones.add_row("3️", "[bold cyan]Eliminar registros[/bold cyan]")
        opciones.add_row("4️", "[bold blue]Volver[/bold blue]")
        console.print(opciones)

        op = console.input("\n [bold white]Selecciona una opción:[/bold white] ")

        if op == "1":
            insertar_registro(cursor, connection, tablas)
            console.input("\n[green]Presiona Enter para continuar...[/green]")
        elif op == "2":
            actualizar_registro(cursor, connection, tablas)
            console.input("\n[green]Presiona Enter para continuar...[/green]")
        elif op == "3":
            eliminar_registro(cursor, connection, tablas)
            console.input("\n[green]Presiona Enter para continuar...[/green]")
        elif op == "4":
            break
        else:
            console.print("[bold yellow]Opción inválida.[/bold yellow]")
            time.sleep(0.5)


def menu_principal():
    os.system("cls")
    titulo = Panel.fit("[bold white]MENÚ PRINCIPAL[/bold white]\n[cyan]Conexión a Oracle XE - Python[/cyan]", 
                    title="SISTEMA DE BASE DE DATOS", 
                    style="bold blue", 
                    border_style="bright_blue")
    console.print(titulo)
    opciones = Table(show_header=False, box=box.SQUARE, style="bright_black")
    opciones.add_row("1️", "[bold cyan]Ver tablas[/bold cyan]")
    opciones.add_row("2️", "[bold cyan]Ver datos de una tabla[/bold cyan]")
    opciones.add_row("3️", "[bold cyan]Gestión de datos (CRUD)[/bold cyan]")
    opciones.add_row("4️", "[bold blue]Salir[/bold blue]")
    console.print(opciones)


connection = conectar_bd()

if connection:
    cursor = connection.cursor()
    while True:
        menu_principal()
        opcion = console.input("\n [bold white]Selecciona una opción:[/bold white] ")
        tablas = obtener_tablas(cursor)

        if opcion == "1":
            os.system("cls")
            mostrar_tablas(tablas)
            console.input("\n[green]Presiona Enter para volver...[/green]")
        elif opcion == "2":
            os.system("cls")
            mostrar_datos(cursor, tablas)
            console.input("\n[green]Presiona Enter para volver...[/green]")
        elif opcion == "3":
            menu_crud(cursor, connection)
        elif opcion == "4":
            console.print("\n [bold green]Cerrando conexión y saliendo del programa...[/bold green]")
            time.sleep(0.05)
            break
        else:
            console.print("[bold yellow]Opción inválida.[/bold yellow]")
            time.sleep(0.5)

    cursor.close()
    connection.close()
else:
    console.print("[bold red]No se pudo establecer la conexión con la base de datos.[/bold red]")
