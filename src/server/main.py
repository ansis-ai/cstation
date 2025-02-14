import os

import typer
from typing_extensions import Annotated

from utils import get_inventory_hosts

app = typer.Typer(no_args_is_help=True, help="Server management commands")
container_app = typer.Typer(help="Container management commands")
app.add_typer(container_app, name="container")


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


@app.command(no_args_is_help=True)
def ssh_setup(
    server: Annotated[str, typer.Argument(help="server name or group name (All)")],
):
    """
    Setting up SSH key for server(s) \n
    For server name: cstation server list
    """
    print("Setting up SSH key to remote server ...")
    os.chdir("/opt/cstation/ansible_playbook/server/")
    print(f"Setting up SSH connection for host(s): {server}")
    if server == "All":
        os.system("ansible-playbook server_ssh.yml")
    else:
        os.system(f"ansible-playbook -l {server} server_ssh.yml")


if __name__ == "__main__":
    app()
