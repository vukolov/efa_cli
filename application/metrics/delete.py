import typer

app = typer.Typer()


@app.command()
def delete(name: str):
    #todo: implement the logic
    print(f"Deleting metric: {name}")