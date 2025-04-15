import typer
import os
import dotenv
import requests
from .auth.auth import TokenAuth, AutoRefreshAdapter
from .metrics import app as metrics_app
from .groups import app as metric_groups_app
from .version import app as version_app
from .login import app as login_app


environment = os.getenv("ENV", "dev")
dotenv.load_dotenv(f"configs/.env.{environment}")

app = typer.Typer()

session = requests.Session()
session.auth = TokenAuth(os.getenv("EVENTS_GATEWAY_URL") + "/v1/auth/token",
                 os.getenv("EVENTS_GATEWAY_CLIENT_ID"),
                 os.getenv("EVENTS_GATEWAY_SECRET_KEY"))
session.headers.update({"Authorization": f"Bearer {session.auth.token}"})
session.mount("https://", AutoRefreshAdapter(session.auth, session))
session.mount("http://", AutoRefreshAdapter(session.auth, session))

session_context = {"obj": {"session": session}}
app.context_settings = session_context

app.add_typer(version_app, name="version", context_settings=session_context)
app.add_typer(login_app, name="login", context_settings=session_context)
app.add_typer(metrics_app, name="metrics", context_settings=session_context)
app.add_typer(metric_groups_app, name="groups", context_settings=session_context)


if __name__ == "__main__":
    app()
