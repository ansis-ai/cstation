import os
import subprocess

import typer
from typing_extensions import Annotated

from utils import get_inventory_hosts

app = typer.Typer(no_args_is_help=True, help="Server management commands")

@app.command()
def list():
    """
    List server from inventory
    """
    hosts_data = get_inventory_hosts()
    if not hosts_data:
        print("No server information found in inventory")
        return

    print("\n[Server Information]")
    for group, hosts in hosts_data.items():
        print(f"\nGroup: {group}")
        for host, host_data in hosts.items():
            display_host = host_data.get("ansible_host", host)
            user = host_data.get("ansible_user", "root")
            port = host_data.get("ansible_port", 22)
            print(f"{host}: {display_host}  ({user}@{port})")


if __name__ == "__main__":
    app()
