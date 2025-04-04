import typer

from github import main as github
from server import main as server
from docker import main as docker

app = typer.Typer(
    no_args_is_help=True,
    help="Control Station (Internal Use)",
    rich_markup_mode="markdown",
)

@app.callback()
def main():
    """Global options for Control Station"""
    pass


app.add_typer(github.app, name="github")
app.add_typer(server.app, name="server")
app.add_typer(docker.app, name="docker")

if __name__ == "__main__":
    app()
