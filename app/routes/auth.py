from flask import (
    Blueprint,
    render_template,
    redirect,
    flash,
    session,
    request,
    url_for
)

# Blueprint definition
auth_bp = Blueprint("auth", __name__)

# Temporary hardcoded credentials (for learning only)
USER_CREDENTIALS = {
    "username": "admin",
    "password": "12345"
}


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username").strip()
        password = request.form.get("password").strip()

        # Validate credentials
        if username == USER_CREDENTIALS["username"] and password == USER_CREDENTIALS["password"]:
            session["user"] = username
            flash("Login successful", "success")
            return redirect(url_for("tasks.view_tasks"))
        else:
            flash("Invalid username or password", "danger")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out successfully", "danger")
    return redirect(url_for("auth.login"))
