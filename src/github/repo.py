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
    Configuration File : /opt/cstation/ansible_playbook/github/repo_odoo_sync.yml
    """
    cmd = ["ansible-playbook", "/opt/cstation/ansible_playbook/github/repo_odoo_sync.yml"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Errors:")
        print(result.stderr)


@app.command()
def odoo_oca_sync(
    version: str = typer.Option('6.0', "--version", "-v", help="Odoo Version => 6.0 - 18.0"),
):
    """
    Update Odoo OCA repositories/directories ( Version 16.0 - 18.0 )
    """
    cmd = [
        "gitoo",
        "install-all",
        f"--conf_file=/opt/PW/PW_ADDONS.{version}/OCA/{version}.yml",
        f"--destination=/opt/PW/PW_ADDONS.{version}/OCA",
    ]
    with subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,  # Combine stdout and stderr
        text=True,
        bufsize=1
    ) as proc:
        for line in proc.stdout:
            print(line, end='')

        proc.wait()
        if proc.returncode != 0:
            print(f"Command failed with exit code {proc.returncode}")
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Errors:")
        print(result.stderr)

if __name__ == "__main__":
    app()
