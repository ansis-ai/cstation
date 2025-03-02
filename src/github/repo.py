import typer
import yaml
import subprocess

from pathlib import Path
from typing import Optional
from typing_extensions import Annotated

app = typer.Typer(no_args_is_help=True)


def load_options(option_file: Path):
    """
        Load options from a YAML file.
    """
    if option_file.exists():
        with open(option_file, "r") as file:
            print(f"Loading options from {option_file}")
            return yaml.safe_load(file)
    

@app.command()
def odoo_sync():
    """
    Update Odoo repositories with ANSIS repositories @ Github ( Version 16.0 - 18.0 )
    \n
    Configuration File : /opt/cstation/ansible_playbook/github/repo_odoo_sync.yaml
    """
    cmd = ["ansible-playbook", "/opt/cstation/ansible_playbook/github/repo_odoo_sync.yaml"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Errors:")
        print(result.stderr)


@app.command()
def odoo_oca_sync(
    version: str = typer.Option('16.0', "--version", "-v", help="Odoo Version => 16.0 - 18.0"),
    server: str = typer.Option('localhost', "--server", "-s", help="Target server to sync OCA repositories")
):
    """
    Update Local Odoo OCA repositories/directories ( Version 16.0 - 18.0 )
    """
    print(f"SERVER: {server}")
    print(f"VERSION: {version}")
    cmd = [
        "ansible-playbook",
        f"/opt/cstation/ansible_playbook/github/repo_oca_sync_{version}.yaml",
        "--limit", server
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Errors:")
        print(result.stderr)

if __name__ == "__main__":
    app()
