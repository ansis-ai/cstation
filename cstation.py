import typer

from server import main as server

app = typer.Typer(
    no_args_is_help=True,
    help="Control Station (Internal Use)",
    rich_markup_mode="markdown",
)

@app.callback()
def main():
    """Global options for Control Station"""
    pass

app.add_typer(server.app, name="server")

if __name__ == "__main__":
    app()
