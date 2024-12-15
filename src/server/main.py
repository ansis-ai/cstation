import typer
import os

from typing_extensions import Annotated

app = typer.Typer(no_args_is_help=True)

@app.command(no_args_is_help=True)
def ssh_setup(ssh_login: Annotated[str, typer.Argument()], ssh_port: Annotated[int, typer.Argument()] = 22):
    print("Setting Up SSH Key to Remote Host...")
    os.system(f'ssh-copy-id -p {ssh_port} {ssh_login}')


if __name__ == "__main__":
    app()
