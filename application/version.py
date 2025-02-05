import typer

app = typer.Typer()


@app.command()
def version():
    print("Events Flow Analyser configuration client Version 0.0.1")
