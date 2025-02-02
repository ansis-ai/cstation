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
def odoo_sync(
    command_file: Path = typer.Option(
        Path("/opt/cstation/ansible_playbook/github/repo_odoo_sync.yaml"),
        help="Sync Odoo Repositories from Github",
        file_okay=True,  # Allow files
        dir_okay=False,  # Disallow directories
        readable=True,  # Ensure the file is readable
    ),
):
    """
    Sync the Lcal Odoo repositories with the Github ANSIS repositories
    Using /opt/cstation/ansible_playbook/github/repo_odoo_sync.yaml Playbook
    """
    result = ansible_runner.run(
        playbook="/opt/cstation/ansible_playbook/github/repo_odoo_sync.yaml",
    )
    print(result)


if __name__ == "__main__":
    app()


