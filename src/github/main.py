import typer

from github import repo as repo


app = typer.Typer()

app.add_typer(repo.app, name="repo")

if __name__ == "__main__":
    app()
