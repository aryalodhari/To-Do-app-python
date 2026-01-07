
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from app.models import Task   # 🔥 IMPORTANT

    with app.app_context():
        db.create_all()           # 🔥 THIS CREATES task TABLE

    from app.routes.tasks import tasks_bp
    from app.routes.auth import auth_bp

    app.register_blueprint(tasks_bp)
    app.register_blueprint(auth_bp)

    return app


# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# # create database object globally
# db = SQLAlchemy()

# def create_app():
#     app = Flask(__name__) #app or kind of engine

#     app.config['SECRET_KEY'] = 'your_secret_key'
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     db.__init__(app)

#     from app.routes.auth import auth_bp
#     from app.routes.tasks import tasks_bp
#     # register_blueprint() tells flask = Attach these routes (URLs) from another file to my main app
#     app.register_blueprint(auth_bp) 
#     app.register_blueprint(tasks_bp)

#     return app