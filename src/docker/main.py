import typer

app = typer.Typer()

@app.command()
def deploy():
    print("DEPLOY")


if __name__ == "__main__":
    app()
