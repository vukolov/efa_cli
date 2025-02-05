import os
import typer
import requests
from rich.progress import Progress, SpinnerColumn, TextColumn

app = typer.Typer()


@app.command()
def add(name: str):
    url = os.getenv("EVENTS_GATEWAY_URL") + "/v1/metrics"
    data = {"key": "value"}
    headers = {"Authorization": "Bearer YOUR_TOKEN", "Content-Type": "application/json"}
    with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
    ) as progress:
        progress.add_task(description=f"Adding metric: {name} ...", total=None)
        response = requests.post(url, json=data, headers=headers)
    print(f"metric {name} has benn added")
