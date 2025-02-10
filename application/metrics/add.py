import os
import typer
import requests
from rich.progress import Progress, SpinnerColumn, TextColumn

app = typer.Typer()


@app.command()
def add(ctx: typer.Context, name: str):
    if ctx.obj is None:
        typer.echo("Error: session not passed to the context", err=True)
        raise typer.Exit(code=1)

    session: requests.Session = ctx.obj["session"]
    url = os.getenv("EVENTS_GATEWAY_URL") + "/v1/metrics/"
    data = {"name": name}
    headers = {"Content-Type": "application/json"}
    with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
    ) as progress:
        progress.add_task(description=f"Adding metric: {name} ...", total=None)
        response = session.post(url, json=data, headers=headers)
        if response.status_code == 201:
            print(f"metric {name} has been added")
        else:
            print(f"Failed to add metric: {response.status_code}, {response.text}")