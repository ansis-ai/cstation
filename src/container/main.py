import typer
from typing_extensions import Annotated
import ansible_runner

app = typer.Typer(no_args_is_help=True, help="Container management commands")

@app.command()
def list(
    server: str = typer.Argument(..., help="sg01, sg02, .... (inventory list) "),
):
    """
        List all containers from a server \n
        server --> sg01 ( cstaion server list )
    """
    typer.echo(f"Listing containers from server: {server}")
    result = ansible_runner.run(
        playbook="/opt/cstation/ansible_playbook/container/list.yml",
        limit=server,
        private_data_dir="/tmp",
    )
    print(result)


@app.command(no_args_is_help=True)
def update(
    server: Annotated[str, typer.Argument(help="server name or group name")],
    container_config: Annotated[
        str, typer.Argument(help="path to container configuration file")
    ],
):
    """
    Update container configuration on the specified server
    """
    print(f"Updating container configuration on server: {server}")
    print(f"Using container configuration file: {container_config}")
    # Add your logic to update the container configuration here
    # For example, you might run an Ansible playbook or other commands


@app.command()
def start(name: str):
    """Start a container"""
    typer.echo(f"Starting container: {name}")

@app.command()
def stop(name: str):
    """Stop a container"""
    typer.echo(f"Stopping container: {name}")