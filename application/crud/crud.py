import os
import typer
import requests
from tabulate import tabulate
from rich.progress import Progress, SpinnerColumn, TextColumn


class Crud:
    @staticmethod
    def add(ctx: typer.Context,
            uri: str,
            data: dict,
            entity_type: str,
            entity_name: str):
        if ctx.obj is None:
            typer.echo("Error: session not passed to the context", err=True)
            raise typer.Exit(code=1)

        session: requests.Session = ctx.obj["session"]
        url = os.getenv("EVENTS_GATEWAY_URL") + uri
        headers = {"Content-Type": "application/json"}
        with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                transient=True,
        ) as progress:
            progress.add_task(description=f"Adding {entity_type}: {entity_name} ...", total=None)
            response = session.post(url, json=data, headers=headers)
            if response.status_code == 201:
                print(f"{entity_type} {entity_name} has been added")
            else:
                print(f"Failed to add {entity_type}: {response.status_code}, {response.text}")

    @staticmethod
    def lst(ctx: typer.Context,
            uri: str,
            params: dict,
            entity_type: str):
        if ctx.obj is None:
            typer.echo("Error: session not passed to the context", err=True)
            raise typer.Exit(code=1)

        session: requests.Session = ctx.obj["session"]
        url = os.getenv("EVENTS_GATEWAY_URL") + uri
        headers = {"Content-Type": "application/json"}
        with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                transient=True,
        ) as progress:
            progress.add_task(description=f"Getting the list of {entity_type}...", total=None)
            response = session.get(url, headers=headers, params=params)
            if response.status_code == 200:
                records = response.json()
                if type(records) is not list:
                    records = [records]
                if len(records) == 0:
                    print(f"No {entity_type} found")
                    return
                headers = records[0].keys()
                table_rows = [[record[h] for h in headers] for record in records]
                print(tabulate(table_rows, headers=headers, tablefmt="pretty"))
            else:
                print(f"Failed to get the {entity_type} list: {response.status_code}, {response.text}")
