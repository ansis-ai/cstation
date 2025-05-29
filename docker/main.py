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

@deploy_app.command()
def postgresql(
    server: Annotated[str, typer.Argument(help="Target server name from inventory")],
    postgresql_config_file: Annotated[str, typer.Option("--config", "-c", help="PostgreSQL DB Config File")],
):
    """Deploy PostgreSQL container"""
    print(f"Deploying PostgreSQL [{postgresql_config_file}] on server: {server}")
    cmd = [
        "ansible-playbook",
        "/opt/cstation/ansible_playbook/docker/deploy_postgresql.yml",
        "-l", server,
    ]
    subprocess.run(cmd)


@deploy_app.command()
def odoo(
    server: Annotated[str, typer.Argument(help="Target server name from inventory")],
    odoo_container_name: Annotated[
        str, typer.Option("--config", "-c", help="Odoo Config File")
    ],
):
    """Deploy Odoo application"""
    print(f"Deploying Odoo [{odoo_container_name}] on server: {server}")
    cmd = [
        "ansible-playbook",
        "/opt/cstation/ansible_playbook/docker/deploy_odoo.yml",
        "-l", server,
        "-e", f"odoo_container_name={odoo_container_name}"
    ]
    subprocess.run(cmd)

@deploy_app.command()
def traefik(
    server: Annotated[str, typer.Argument(help="Target server name from inventory")],
    version: Annotated[str, typer.Option("--version", "-v", help="Traefik version")] = "latest",
    http_port: Annotated[int, typer.Option("--http-port", help="HTTP port")] = 80,
    https_port: Annotated[int, typer.Option("--https-port", help="HTTPS port")] = 443,
    dashboard_port: Annotated[int, typer.Option("--dashboard-port", help="Dashboard port")] = 5000,
):
    """Deploy Traefik reverse proxy container"""
    print(f"Deploying Traefik {version} on server: {server}")
    cmd = [
        "ansible-playbook",
        "/opt/cstation/ansible_playbook/docker/deploy_traefik.yml",
        "-l", server,
        "-e", f"traefik_version={version}",
        "-e", f"traefik_http_port={http_port}",
        "-e", f"traefik_https_port={https_port}",
        "-e", f"traefik_dashboard_port={dashboard_port}"
    ]
    subprocess.run(cmd)

if __name__ == "__main__":
    app()