import oracledb
from rich.console import Console

console = Console()

def conectar_bd():
    try:
        oracledb.init_oracle_client(lib_dir=r"C:\oraclexe\app\oracle\product\11.2.0\server\BIN")
        connection = oracledb.connect(
            user="lester",
            password="12345",
            dsn="localhost:1521/XE"
        )
        console.print("[bold green]Conexión exitosa a Oracle XE[/bold green]")
        return connection
    except Exception as e:
        console.print(f"[bold red]Error al conectar:[/bold red] {e}")
        return None
