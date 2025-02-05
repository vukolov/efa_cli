import typer

from .add import app as add_app
from .delete import app as delete_app

app = typer.Typer(no_args_is_help=True)

app.add_typer(add_app)
app.add_typer(delete_app)