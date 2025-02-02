import typer
import yaml
import ansible_runner

from pathlib import Path
from typing import Optional
from typing_extensions import Annotated

app = typer.Typer()


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
    result = ansible_runner.run(
        playbook="/opt/cstation/ansible_playbook/github/repo_odoo_sync.yaml",
    )
    print(result)


@app.command()
def odoo_oca_sync( version: str = typer.Option('16.0', "--version", "-v", help="Odoo Version => 16.0 - 18.0")):
    """
    Update Local Odoo OCA repositories/directories ( Version 16.0 - 18.0 )
    """
    print(f"VERSION: {version}")
    result = ansible_runner.run(
        playbook=f"/opt/cstation/ansible_playbook/github/repo_oca_sync_{version}.yaml",
    )
    print(result)

if __name__ == "__main__":
    app()


