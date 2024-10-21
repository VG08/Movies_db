from rich.table import Table
from rich.console import Console
import os

def print_table(title, columns, data):
    clear_screen()

    table = Table(title=title, padding=1)
    for column in columns:
        table.add_column(column, overflow="ellipsis")

    for row in data:
        l = [str(x) for x in row]
        table.add_row(*l)
    console = Console()
    console.print(table)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")