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


@app.command()
def setup(
    server: Annotated[str, typer.Argument(help="Target server name from inventory")]
):
    """
    Setup and configure a server with required packages and configurations
    """
    print(f"Setting up server: {server}")
    cmd = [
        "ansible-playbook",
        "/opt/cstation/ansible_playbook/server/setup.yml",
        "-l", server
    ]
    subprocess.run(cmd)

if __name__ == "__main__":
    app()
