import typer
import os
import sys
import ansible_runner
from typing_extensions import Annotated
from utils import get_inventory_hosts

app = typer.Typer(no_args_is_help=True)

@app.command()
def list():
    """List server from inventory"""
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
def ssh_setup(ssh_host: Annotated[str, typer.Argument(help="For Specific Host(s) or All")]):
    print("Setting Up SSH Key to Remote Host...")
    os.chdir('/opt/cstation/ansible_playbook/server/')
    print(f'Setting Up SSH Connection for Host(s): {ssh_host}')
    if ssh_host == "All":
        os.system('ansible-playbook server_ssh.yaml')
    else:
        os.system(f'ansible-playbook -l {ssh_host} server_ssh.yaml')


if __name__ == "__main__":
    app()


