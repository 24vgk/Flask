from flask import Blueprint, render_template
from flask_login import login_required

secret_app = Blueprint("secret_app", __name__)


@secret_app.route("/", endpoint="secret")
@login_required
def secret_list():
    return render_template("secret/secret.html")