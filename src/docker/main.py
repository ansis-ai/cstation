import typer
from typing_extensions import Annotated
import subprocess

app = typer.Typer(no_args_is_help=True, help="Docker management commands")
deploy_app = typer.Typer(no_args_is_help=True, help="Deploy container applications")
app.add_typer(deploy_app, name="deploy")

@app.command()
def setup(
    server: Annotated[str, typer.Argument(help="Target server name from inventory")]
):
    """Setup Docker on the target server"""
    print(f"Setting up Docker on server: {server}")
    cmd = [
        "ansible-playbook",
        "/opt/cstation/ansible_playbook/docker/docker_setup.yml",
        "-l", server
    ]
    subprocess.run(cmd)

@deploy_app.command()
def portainer(
    server: Annotated[str, typer.Argument(help="Target server name from inventory")],
    version: Annotated[str, typer.Option("--version", "-v", help="Portainer version")] = "ce-latest",
    port: Annotated[int, typer.Option("--port", "-p", help="Portainer web UI port")] = 9000,
):
    """Deploy Portainer container"""
    print(f"Deploying Portainer {version} on server: {server}")
    cmd = [
        "ansible-playbook",
        "/opt/cstation/ansible_playbook/docker/deploy_portainer.yml",
        "-l", server,
        "-e", f"portainer_version={version}",
        "-e", f"portainer_port={port}"
    ]
    subprocess.run(cmd)

if __name__ == "__main__":
    app()