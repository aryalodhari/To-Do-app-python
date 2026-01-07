from flask import Blueprint, redirect, request, url_for, render_template, session, flash 
from app import db
from app.models import Task, User

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/')
def view_tasks():
    if 'uname' not in session:
        return redirect(url_for("auth.login"))

    tasks = Task.query.all()
    return render_template("tasks.html", tasks=tasks)

@tasks_bp.route('/add', methods=["POST"])
def add_tasks():
    if 'uname' not in session:
        return redirect(url_for("auth.login"))
    
    title = request.form.get('title').strip()
    if title:
        new_task = Task(title=title, status = "Pending")
        db.session.add(new_task)
        db.session.commit()
        flash("Task added Successfully!", 'success')
    
    return redirect(url_for("tasks.view_tasks"))

@tasks_bp.route('/toggle/<int:task_id>', methods=["POST"])
def toggle_status(task_id):
    if "uname" not in session:
        return redirect(url_for("auth.login"))
    task = Task.query.get(task_id)
    if task:
        if task.status == 'Pending':
            task.status = 'Working'
        elif task.status == 'Working':
            task.status = 'Done'
        else:
            task.status = 'Pending'
        db.session.commit()
    return redirect(url_for("tasks.view_tasks"))

@tasks_bp.route('/clear', methods=["POST"])
def clear_tasks():
    if "uname" not in session:
        return redirect(url_for("auth.login"))
    Task.query.delete()
    db.session.commit()
    flash("All tasks are deleted!",'danger')
    return redirect(url_for("tasks.view_tasks"))

@tasks_bp.route('/delete/<int:task_id>', methods=["GET"])
def delete_tasks(task_id):
    task = Task.query.get_or_404(task_id)   # fetch task

    db.session.delete(task)                 # delete object
    db.session.commit()

    flash("Task deleted successfully!", "danger")
    return redirect(url_for("tasks.view_tasks"))

