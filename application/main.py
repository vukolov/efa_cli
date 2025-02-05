import typer
import os
import dotenv
from .metrics import app as metrics_app
from .version import app as version_app
from .login import app as login_app


environment = os.getenv("ENV", "dev")
dotenv.load_dotenv(f"configs/.env.{environment}")

app = typer.Typer()

app.add_typer(version_app)
app.add_typer(login_app)
app.add_typer(metrics_app, name="metrics")


if __name__ == "__main__":
    app()
