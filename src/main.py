from conexion import conectar_bd
from funciones import obtener_tablas, mostrar_tablas, mostrar_datos, insertar_registro, actualizar_registro, eliminar_registro
from funciones_avanzadas import (
    crear_procedimiento_almacenado, listar_procedimientos, ejecutar_procedimiento, eliminar_procedimiento,
    crear_trigger, listar_triggers, eliminar_trigger,
    crear_vista, listar_vistas, mostrar_resultados_vista, eliminar_vista
)
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
import os, time

console = Console()


def menu_procedimientos(cursor, connection):
    """Menú para gestionar procedimientos almacenados"""
    while True:
        os.system("cls")
        console.print(Panel.fit("[bold white]PROCEDIMIENTOS ALMACENADOS[/bold white]", style="bold blue"))
        opciones = Table(show_header=False, box=box.SQUARE, style="bright_black")
        opciones.add_row("1️", "[bold cyan]Crear procedimiento[/bold cyan]")
        opciones.add_row("2️", "[bold cyan]Listar procedimientos[/bold cyan]")
        opciones.add_row("3️", "[bold cyan]Ejecutar procedimiento[/bold cyan]")
        opciones.add_row("4️", "[bold red]Eliminar procedimiento[/bold red]")
        opciones.add_row("5️", "[bold blue]Volver[/bold blue]")
        console.print(opciones)

        op = console.input("\n [bold white]Selecciona una opción:[/bold white] ")

        if op == "1":
            os.system("cls")
            crear_procedimiento_almacenado(cursor, connection)
            console.input("\n[green]Presiona Enter para continuar...[/green]")
        elif op == "2":
            os.system("cls")
            listar_procedimientos(cursor)
            console.input("\n[green]Presiona Enter para continuar...[/green]")
        elif op == "3":
            os.system("cls")
            ejecutar_procedimiento(cursor, connection)
            console.input("\n[green]Presiona Enter para continuar...[/green]")
        elif op == "4":
            os.system("cls")
            eliminar_procedimiento(cursor, connection)
            console.input("\n[green]Presiona Enter para continuar...[/green]")
        elif op == "5":
            break
        else:
            console.print("[bold yellow]Opción inválida.[/bold yellow]")
            time.sleep(0.5)


def menu_triggers(cursor, connection):
    """Menú para gestionar triggers"""
    while True:
        os.system("cls")
        console.print(Panel.fit("[bold white]TRIGGERS BÁSICOS[/bold white]", style="bold blue"))
        opciones = Table(show_header=False, box=box.SQUARE, style="bright_black")
        opciones.add_row("1️", "[bold cyan]Crear trigger[/bold cyan]")
        opciones.add_row("2️", "[bold cyan]Listar triggers[/bold cyan]")
        opciones.add_row("3️", "[bold red]Eliminar trigger[/bold red]")
        opciones.add_row("4️", "[bold blue]Volver[/bold blue]")
        console.print(opciones)

        op = console.input("\n [bold white]Selecciona una opción:[/bold white] ")

        if op == "1":
            os.system("cls")
            crear_trigger(cursor, connection)
            console.input("\n[green]Presiona Enter para continuar...[/green]")
        elif op == "2":
            os.system("cls")
            listar_triggers(cursor)
            console.input("\n[green]Presiona Enter para continuar...[/green]")
        elif op == "3":
            os.system("cls")
            eliminar_trigger(cursor, connection)
            console.input("\n[green]Presiona Enter para continuar...[/green]")
        elif op == "4":
            break
        else:
            console.print("[bold yellow]Opción inválida.[/bold yellow]")
            time.sleep(0.5)


def menu_vistas(cursor, connection):
    """Menú para gestionar vistas"""
    while True:
        os.system("cls")
        console.print(Panel.fit("[bold white]VISTAS[/bold white]", style="bold blue"))
        opciones = Table(show_header=False, box=box.SQUARE, style="bright_black")
        opciones.add_row("1️", "[bold cyan]Crear vista[/bold cyan]")
        opciones.add_row("2️", "[bold cyan]Listar vistas[/bold cyan]")
        opciones.add_row("3️", "[bold cyan]Mostrar resultados de vista[/bold cyan]")
        opciones.add_row("4️", "[bold red]Eliminar vista[/bold red]")
        opciones.add_row("5️", "[bold blue]Volver[/bold blue]")
        console.print(opciones)

        op = console.input("\n [bold white]Selecciona una opción:[/bold white] ")

        if op == "1":
            os.system("cls")
            crear_vista(cursor, connection)
            console.input("\n[green]Presiona Enter para continuar...[/green]")
        elif op == "2":
            os.system("cls")
            listar_vistas(cursor)
            console.input("\n[green]Presiona Enter para continuar...[/green]")
        elif op == "3":
            os.system("cls")
            mostrar_resultados_vista(cursor)
            console.input("\n[green]Presiona Enter para continuar...[/green]")
        elif op == "4":
            os.system("cls")
            eliminar_vista(cursor, connection)
            console.input("\n[green]Presiona Enter para continuar...[/green]")
        elif op == "5":
            break
        else:
            console.print("[bold yellow]Opción inválida.[/bold yellow]")
            time.sleep(0.5)


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
    opciones.add_row("4️", "[bold cyan]Procedimientos almacenados[/bold cyan]")
    opciones.add_row("5", "[bold cyan]Triggers básicos[/bold cyan]")
    opciones.add_row("6️", "[bold cyan]Vistas[/bold cyan]")
    opciones.add_row("7️", "[bold blue]Salir[/bold blue]")
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
            menu_procedimientos(cursor, connection)
        elif opcion == "5":
            menu_triggers(cursor, connection)
        elif opcion == "6":
            menu_vistas(cursor, connection)
        elif opcion == "7":
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