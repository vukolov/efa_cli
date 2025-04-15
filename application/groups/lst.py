import typer
from uuid import UUID
from application.crud.crud import Crud

app = typer.Typer()


@app.command()
def lst(ctx: typer.Context,
        uuid: UUID = typer.Option(default=None, help="Group UUID"),
        name: str = typer.Option(default=None, help="Group name"),
        ):
    url = "/v1/metric-groups/"
    params = {}
    if uuid:
        url += str(uuid)
    elif name:
        params = {"name": name}
    Crud.lst(ctx, url, params, "metric groups")
