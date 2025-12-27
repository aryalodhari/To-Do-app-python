from app import create_app, db
from app.models import Task

app = create_app()

# temporarily tells flask: This is the active app right now and only work when Flask knows which app is currently active.
with app.app_context():
    db.create_all() # it looks the models and makes sure table must be exist in database and if file is not exist then it creates it.

if __name__ == '__main__':
    app.run(debug=True)