import typer
from application.crud.crud import Crud

app = typer.Typer()


@app.command()
def add(ctx: typer.Context, name: str):
    Crud.add(ctx=ctx, uri="/v1/metric-groups/", data={"name": name}, entity_type="metric group", entity_name=name)
