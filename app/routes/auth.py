from flask import (
    Blueprint,
    render_template,
    redirect,
    flash,
    session,
    request,
    url_for
)
from app.models import User
from app import db

# Blueprint definition
auth_bp = Blueprint("auth", __name__)

# Temporary hardcoded credentials (for learning only)
# USER_CREDENTIALS = {
#     "username": "admin",
#     "password": "12345"
# }


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email").strip()
        password = request.form.get("password").strip()

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            session['email'] = user.email
            flash("Login successful", "success")
            return redirect(url_for("auth.dashboard"))
        else:
            return render_template("login.html", error='Invalid user!')
    
    return render_template("login.html")
    #     # Validate credentials
    #     if username == USER_CREDENTIALS["username"] and password == USER_CREDENTIALS["password"]:
    #         session["user"] = username
    #         flash("Login successful", "success")
    #         return redirect(url_for("tasks.view_tasks"))
    #     else:
    #         flash("Invalid username or password", "danger")

    # return render_template("login.html")

@auth_bp.route("/register", methods=["GET","POST"])
def register():
    if request.method == 'POST':
        # handle request
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("Register successful", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html")

@auth_bp.route("/dashboard")
def dashboard():
    if session['email']:
        user = User.query.filter_by(email=session['email']).first()
        return render_template("dashboard.html",user=user)
    return redirect(url_for("auth.login"))

@auth_bp.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out successfully", "danger")
    return redirect(url_for("auth.login"))
