import typer
from application.crud.crud import Crud

app = typer.Typer()


@app.command()
def add(ctx: typer.Context, name: str):
    Crud.add(ctx=ctx, uri="/v1/metrics/", data={"name": name}, entity_type="metric", entity_name=name)
