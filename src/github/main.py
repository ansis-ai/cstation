import typer

from github import repo as repo


app = typer.Typer(no_args_is_help=True, help="GitHub Repository Management")

app.add_typer(repo.app, name="repo")

if __name__ == "__main__":
    app()
