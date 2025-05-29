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

def load_odoo_repos(odoo_repo_path: Path):
    with open(odoo_repo_path) as f:
        data = yaml.safe_load(f)
        return data[0]["vars"]["repos"]  # Assumes first play contains repo definitions


@app.command()
def odoo_sync(odoo_repo_path: Path = Path("/opt/cstation/etc/repo_odoo_sync.yml")):
    """
    Update Odoo repositories with ANSIS repositories @ Github ( Version 16.0 - 18.0 )
    \n
    Configuration File : /opt/cstation/ansible_playbook/github/repo_odoo_sync.yml
    """
    repos = load_odoo_repos(odoo_repo_path)
    for repo in repos:
        typer.echo(f"\nSyncing {repo['name']}...")
        
        # Sync using GitHub CLI
        try:
            subprocess.run([
                "gh", "repo", "sync",
                "--source", repo["upstream_url"],
                "--branch", repo["branch"],
                repo["fork_url"]
            ], check=True)
            typer.echo(f"✅ Remote sync completed - {repo['name']}")
        except subprocess.CalledProcessError as e:
            typer.echo(f"❌ Remote sync failed: {e}", err=True)
            continue

        # Update local repository
        try:
            subprocess.run(
                ["git", "pull"],
                cwd=repo["local_dir"],
                check=True
            )
            typer.echo(
                f"✅ Local pull completed for {repo['name']} {repo['local_dir']}"
            )
        except subprocess.CalledProcessError as e:
            typer.echo(f"❌ Local pull failed: {e}", err=True)




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
