import typer


from github import main as github
from local import main as local
from odoo import main as odoo
from server import main as server
from container import main as container

app = typer.Typer(no_args_is_help=True, help='Control Station (Internal Use)', rich_markup_mode="markdown")

app.add_typer(github.app, name="github")
app.add_typer(local.app, name="local")
app.add_typer(odoo.app, name="odoo")
app.add_typer(server.app, name="server")
app.add_typer(container.app, name="container")

if __name__ == "__main__":
    app()

