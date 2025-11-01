from conexion import conectar_bd
from funciones import obtener_tablas, mostrar_tablas, mostrar_datos
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
import os, time

console = Console()

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
    opciones.add_row("3️", "[bold blue]Salir[/bold blue]")
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
            console.print("\n [bold green]Cerrando conexión y saliendo...[/bold green]")
            time.sleep(0.05)
            break
        else:
            console.print("[bold yellow]Opción inválida.[/bold yellow]")
            time.sleep(0.5)

    cursor.close()
    connection.close()
