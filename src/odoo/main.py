import typer

app = typer.Typer(no_args_is_help=True)

@app.command()
def restore_db():
    print("RESTORE DB")


if __name__ == "__main__":
    app()
