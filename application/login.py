import typer
import os
import requests
from rich.progress import Progress, SpinnerColumn, TextColumn

app = typer.Typer()


@app.command()
def login():
    url = os.getenv("EVENTS_GATEWAY_URL") + "/v1/auth/token"
    data = {
        # "grant_type": "authorization_code",
        # "code": "",
        # "redirect_uri": "",
        "client_id": "cli",
        "client_secret": os.getenv("EVENTS_GATEWAY_SECRET_KEY")
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
    ) as progress:
        progress.add_task(description="Logging in ...", total=None)
        response = requests.post(url, data=data, headers=headers)
        if response.status_code == 200:
            token_data = response.json()
            access_token = token_data.get("access_token")
        else:
            print(f"Failed to log in: {response.status_code}, {response.text}")
