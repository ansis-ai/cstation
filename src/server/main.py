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

@app.command()
def odoo(
    server: Annotated[str, typer.Argument(help="Target server name from inventory")],
    odoo_action: Annotated[str, typer.Argument(help="Action to perform: setup (Odoo + Addons), addons (Addons), dev (Dev Env)")] = "addons",
    ssh_port: Annotated[
        str, typer.Option("--ssh_port", "-p", help="SSH port for the server")
    ] = "22",
    version: Annotated[
        str, typer.Option("--version", "-v", help="Odoo version")
    ] = "6.0",
):
    """
    Manage Odoo server instances
    """
    valid_actions = ["setup", "addons", "dev"]
    if odoo_action not in valid_actions:
        print(f"Invalid action. Please choose from: {', '.join(valid_actions)}")
        return

    if odoo_action == "setup":     
        print(f"Preparing {odoo_action} on Odoo {version} server: {server}")
        cmd = [
            "ansible-playbook",
            "/opt/cstation/ansible_playbook/server/odoo_setup_local.yml",
            "-l",
            "localhost",
            "-e",
            f"odoo_version={version}",
            "-e",
            f"odoo_action={odoo_action}",
        ]
        subprocess.run(cmd)

        print(f"Performing {odoo_action} on Odoo {version} server: {server}")
        cmd = [
            "ansible-playbook",
            "/opt/cstation/ansible_playbook/server/odoo_setup.yml",
            "-l", server,
            "-e", f"odoo_version={version}",
            "-e", f"odoo_action={odoo_action}"
        ]
        subprocess.run(cmd)

    if odoo_action == "addons":
        print(f"Synchonize {odoo_action} for Odoo {version} to server: {server}")
        cmd = [
            "ansible-playbook",
            "/opt/cstation/ansible_playbook/server/odoo_addons.yml",
            "-l", server,
            "-e", f"odoo_version={version}",
            "-e", f"odoo_action={odoo_action}"
        ]
        subprocess.run(cmd)
        return

    if odoo_action == "dev":
        print(f"Synchonize Whole Development Code Structure -  {odoo_action}")
        cmd = [
            "ansible-playbook",
            "/opt/cstation/ansible_playbook/server/odoo_dev.yml",
            "-l",
            server,
            "-e",
            f"odoo_version={version}",
            "-e",
            f"odoo_action={odoo_action}",
        ]
        subprocess.run(cmd)
        return


if __name__ == "__main__":
    app()
